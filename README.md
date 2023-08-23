# python-crisp-status-reporter

[![Test and Build](https://github.com/crisp-im/python-crisp-status-reporter/workflows/Test%20and%20Build/badge.svg?branch=master)](https://github.com/crisp-im/python-crisp-status-reporter/actions?query=workflow%3A%22Test+and+Build%22)

**Crisp Status Reporter for Python.**

Crisp Status Reporter is used to actively submit health information to Crisp Status from your apps. Apps are best monitored via application probes, which are able to report detailed system information such as CPU and RAM load. This lets Crisp Status show if an application host system is under high load.

## How to use?

### Create reporter

`crisp-status-reporter` can be instantiated as such:

```python
# TODO
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

