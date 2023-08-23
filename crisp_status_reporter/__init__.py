##
# python-crisp-status-reporter
#
# Copyright 2023, Valerian Saliou
# Author: Valerian Saliou <valerian@valeriansaliou.name>
##

import json
import base64
import time
import urllib.error
import urllib.request

from threading import Thread

REPORT_URL = "https://report.crisp.watch/v1"
REPORT_ACCEPT = "application/json"
REPORT_USERAGENT = "python-crisp-status-reporter/1.0.0"
REPORT_INITIAL_DELAY = 10
REPORT_INTERVAL_DEFAULT = 30

class Reporter:
  def __init__(
    self, token, service_id, node_id, replica_id, interval=None, logger=None
  ):
    # Read configuration
    self.__token = token or None
    self.__service_id = service_id or None
    self.__node_id = node_id or None
    self.__replica_id = replica_id or None
    self.__interval = interval or REPORT_INTERVAL_DEFAULT
    self.__logger = logger or None

    # Validate environment variables
    assert self.__token, "crisp status token is required"
    assert self.__service_id, "crisp status service identifier is required"
    assert self.__node_id, "crisp status node identifier is required"
    assert self.__replica_id, "crisp status replica identifier is required"

    # Configure reporter
    self.__configure_reporter()

    # Spawn status reporter
    self.__reporter = self.__spawn_reporter()

  def __configure_reporter(self):
    # Compute authorization bytes
    authorization_bytes = base64.b64encode(
      (":" + self.__token).encode("ascii")
    )

    # Build report attributes
    self.__report_url = "{endpoint}/report/{service}/{node}/".format(
      endpoint = REPORT_URL,
      service = self.__service_id,
      node = self.__node_id
    )

    self.__report_headers = {
      "Accept": REPORT_ACCEPT,
      "Content-Type": REPORT_ACCEPT,
      "User-Agent": REPORT_USERAGENT,

      "Authorization": "Basic {authorization}".format(
        authorization = authorization_bytes.decode("ascii")
      )
    }

  def __spawn_reporter(self):
    task = Thread(
      target=self.__run_reporter,
      daemon=True,
      name="Crisp Status Reporter"
    )

    task.start()

    return task

  def __run_reporter(self):
    self.__log_debug("(status) Status reporter background task running")

    # Wait before sending first report
    time.sleep(REPORT_INITIAL_DELAY)

    # Start reporter infinite loop
    while True:
      self.__log_debug("(status) Will trigger a reporter tick")

      # Run reporter tick (1st attempt)
      if self.__tick_reporter(1) == False:
        self.__log_warning("(status) Reporter tick failed, will try again")

        # Try reporting again after half the interval (after failure)
        time.sleep(self.__interval / 2)

        # Run reporter tick (2nd attempt, and last one)
        if self.__tick_reporter(2) == False:
          self.__log_error("(status) All reporter tick attempts failed")

      # Hold on before sending next report
      time.sleep(self.__interval)

      continue

  def __tick_reporter(self, attempt=1):
    self.__log_debug("(status) Running reporter tick attempt #%d", attempt)

    # Build reporter data
    data = {
      "replica_id": self.__replica_id,
      "interval": self.__interval
    }

    # Open reporter request
    request = urllib.request.Request(
      self.__report_url,

      method="POST",
      headers=self.__report_headers,
      data=json.dumps(data).encode()
    )

    try:
      with urllib.request.urlopen(request) as response:
        # Response is success?
        if response.status == 200:
          self.__log_debug("(status) Reporter request got success status")

          # Report succeeded (cut short)
          return True

        self.__log_warning(
          "(status) Reporter request got error status: HTTP %d",
          response.status
        )

    except urllib.error.HTTPError as error:
      self.__log_warning("(status) Reporter request failure: %s", error)

    # Report failed (default outcome)
    return False

    def __log_debug(self, *args):
      if self.__logger is not None:
        self.__logger.debug(*args)

    def __log_warning(self, *args):
      if self.__logger is not None:
        self.__logger.warning(*args)

    def __log_error(self, *args):
      if self.__logger is not None:
        self.__logger.error(*args)
