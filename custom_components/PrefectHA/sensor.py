import logging

import voluptuous as vol
from homeassistant.components.sensor import PLATFORM_SCHEMA
from homeassistant.const import CONF_REGION

from . import DOMAIN

_LOGGER = logging.getLogger(__name__)