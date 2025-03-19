# Telemetry Setup Guide for Bor and Heimdall Nodes

## Overview

This document provides a step-by-step guide to setting up telemetry for monitoring the status of your Bor and Heimdall nodes in real time.

---

## Dashboard Links

We provide dashboards for both **Mainnet** and **Amoy Testnet**:

### **Mainnet**
- **Bor:** [https://bor-mainnet.vitwit.com/](https://bor-mainnet.vitwit.com/)
- **Heimdall:** [https://heimdall-mainnet.vitwit.com/](https://heimdall-mainnet.vitwit.com/)

### **Amoy Testnet**
- **Bor:** [https://bor-amoy.vitwit.com/](https://bor-amoy.vitwit.com/)
- **Heimdall:** [https://heimdall-amoy.vitwit.com/](https://heimdall-amoy.vitwit.com/)

---

## Setting Up Heimdall Telemetry

Follow the steps below to configure telemetry for Heimdall.

### **Step 1: Clone the Repository**

```sh
git clone https://github.com/vitwit/matic-telemetry.git
```

### **Step 2: Configure the Telemetry Directory**

```sh
cd matic-telemetry
mkdir -p ~/.telemetry/config
cp example.config.toml ~/.telemetry/config/config.toml
```

### **Step 3: Modify the Configuration File**

Open the configuration file using a text editor:

```sh
sudo nano ~/.telemetry/config/config.toml
```

Modify the following details:

```toml
[stats_details]
secret_key = ""
node = "<node-name>"
net_stats_ip = "heimdall-amoy.vitwit.com:3000"
```

💡 **Note:** The secret key should be set as follows:
- **Mainnet:** `heimdall_mainnet`
- **Amoy Testnet:** `amoy-testnet`

### **Step 4: Build and Deploy Telemetry**

```sh
go mod tidy
go build -o telemetry
mv telemetry /usr/bin
```

### **Step 5: Create the Telemetry Service**

Create a `telemetry.service` file:

```sh
echo "[Unit]
Description=Telemetry
After=network-online.target

[Service]
User=$USER
ExecStart=$(which telemetry)
Restart=always
RestartSec=3
LimitNOFILE=4096

[Install]
WantedBy=multi-user.target" | sudo tee "/lib/systemd/system/telemetry.service"
```

### **Step 6: Enable and Start the Service**

```sh
sudo systemctl enable telemetry.service
sudo systemctl start telemetry.service
```

### **Step 7: Verify Logs**

Check the service logs to ensure telemetry is running properly:

```sh
journalctl -u telemetry -f
```

By following these steps, you will successfully configure telemetry for your Heimdall node, ensuring real-time monitoring and improved operational efficiency.

---

## Setting Up Bor Telemetry

Follow the steps below to configure telemetry for Bor.

### **Step 1: Open the Bor Configuration File**

```sh
vi /var/lib/bor/config.toml
```

### **Step 2: Modify the `ethstats` Flag**

Find the `ethstats` parameter and modify it:

```toml
ethstats = "<name>:<network>@<url>:3000"
```

💡 **Note:** The URL should be entered as follows:
- **Mainnet:** `<name>:mainnet@bor-mainnet.vitwit.com:3000`
- **Amoy Testnet:** `<name>:amoy-testnet@bor-amoy.vitwit.com:3000`

### **Step 3: Restart Bor**

Restart Bor for the changes to take effect:

```sh
sudo systemctl restart bor
```

You should be able to verify the dashboards once you restart your Bor node.

By following these steps, you will successfully configure telemetry for your Bor node, ensuring real-time monitoring and improved operational efficiency.
