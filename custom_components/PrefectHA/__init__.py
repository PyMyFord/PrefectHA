"""Support for My Ford Mobile vehicles."""
import logging
from datetime import timedelta

import voluptuous as vol

from homeassistant.components.lock import DOMAIN as LOCK
from homeassistant.components.sensor import DOMAIN as SENSOR
from homeassistant.components.switch import DOMAIN as SWITCH
from homeassistant.const import (
    CONF_USERNAME,
    CONF_PASSWORD,
    CONF_SCAN_INTERVAL
)
from homeassistant.helpers import config_validation as cv
from homeassistant.helpers.discovery import load_platform
from homeassistant.helpers.dispatcher import dispatcher_send
from homeassistant.helpers.event import track_time_interval

DOMAIN = "prefect"
DATA_UPDATED = "{}_data_updated".format(DOMAIN)

_LOGGER = logging.getLogger(__name__)

SUPPORTED_PLATFORMS = [LOCK, SENSOR, SWITCH]

DEFAULT_INTERVAL = timedelta(days=7)

CONFIG_SCHEMA = vol.Schema(
    {
        DOMAIN: vol.Schema(
            {
                vol.Required(CONF_USERNAME): cv.string,
                vol.Required(CONF_PASSWORD): cv.string,
                vol.Optional(CONF_SCAN_INTERVAL, default=DEFAULT_INTERVAL): vol.All(
                    cv.time_period, cv.positive_timedelta
                ),
            }
        )
    },
    extra=vol.ALLOW_EXTRA,
)

def setup(hass, config):
    """Set up the Prefect component."""
    from prefect import FordAPI
    F = FordAPI()

    conf = config[DOMAIN]
    F.authenticate(conf.get(CONF_USERNAME), conf.get(CONF_PASSWORD))
    _LOGGER.debug("Successfully authenticated with prefect.")
