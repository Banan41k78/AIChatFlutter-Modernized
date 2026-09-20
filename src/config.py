# src/config.py

PROVIDERS = {
    "openrouter": {
        "name": "OpenRouter",
        "url": "https://openrouter.ai/api/v1/chat/completions",
        "models": [
            "openai/gpt-4o-mini",
            "openai/gpt-4o",
            "anthropic/claude-3.5-sonnet",
            "google/gemini-flash-1.5",
        ],
    },
    "vsegpt": {
        "name": "VSEGPT",
        "url": "https://api.vsegpt.ru/v1/chat/completions",
        "models": [
            "openai/gpt-4o-mini",
            "anthropic/claude-3-haiku",
            "google/gemini-flash-1.5",
        ],
    },
}

# Ориентировочные цены за 1M токенов, $
PRICES = {
    "openai/gpt-4o-mini":         {"in": 0.15,  "out": 0.60},
    "openai/gpt-4o":              {"in": 2.50,  "out": 10.00},
    "anthropic/claude-3.5-sonnet":{"in": 3.00,  "out": 15.00},
    "anthropic/claude-3-haiku":   {"in": 0.25,  "out": 1.25},
    "google/gemini-flash-1.5":    {"in": 0.075, "out": 0.30},
}

DEFAULT_SYSTEM_PROMPT = "Ты полезный ассистент."


def get_price(model: str) -> dict:
    return PRICES.get(model, {"in": 0.0, "out": 0.0})