/* eslint-disable no-await-in-loop, no-use-before-define, no-lonely-if */
/* eslint-disable no-console, no-inner-declarations, no-undef, import/no-unresolved */
import path = require("path");

import * as dotenv from "dotenv";
dotenv.config({path: path.resolve(__dirname, "../../.env")});
import {ethers} from "hardhat";

const updateRollupOutput = require("./updateRollupOutput.json");
const addRollupParameters = require("./updateRollup.json");
import "../../deployment/helpers/utils";
import {PolygonZkEVMTimelock} from "../../typechain-types";

async function main() {
    const {target, value, data, predecessor, salt} = updateRollupOutput.decodedScheduleData;
    const {timelockAddress} = addRollupParameters;

    // Load provider
    let currentProvider = ethers.provider;
    if (updateRollupOutput.multiplierGas || updateRollupOutput.maxFeePerGas) {
        if (process.env.HARDHAT_NETWORK !== "hardhat") {
            currentProvider = ethers.getDefaultProvider(
                `https://${process.env.HARDHAT_NETWORK}.infura.io/v3/${process.env.INFURA_PROJECT_ID}`
            ) as any;
            if (updateRollupOutput.maxPriorityFeePerGas && updateRollupOutput.maxFeePerGas) {
                console.log(
                    `Hardcoded gas used: MaxPriority${updateRollupOutput.maxPriorityFeePerGas} gwei, MaxFee${updateRollupOutput.maxFeePerGas} gwei`
                );
                const FEE_DATA = new ethers.FeeData(
                    null,
                    ethers.parseUnits(updateRollupOutput.maxFeePerGas, "gwei"),
                    ethers.parseUnits(updateRollupOutput.maxPriorityFeePerGas, "gwei")
                );

                currentProvider.getFeeData = async () => FEE_DATA;
            } else {
                console.log("Multiplier gas used: ", updateRollupOutput.multiplierGas);
                async function overrideFeeData() {
                    const feedata = await ethers.provider.getFeeData();
                    return new ethers.FeeData(
                        null,
                        ((feedata.maxFeePerGas as bigint) * BigInt(updateRollupOutput.multiplierGas)) / 1000n,
                        ((feedata.maxPriorityFeePerGas as bigint) * BigInt(updateRollupOutput.multiplierGas)) / 1000n
                    );
                }
                currentProvider.getFeeData = overrideFeeData;
            }
        }
    }

    // Load deployer
    let deployer;
    if (updateRollupOutput.deployerPvtKey) {
        deployer = new ethers.Wallet(updateRollupOutput.deployerPvtKey, currentProvider);
    } else if (process.env.MNEMONIC) {
        deployer = ethers.HDNodeWallet.fromMnemonic(
            ethers.Mnemonic.fromPhrase(process.env.MNEMONIC),
            "m/44'/60'/0'/0/0"
        ).connect(currentProvider);
    } else {
        [deployer] = await ethers.getSigners();
    }

    console.log("Using with: ", deployer.address);

    // load timelock
    const timelockContractFactory = await ethers.getContractFactory("PolygonZkEVMTimelock", deployer);
    const timelock = (await timelockContractFactory.attach(
        timelockAddress
    )) as PolygonZkEVMTimelock;
    await timelock.execute(
        target,
        value,
        data,
        predecessor,
        salt,
    )
}

main().catch((e) => {
    console.error(e);
    process.exit(1);
});