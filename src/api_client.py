# src/api_client.py
import httpx

from config import PROVIDERS, get_price
from storage import add_stat


class AIClient:
    def __init__(self, settings: dict):
        self.provider = settings["provider"]
        self.api_key = settings["api_key"]
        self.model = settings["model"]
        self.system_prompt = settings.get("system_prompt", "Ты полезный ассистент.")
        self.history = [{"role": "system", "content": self.system_prompt}]

    def _url(self) -> str:
        return PROVIDERS[self.provider]["url"]

    async def send(self, user_message: str) -> str:
        self.history.append({"role": "user", "content": user_message})

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://github.com/neuro-fill/AIChatFlutter",
            "X-Title": "AIChatFlutter",
        }
        payload = {
            "model": self.model,
            "messages": self.history,
            "usage": {"include": True},
        }

        async with httpx.AsyncClient(timeout=60) as client:
            r = await client.post(self._url(), headers=headers, json=payload)
            r.raise_for_status()
            data = r.json()

        reply = data["choices"][0]["message"]["content"]
        self.history.append({"role": "assistant", "content": reply})

        # Запись статистики
        usage = data.get("usage") or {}
        tokens_in = usage.get("prompt_tokens", 0)
        tokens_out = usage.get("completion_tokens", 0)
        price = get_price(self.model)
        cost = tokens_in / 1_000_000 * price["in"] + tokens_out / 1_000_000 * price["out"]
        add_stat(self.model, tokens_in, tokens_out, cost)

        return reply