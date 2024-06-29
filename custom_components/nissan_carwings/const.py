"""Constants for nissan_carwings."""

from logging import Logger, getLogger

LOGGER: Logger = getLogger(__package__)

DOMAIN = "nissan_carwings"

PYCARWINGS_SLEEP = 25
PYCARWINGS_MAX_RESPONSE_ATTEMPTS = 10
PYCARWINGS3_BASE_URL = None  # use default BASE_URL

CONF_PYCARWINGS3_BASE_URL = "pycarwings3_base_url"

OPTIONS_UPDATE_INTERVAL = "update_interval"
DEFAULT_UPDATE_INTERVAL = 600

DATA_BATTERY_STATUS_KEY = "battery_status"
DATA_CLIMATE_STATUS_KEY = "climate_status"
DATA_DRIVING_ANALYSIS_KEY = "driving_analysis"
DATA_TIMESTAMP_KEY = "timestamp"
