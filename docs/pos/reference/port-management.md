This guide provides a detailed list of default ports used across Polygon nodes, including Bor and Heimdall. Understanding these ports is crucial for network configuration and effective communication between nodes.

## Bor node

| Name                    | Port  | Tags                      | Description                                                                                                    |
|-------------------------|-------|---------------------------|----------------------------------------------------------------------------------------------------------------|
| Network Listening Port  | 30303 | Public                    | Port used by Bor for peer connections and synchronization.                                                     |
| RPC Server              | 8545  | Can be Public, Internal   | RPC port for sending transactions and fetching data. Heimdall uses this port to obtain Bor headers.             |
| WebSocket Server        | 8546  | Can be Public, Internal   | WebSocket port for real-time updates.                                                                           |
| GraphQL Server          | 8547  | Internal                  | GraphQL port for querying data.                                                                                 |
| Prometheus Server       | 9091  | Can be Public, Monitoring | Prometheus APIs for Grafana data source. Can be mapped to ports 80/443 via an Nginx reverse proxy.              |
| Grafana Server          | 3001  | Can be Public, Monitoring | Grafana web server. Can be mapped to ports 80/443 via an Nginx reverse proxy.                                   |
| Pprof Server            | 7071  | Internal, Monitoring      | Pprof server for collecting Bor metrics.                                                                        |
| UDP Discovery           | 30301 | Can be Public, Internal   | Default port for Bootnode peer discovery.                                                                       |

## Heimdall node

| Name                    | Port  | Tags                      | Description                                                                                                    |
|-------------------------|-------|---------------------------|----------------------------------------------------------------------------------------------------------------|
| Network Listening Port  | 30303 | Public                    | Port used by Heimdall for peer connections and synchronization.                                                 |
| RPC Server              | 8545  | Can be Public, Internal   | RPC port for sending transactions and fetching data. Heimdall uses this port to obtain Bor headers.             |
| WebSocket Server        | 8546  | Can be Public, Internal   | WebSocket port for real-time updates.                                                                           |
| GraphQL Server          | 8547  | Internal                  | GraphQL port for querying data.                                                                                 |
| Prometheus Server       | 9091  | Can be Public, Monitoring | Prometheus APIs for Grafana data source. Can be mapped to ports 80/443 via an Nginx reverse proxy.              |
| Grafana Server          | 3001  | Can be Public, Monitoring | Grafana web server. Can be mapped to ports 80/443 via an Nginx reverse proxy.                                   |
| Pprof Server            | 7071  | Internal, Monitoring      | Pprof server for collecting Heimdall metrics.                                                                   |
| UDP Discovery           | 30301 | Can be Public, Internal   | Default port for Bootnode peer discovery.                                                                       |
