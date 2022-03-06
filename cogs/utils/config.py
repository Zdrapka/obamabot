import json

with open("cogs/utils/config.json", encoding="utf-8") as f:
    _config = json.load(f)

CONFIG = _config
