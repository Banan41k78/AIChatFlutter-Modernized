# Установка

## Требования

- **Python 3.10+**
- **pip**
- **Flet 0.86+**
- **Flutter SDK** — только для сборки (`flet build`), не для запуска

Проверка:

```bash
python --version
pip --version
```

---

## Установка

```bash
git clone https://github.com/Banan41k78/AIChatFlutter-Modernized.git
cd AIChatFlutter-Modernized

python -m venv .venv
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # macOS / Linux

pip install -r requirements.txt
```

Если `requirements.txt` нет:

```bash
pip install "flet==0.86.5" httpx
```

---

## Запуск

Из корня проекта:

```bash
flet run src/main.py
```

В браузере:

```bash
flet run --web src/main.py
```

---

## Первая настройка

1. Открой вкладку **Настройки**.
2. Выбери провайдера: **OpenRouter** или **VSEGPT**.
3. Вставь API-ключ:
   - OpenRouter → https://openrouter.ai/keys
   - VSEGPT → https://vsegpt.ru/
4. Выбери модель → **Сохранить**.

Перейди в **Чат** и отправь сообщение.

---

## Сборка

Нужен **Flutter SDK** в `PATH` (https://docs.flutter.dev/get-started/install).

```bash
flet build apk        # Android
flet build windows    # Windows
flet build web        # Web
flet build ipa        # iOS (только macOS)
```

Результат — в папке `build/`.

---

## Частые проблемы

| Ошибка | Решение |
|---|---|
| `flet: command not found` | `pip install flet` |
| `No module named 'httpx'` | `pip install httpx` |
| `Flutter not found` | Установи Flutter SDK, добавь `flutter/bin` в `PATH` |
| `Android SDK not found` | Установи Android Studio, выполни `flutter doctor --android-licenses` |
| `Visual Studio not found` (Windows) | Установи VS 2022 с компонентом **Desktop development with C++** |
| Ошибка `401` при запросе | Неверный API-ключ |
| Ошибка `402` | Закончился баланс на провайдере |

Полная диагностика:

```bash
flet doctor
```
