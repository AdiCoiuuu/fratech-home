"""Constants for the Fratech Home UI integration."""

from __future__ import annotations

DOMAIN = "fratech_home"
NAME = "Fratech Home"
VERSION = "1.2.0"

STATIC_URL = "/fratech_home_static"
FRONTEND_FILE = "fratech-home.js"
CONFIG_URL = "/api/fratech_home/config"

PANEL_URL = "fratech-home"
PANEL_ELEMENT = "fratech-home-panel"
PANEL_ICON = "mdi:home-lightning-bolt-outline"

DEFAULT_TITLE = "Zurli Family"
DEFAULT_SUBTITLE = "AdiHouse · Smart Home"
DEFAULT_SIDEBAR_TITLE = "Fratech Home"
DEFAULT_LANGUAGE = "ro"
DEFAULT_LOCAL_BACKGROUND_BASE = "/local/backgrounds"
DEFAULT_GREETING_NAME = "Adi"

DEFAULT_BACKGROUNDS: dict[str, str] = {
    "home": "casa.jpg",
    "garaj": "garaj.jpg",
    "curte": "curte.jpg",
    "hol_mare": "hol_mare.jpg",
    "hol_mic": "hol_mic.jpg",
    "bucatarie": "bucatarie.jpg",
    "dormitor_adi": "dormitor_adi.jpg",
    "dormitor_adina": "dormitor_adina.jpg",
    "dormitor_alexandra": "dormitor_alexandra.jpg",
}

ROOM_KEYS: tuple[str, ...] = tuple(key for key in DEFAULT_BACKGROUNDS if key != "home")

OVERRIDE_KEYS = {
    "rooms",
    "global",
    "labels",
    "remote_commands",
    "features",
    "clock",
    "greeting_name",
}
