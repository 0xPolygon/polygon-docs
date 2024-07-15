The Storage SM is one of zkProver's secondary state machines, and thus receives instructions from the Main SM called Storage Actions. The Storage Actions basically refer to the verification of CRUD operations executed by the Main SM.

The Storage SM is designed as a microprocessor and it is therefore composed of three parts:

- Storage Assembly code,
- Storage executor code,
- Storage PIL code.

## Storage assembly

The Storage Assembly is the interpreter between the Main State Machine and its own Executor.

The Storage SM receives instructions from the Main SM written in zkASM. It then generates a JSON-file containing the corresponding rules and logic, which are stored in a special ROM for the Storage SM.

The Storage SM has a primary Storage Assembly code that maps each instruction of the Main SM to the secondary Assembly code corresponding to each basic operation. These basic operations are mainly the CREATE, READ, UPDATE and DELETE, as discussed in previous sections.

Considering some special cases, there are eight secondary [Storage Assembly](https://github.com/0xPolygonHermez/zkevm-storage-rom/tree/main/zkasm) codes all-in-all, each for a distinct basic operation. We list these in the table below.

| Storage Actions                   | File Names         | Code Names | Action Selectors In Primary zkASM Code |
| --------------------------------- | ------------------ | ---------- | -------------------------------------- |
| READ                              | Get                | Get        | isGet()                                |
| UPDATE                            | Set_Update         | SU         | isSetUpdate()                          |
| CREATE new value at a found leaf  | Set_InsertFound    | SIF        | isSetInsertFound()                     |
| CREATE new value at a zero node   | Set_InsertNotFound | SINF       | isSetInsertNotFound()                  |
| DELETE last non-zero node         | Set_DeleteLast     | SDL        | isSetDeleteLast()                      |
| DELETE leaf with non-zero sibling | Set_DeleteFound    | SDF        | isSetDeleteFound()                     |
| DELETE leaf with zero sibling     | Set_DeleteNotFound | SDNF       | isSetDeleteNotFound()                  |
| SET a zero node to zero           | Set_ZeroToZero     | SZTZ       | isSetZeroToZero()                      |

Input and output states of the Storage SM are literally SMTs, given in the form of; the Merkle roots, the relevant siblings, as well as the key-value pairs.

Note that state machines use registers in the place of variables. All values needed, for carrying out the basic operations, are stored by the primary Assembly code in the following registers;

_HASH_LEFT_, _HASH_RIGHT_, _OLD_ROOT_, _NEW_ROOT_, _VALUE_LOW_, _VALUE_HIGH_, _SIBLING_VALUE_HASH_, _RKEY_, _SIBLING_RKEY_, _RKEY_BIT_, _LEVEL_.

The _SIBLING_VALUE_HASH_ and _SIBLING_RKEY_ registers are only used by the _Set_InsertFound_ and the _Set_DeleteFound_ secondary Assembly codes. The rest of the registers are used in all the secondary Assembly codes.

## SMT Action selectors in primary assembly code

The Primary Assembly Code maps the Main SM instructions to the relevant Storage Actions using selectors. Like switches can either be ON or OFF, selectors can either be 1 or 0, where 1 means the action is selected for execution, while 0 means the instruction does not tally with the required action so a "jump if zero" _JMPZ_ is applied.

The primary Assembly code uses selectors by following the sequence in which these Storage Actions are listed in the above table. That is,

- It first checks if the required action is a _Get_. If it is so, the [storage_sm_get.zkasm](https://github.com/0xPolygonHermez/zkevm-storage-rom/blob/main/zkasm/storage_sm_get.zkasm) code is fetched for execution.
- If not, it checks if the required action is _Set_Update_. If it is so, the [storage_sm_set_update.zkasm](https://github.com/0xPolygonHermez/zkevm-storage-rom/blob/main/zkasm/storage_sm_set_update.zkasm) code is fetched for execution.
- If not, it continues to check if the required action is _Set_InsertFound_. If it is so, the [storage_sm_set_insert_found.zkasm](https://github.com/0xPolygonHermez/zkevm-storage-rom/blob/main/zkasm/storage_sm_set_insert_found.zkasm) code is fetched for execution.
- If not, it continues in the same way until the correct action is selected, in which case the corresponding code is fetched for execution.

That's all the primary Storage Assembly code does and the details of how each of the SMT Actions is stipulated in the individual secondary Assembly codes.

The primary and secondary Storage Assembly files are stored as JSON-files in the Storage ROM, ready to be fetched as function calls by the Storage Executor.

## The UPDATE zkASM code

Take as an example the _Set_UPDATE_ zkASM code. The primary Storage Assembly code uses the selector _isSetUpdate()_ for _Set_UPDATE_.

Note that an UPDATE involves the following actions:

1. Reconstructs the corresponding key, from both the remaining key found at the leaf and key-bits used to navigate to the leaf.
2. Ascertains that indeed the old value was included in the old root,
3. Carries out the UPDATE of the old value with the new value, as well as updating all nodes along the path from the leaf to the root.

There is only one _Set_UPDATE_ Assembly code, [storage_sm_set_update.zkasm](https://github.com/0xPolygonHermez/zkevm-storage-rom/blob/main/zkasm/storage_sm_set_update.zkasm), for all the above three computations.

### Key reconstruction in zkASM

Key Reconstruction is achieved in two steps: positioning of the bit "1" in the _LEVEL_ register, and using the _LEVEL_ register to climb the RKey. That is, append the path bit last used in navigation to the correct RKey part.

1. Positioning the bit "1" in the _LEVEL_ register

   The _Set_UPDATE_ zkASM code, first initialises the _LEVEL_ register to _(1,0,0,0)_. Then uses the _GetLevelBit()_ function to read the two least-significant bits of the leaf level, which happens in two cases, each with its own two subcases:

   Case 1. If the least-significant bit of leaf level is _0_, then the _GetLevelBit()_ function is used again to read the second least-significant bit of the leaf level.

   - Subcase 1.1: If the second least-significant bit of the leaf level is _0_, it means the leaf level is a multiple of 4, which is equivalent to 0 because leaf level works in _modulo_ 4. So, the _LEVEL_ register must remain as _(1,0,0,0)_.
   - Subcase 1.2:  If the second least-significant bit of the leaf level is _1_, it means the leaf level in its binary form ends with a _10_. Hence, leaf level is a number of the form _2 + 4k_, for some positive integer _k_. As a result, the _LEVEL_ register must be rotated to the position, _(0,0,1,0)_. The code therefore applies _ROTATE_LEVEL_ twice to _LEVEL = (1,0,0,0)_ in order to bring it to _(0,0,1,0)_.

   Case 2. If the least-significant bit of leaf level is _1_; then, the _LEVEL_ register is rotated three times to the left, using ROTATE_LEVEL, and bringing the _LEVEL_ register to _(0,1,0,0)_. Next, the _GetLevelBit()_ function is used again to read the second least-significant bit of the leaf level.

   - Subcase 2.1: If the second least-significant bit of the leaf level is _0_, it means the leaf level in its binary form ends with a _01_. That is, leaf level is a number of the form _1 + 4k_, for some positive integer _k_. And thus, the _LEVEL_ register must remain in its current position, _(0,1,0,0)_. So it does not need to be rotated.
   - Subcase 2.2: Otherwise, the second least-significant bit of the leaf level is _1_, which means the leaf level in its binary form ends with a _11_. Hence, leaf level is a number of the form _3 + 4k_, for some positive integer _k_. Consequently, the _LEVEL_ register needs to be rotated from the current position _(0,1,0,0)_ to the position _(0,0,0,1)_.

2. Using LEVEL to "climb the RKey"

   The Remaining Key is fetched using the _GetRKey()_ function and stored in the _RKEY_ register.

   When climbing the tree, there are two functions that are used in the code: the CLIMB_RKEY and the ROTATE_LEVEL.

   - First, the _LEVEL_ register is used to pinpoint the correct part of the Remaining Key to which the path-bit last used in the navigation must be appended.
   - Second, the ROTATE_LEVEL is used to rotate the _LEVEL_ register once.  
   - The CLIMB_RKEY is used. Firstly, to shift the value of the pinpointed RKey part one position to the left. Secondly, to insert the last used path bit to the least-significant position of the shifted-value of the pinpointed RKey part.

The above two steps are repeated until all the path bits used in navigation have been appended. Later, equality between the reconstructed key and the original key is checked.

### Checking inclusion of old value in old root

The above key reconstruction, together with checking inclusion of the old value in the old root and updating the old value to the new value, are carried out simultaneously.

Since checking inclusion of the old value in the old root follows the same steps as the update of the old value to the new value, the corresponding lines in the Assembly code are similar. It suffices therefore to explain only one of these two computations.

Next is the discussion of the update of the old value to the new value.

### Update part of Set_UPDATE

All values, $\text{V}_{0123}=\big(\text{V}_{0},\text{V}_{1},\text{V}_{2},\text{V}_{3},\text{V}_{4},\text{V}_{5},\text{V}_{6},\text{V}_{7}\big)$ are 256-bit long and expressed as lower half and higher half as, _VALUE_LOW_ $=\big(\text{V}_{0},\text{V}_{1},\text{V}_{2},\text{V}_{3}\big)$ and _VALUE_HIGH_ $=\big(\text{V}_{4},\text{V}_{5},\text{V}_{6},\text{V}_{7} \big)$.

1. Computing the new leaf value

   1. The functions _GetValueLow()_ and _GetValueHigh()_ are used to fetch _VALUE_LOW_ $=\big(\text{V}_{0},\text{V}_{1},\text{V}_{2},\text{V}_{3}\big)$ and _VALUE_HIGH_ $=\big(\text{V}_{4},\text{V}_{5},\text{V}_{6},\text{V}_{7}\big)$, respectively.

   2. The _VALUE_LOW_ $= \big(\text{V}_{0},\text{V}_{1},\text{V}_{2},\text{V}_{3}\big)$ is stored in a register called _HASH_LEFT_, whilst _VALUE_HIGH_ $=\big(\text{V}_{4},\text{V}_{5},\text{V}_{6},\text{V}_{7}\big)$ is stored in another register called _HASH_RIGHT_.

   3. The hashed value of $\text{V}_{0123}$ is computed using _HASH0_ as, $\text{HASH0}\big(\text{HASH}\_ {\text{LEFT}}\|\text{HASH}\_ {\text{RIGHT}}\big)$. Note that this is in fact, $\text{POSEIDON}\big(0\|0\|0\|0\|\text{VALUE}\_ {\text{LOW}}\|\text{VALUE}\_ {\text{HIGH}}\big)$. The hashed value is then stored in _HASH_RIGHT_.

   !!!info
       This means the _HASH_RIGHT_ and the _HASH_LOW_ are 'make-shift' registers. Whenever a value is stored in it, the old value that was previously stored therein is simply pushed out. They hold values only for the next computation.

   4. Next the Rkey is copied into the _HASH_LEFT_ register. And the leaf value is computed by using _HASH1_ as, $\text{HASH1}\big(\text{HASH}\_ {\text{LEFT}}\|\text{HASH}\_ {\text{RIGHT}}\big)$. i.e., The value of the leaf is, $\text{HASH1}\big( \text{RKey}\|\text{HashedValue}\big)$. The leaf value is then copied into another register called _NEW_ROOT_.

2. Climbing the SMT

   Check if the path bit that led to the leaf is 0 or 1, by using the _GetNextKeyBit()_ function.

   Case 1: If the path bit (called 'key bit' in the code) is 0, then the corresponding sibling is on the right. Therefore, using 'jump if zero' _JMPZ_, the code jumps to the _SU_SiblingIsRight_ routine.

   - The leaf value in _NEW_ROOT_ is pushed into the _HASH_LEFT_ register.

   - The hash value of the sibling node is fetched, using the _GetSiblingHash()_ function. And it is pushed into the _HASH_RIGHT_ register.

   - The hash value of the parent node is computed using _HASH0_ as follows, $\text{HASH0}\big(\text{HASH}\_ {\text{LEFT}} \|\text{HASH}\_{\text{RIGHT}}\big)$.

   The parent node is $\text{POSEIDON}\big(0\|0\|0\|0\|\text{LeafValue}\|\text{SiblingHash}\big)$.

   Case 2: If the path bit is 1, then the corresponding sibling is on the left. The routine _SU_SiblingIsRight_ is then executed.

   - The leaf value in _NEW_ROOT_ is pushed into the _HASH_RIGHT_ register.

   - The hash value of the sibling node is fetched, using the _GetSiblingHash()_ function. And it is pushed into the _HASH_LEFT_ register.

   - The hash value of the parent node is computed using _HASH0_ as follows, $\text{HASH0}\big(\text{HASH}\_ {\text{LEFT}}\|\text{HASH}\_ \text{RIGHT}\big)$.

   The parent node is $\text{POSEIDON}\big(0\|0\|0\|0\|\text{SiblingHash}\|\text{LeafValue}\big)$.

3. Check if tree top has been reached

   The code uses the function _GetTopTree()_ to check is the top of the tree has been reached.

   Case 1. If _GetTopTree()_ returns 1, then Step 2 is repeated. But this time using the hash value of the corresponding sibling at the next level (at _leaf level - 1_).

   Case 2. If _GetTopTree()_ returns 0, then the code jumps to the _SU_Latch_ routine.

The _SU_Latch_ is an overall routine for the entire _Set_UPDATE_ Assembly code. It is here where,

- Equality between the reconstructed key and the original key is checked.

- Equality between the computed old root value and the original old root is checked.

Once consistency is established both between the keys and the old roots, then all new values; the new root, the new hash value, and the new leaf value are set using _LATCH_SET_.

## Remaining secondary assembly codes

The Assembly codes for the other seven SMT Actions to a certain extent follow a similar pattern except for a few cases where especially adjusted routines are used.

Actions such as:

1. The _Set_InsertFound_ (or _SIF_) may involve a change in the topology of the SMT by extending a branch once or several times.

   In cases where a branch has been extended, the SIF Assembly code, when computing the new root, uses another routine called _SIF_ClimbBranch_ just for updating values along the newly extended branch. This is done in addition to the _SIF_ClimbTree_, which is the exact same routine as the aforementioned _SU_ClimbTree_ of the _Set_UPDATE_ case.

   It is for the same reason that SIF Assembly utilizes special registers: the _SIBLING_VALUE_HASH_ and _SIBLING_RKEY_.

2. The opposite SMT Action, the _Set_DeleteFound_ or _SDF_, may entail a previously extended branch being reversed.

   As in the SIF case, if a branch had been extended but now the extension needs to be reversed due to a deleted leaf value, a special routine called _SDF_ClimbBranch_ is used when updating values of nodes along the newly shortened branch. This _SDF_ClimbBranch_ routine is the exact same routine as the _SIF_ClimbBranch_. Similarly, the SDF Assembly code uses the _SDF_ClimbTree_ as in the Set_UPDATE Assembly.

Note also that there is only one _Get_ Assembly code for the READ SMT Action, and the rest of the secondary Assembly codes are _Set_ Assembly codes differing according to their respective SMT Actions. So _Get_ uses _LATCH_GET_ at the end of a run, while the _Set_ codes use _LATCH_SET_.
