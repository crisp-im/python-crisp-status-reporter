# python-crisp-status-reporter

[![Build and Release](https://github.com/crisp-im/python-crisp-status-reporter/workflows/Build%20and%20Release/badge.svg)](https://github.com/crisp-im/python-crisp-status-reporter/actions?query=workflow%3A%22Build+and+Release%22)

**Crisp Status Reporter for Python.**

Crisp Status Reporter is used to actively submit health information to Crisp Status from your apps. Apps are best monitored via application probes, which are able to report detailed system information such as CPU and RAM load. This lets Crisp Status show if an application host system is under high load.

## How to use?

### Create reporter

`crisp-status-reporter` can be instantiated as such:

```python
from crisp_status_reporter import Reporter
import logging as logger

# Build and run reporter
Reporter(
  token = "YOUR_TOKEN_SECRET",
  service_id = "d657b4c1-dd07-4f94-ac7a-d4c3b4b219c1",
  node_id = "5eca824b-4134-4126-982d-2c2338ecf3ab",
  replica_id = "192.168.1.10",
  interval = 60,
  logger = logger
)
```

## Where can I find my token?

Your private token can be found on your [Crisp dashboard](https://app.crisp.chat/). Go to Settings, then Status Page, and then scroll down to "Configure your Status Reporter". Copy the secret token shown there, and use it while configuring this library in your application.

## How to add monitored node?

You can easily add a push node for the application running this library on your Crisp dashboard. Add the node, and retrieve its `service_id` and `node_id` as follows:

<p align="center">
  <img width="605" src="https://crisp-im.github.io/python-crisp-status-reporter/images/setup.gif" alt="How to add monitored node">
</p>

## Get more help

You can find more help on our helpdesk article: [How to setup the Crisp Status Reporter library?](https://help.crisp.chat/en/article/1koqk09/)

