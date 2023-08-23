##
# python-crisp-status-reporter
#
# Copyright 2023, Valerian Saliou
# Author: Valerian Saliou <valerian@valeriansaliou.name>
##

import logging as logger

from crisp_status_reporter import Reporter

Reporter(
  token = "YOUR_TOKEN_SECRET",
  service_id = "d657b4c1-dd07-4f94-ac7a-d4c3b4b219c1",
  node_id = "5eca824b-4134-4126-982d-2c2338ecf3ab",
  replica_id = "192.168.1.10",
  interval = 60,
  logger = logger
)
