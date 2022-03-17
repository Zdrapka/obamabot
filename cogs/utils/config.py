import json
from typing import Any

with open("cogs/utils/config.json", encoding="utf-8") as f:
    _cfg = json.load(f)

# fmt: off
ALL: dict[str, Any] = _cfg

IS_PRODUCTION : bool           = _cfg["is_production"]
PREFIX        : str            = _cfg["default"]["prefix"]
EMB_COLOR     : str            = _cfg["default"]["embed_color"]
POSTGRES_CREDS: dict[str, str] = _cfg["postgres"]
DEBUG_GUILD   : int            = _cfg["debug_guild"]

TOKEN: str = (
    _cfg["token"]["production"]
    if IS_PRODUCTION
    else _cfg["token"]["development"]
)
