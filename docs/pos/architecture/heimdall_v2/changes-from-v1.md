

# Heimdall-v2 changes compared to v1

There are a number of differences between Heimdall v1 to v2. These changes are outlined below:

## Encoding changes to Base64

Data encoding format has been changed from Hex encoded to Base64 encoded, for example:

Hex encoded: `BJSk2KCI4snP2Cw/ntDdgp8R25XJ2xg18KL67fyEAwgtPMpeq5APSUHrkv5wtgrFfpmcDivnP8HPGufyyXnByxo=`

Base64 encoded: `0x0494a4d8a088e2c9cfd82c3f9ed0dd829f11db95c9db1835f0a2faedfc8403082d3cca5eab900f4941eb92fe70b60ac57e999c0e2be73fc1cf1ae7f2c979c1cb1a`

## Validator signing key
In Heimdall-v2, validator signing keys must be imported into the keyring for transaction signing. For details of keyring, refer to the Cosmos SDK documentation [here](https://docs.cosmos.network/v0.46/run-node/keyring.html)

From the Cosmos documentation:

>The keyring holds the private/public keypairs used to interact with a node. For instance, >a validator key needs to be set up before running the blockchain node, so that blocks can >be correctly signed. The private key can be stored in different locations, called >"backends", such as a file or the operating system's own key storage.

### How to use Keyring

Below are the instructions on how to import your validator private key into the keyring and use it to sign transactions.

Get your `base64` encoded private key from:

```cat /var/lib/heimdall/config/priv_validator_key.json```

Convert the `base64` encoded key to hex encoded key:

```echo "<PRIVATE_KEY_BASE64_ENCODED>" | base64 -d | xxd -p -c 256```

Import the `hex` encoded key to your keyring:

```heimdalld keys import-hex <KEY_NAME> <PRIVATE_KEY_HEX_ENCODED> --home <HOME_DIR_PATH>```

When you first import a key into the keyring, you will be prompted for a password, which will be used every time you sign a transaction.

When running a `tx` command, just specify the `--from` argument, by using the name of the key you have set above. Example:
```heimdalld tx gov vote 1 yes --from <KEY_NAME>```

## Vote extension in each block

In Heimdall-v2, the first transaction of each block will contain the encoded vote extensions. To decode these, use the additional command in `heimdallld`
