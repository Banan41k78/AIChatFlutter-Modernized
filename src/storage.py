# src/storage.py
import json
from pathlib import Path
from datetime import datetime

from config import DEFAULT_SYSTEM_PROMPT

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

SETTINGS_FILE = DATA_DIR / "settings.json"
STATS_FILE = DATA_DIR / "stats.json"

DEFAULT_SETTINGS = {
    "provider": "openrouter",
    "api_key": "",
    "model": "openai/gpt-4o-mini",
    "system_prompt": DEFAULT_SYSTEM_PROMPT,
}


def load_settings() -> dict:
    if SETTINGS_FILE.exists():
        try:
            data = json.loads(SETTINGS_FILE.read_text("utf-8"))
            return {**DEFAULT_SETTINGS, **data}
        except Exception:
            pass
    return DEFAULT_SETTINGS.copy()


def save_settings(settings: dict) -> None:
    SETTINGS_FILE.write_text(
        json.dumps(settings, ensure_ascii=False, indent=2), "utf-8"
    )


def load_stats() -> list:
    if STATS_FILE.exists():
        try:
            return json.loads(STATS_FILE.read_text("utf-8"))
        except Exception:
            pass
    return []


def save_stats(stats: list) -> None:
    STATS_FILE.write_text(
        json.dumps(stats, ensure_ascii=False, indent=2), "utf-8"
    )


def add_stat(model: str, tokens_in: int, tokens_out: int, cost: float) -> None:
    stats = load_stats()
    stats.append({
        "date": datetime.now().isoformat(timespec="seconds"),
        "model": model,
        "tokens_in": tokens_in,
        "tokens_out": tokens_out,
        "cost": cost,
    })
    save_stats(stats)