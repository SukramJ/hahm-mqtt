""" Constants used by hahm-mqtt. """
from __future__ import annotations

from datetime import timedelta

from hahomematic.const import AVAILABLE_HM_PLATFORMS
from hahomematic.backport import StrEnum

DOMAIN = "hahm-mqtt"
MANUFACTURER_EQ3 = "eQ-3"
HMIP_LOCAL_MIN_VERSION = "2022.11"
IDENTIFIER_SEPARATOR = "@"

ATTR_INSTANCE_NAME = "instance_name"
ATTR_INTERFACE = "interface"
ATTR_PATH = "path"

EVENT_DEVICE_AVAILABILITY = "homematic.device_availability"
EVENT_DEVICE_TYPE = "device_type"
EVENT_DATA_IDENTIFIER = "identifier"
EVENT_DATA_TITLE = "title"
EVENT_DATA_MESSAGE = "message"
EVENT_DATA_UNAVAILABLE = "unavailable"

SYSVAR_SCAN_INTERVAL = timedelta(seconds=30)
# only used for entities from MASTER paramset
MASTER_SCAN_INTERVAL = timedelta(seconds=300)


class Platform(StrEnum):
    """Available entity platforms."""

    AIR_QUALITY = "air_quality"
    ALARM_CONTROL_PANEL = "alarm_control_panel"
    BINARY_SENSOR = "binary_sensor"
    BUTTON = "button"
    CALENDAR = "calendar"
    CAMERA = "camera"
    CLIMATE = "climate"
    COVER = "cover"
    DEVICE_TRACKER = "device_tracker"
    FAN = "fan"
    GEO_LOCATION = "geo_location"
    HUMIDIFIER = "humidifier"
    IMAGE_PROCESSING = "image_processing"
    LIGHT = "light"
    LOCK = "lock"
    MAILBOX = "mailbox"
    MEDIA_PLAYER = "media_player"
    NOTIFY = "notify"
    NUMBER = "number"
    REMOTE = "remote"
    SCENE = "scene"
    SELECT = "select"
    SENSOR = "sensor"
    SIREN = "siren"
    STT = "stt"
    SWITCH = "switch"
    TTS = "tts"
    VACUUM = "vacuum"
    UPDATE = "update"
    WATER_HEATER = "water_heater"
    WEATHER = "weather"


def _get_hmip_local_platforms() -> list[str]:
    """Return relevant hahm-mqtt platforms."""
    platforms = [entry.value for entry in Platform]
    hm_platforms = [entry.value for entry in AVAILABLE_HM_PLATFORMS]
    hmip_local_platforms: list[str] = []
    for hm_platform in hm_platforms:
        if hm_platform in platforms:
            hmip_local_platforms.append(hm_platform)

    return hmip_local_platforms


HMIP_LOCAL_PLATFORMS: list[str] = _get_hmip_local_platforms()