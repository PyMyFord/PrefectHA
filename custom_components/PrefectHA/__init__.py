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

DOMAIN = "ford_prefect"
#DATA_UPDATED = "{}_data_updated".format(DOMAIN)

_LOGGER = logging.getLogger(__name__)

SUPPORTED_PLATFORMS = [SENSOR]

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
    from prefect import FordAPI
    """Set up the Prefect component."""
    conf = config[DOMAIN]
    F = FordAPI()
    F.authenticate(conf[CONF_USERNAME], conf[CONF_PASSWORD])
    _LOGGER.debug("Successfully authenticated with prefect.")
    return true

class FordPrefectData:
    def __init__(self, *args, **kwargs):
        self.__hass = hass
        self.vehicles = []
    def update(self, now, **kwargs):
        from prefect import FordAPI
