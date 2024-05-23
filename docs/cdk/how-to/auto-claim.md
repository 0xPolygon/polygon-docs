### How to onboard a new CDK chain to the Unified Bridge API

***Expectations from a CDK chain team for onboarding them to the Portal UI and to spin up the Bridge API service for their chain is as follows :-*** 

- Public RPC
- Chain ID
- Chain Name
- Icon/Logo of the specific CDK chain
- Dedicated RPC ( This is really important and is expected at the early stages itself ) - This will be used by the indexer to index all the data from the specific CDK chain.
- Block Explorer URL
- Bridging Contracts Address

***Note: All of the above are mandatory expectations from any CDK team. Rest of the dependencies and services will be handled and deployed by the Polygon team in the initial phases.*** 


Note: In the initial stages, ***an IP for a CDK chain would be expected to only deploy the*** ***autoclaim script***. Instructions for deploying the autoclaim script will be shared in the next section. All other services mentioned above will be deployed by the Polygon Team. 

### How to run the Autoclaim Script ? [ For IP’s ]

The script will have the functionality to poll the Bridge API service endpoints to fetch the unprocessed claims and then submit the claimAsset transactions for all the unprocessed claims. The retry mechanisms and all error handling will be taken care by the script. 

The bridge API service which the script heavily depends up on will also be deployed by the Polygon team. The URL’s for the endpoints is all that will have to be set in the autoclaim script config before running the script. 

Autoclaim Serice Public Repo : https://github.com/0xPolygon/auto-claim-service

Following the [README.md](https://github.com/0xPolygon/auto-claim-service/blob/main/README.md) is recommended to understand how to deploy the autoclaim service for any given CDK chain which is a part of the unified lxly contract.