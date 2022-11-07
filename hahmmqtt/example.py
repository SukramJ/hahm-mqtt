# !/usr/bin/python3
""" Example used for hahm-mqtt. """
from __future__ import annotations

import asyncio
import logging
import sys
import time

from hahmmqtt.control_unit import ControlConfig


logging.basicConfig(level=logging.DEBUG)
_LOGGER = logging.getLogger(__name__)

entry_id = "1234567890"
default_callback_port = 56345
config_data = {
    "instance_name": "xxx",
    "host": "xxx",
    "username": "xxx",
    "password": "xxx",
    "tls": False,
    "verify_tls": False,
    "callback_host": None,
    "callback_port": None,
    "json_port": None,
    "interface": {
        "HmIP-RF": {
            "port": 2010
        },
        "BidCos-RF": {
            "port": 2001
        }
    }
}


class Example:
    # Create a server that listens on 127.0.0.1:* and identifies itself as myserver.

    def __init__(self):
        ...

    async def run(self):
        """..."""
        control = await ControlConfig(
            entry_id=entry_id,
            data=config_data,
            default_port=default_callback_port,
        ).async_get_control_unit()
        await control.async_start_central()

        for i in range(100):
            _LOGGER.debug("Sleeping (%i)", i)
            await asyncio.sleep(60)
        # Stop the central_1 thread so Python can exit properly.
        await control.async_stop_central()


example = Example()
asyncio.run(example.run())
sys.exit(0)
