# AIChatFlutter-Modernized
Мультиплатформенный AI-чат на Flet + Flutter — модернизированная версия neuro-fill/AIChatFlutter. 4 экрана: чат, настройка провайдера (OpenRouter / VSEGPT), статистика токенов и график расходов по дням. Работает на Android, iOS, Windows, Linux и Web.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![Flet](https://img.shields.io/badge/Flet-0.86+-00A98F?logo=flutter&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Android%20%7C%20iOS%20%7C%20Windows%20%7C%20Linux%20%7C%20Web-blue)
![License](https://img.shields.io/badge/License-MIT-green)

Мультиплатформенный AI-чат на **Flet + Flutter** — модернизированная версия
[neuro-fill/AIChatFlutter](https://github.com/neuro-fill/AIChatFlutter).

**4 экрана**: чат, настройка провайдера (OpenRouter / VSEGPT), статистика токенов
и график расходов по дням. Работает на Android, iOS, Windows, Linux и Web.

---

## Web-демо

[**Открыть в браузере**](https://banan41k78.github.io/AIChatFlutter-Modernized/)

Работает без установки — прямо в браузере.

---

## Скачать

| Платформа | Ссылка |
|---|---|
| Android | [APK](https://github.com/Banan41k78/AIChatFlutter-Modernized/releases/latest) |
| Windows | [ZIP](https://github.com/Banan41k78/AIChatFlutter-Modernized/releases/latest) |
| Web | [Открыть демо](https://banan41k78.github.io/AIChatFlutter-Modernized/) |

---

## Возможности

### Чат
- Обмен сообщениями с AI в реальном времени
- История диалога в рамках сессии
- Индикатор «печатает…»
- Автопрокрутка, адаптивная вёрстка

### Настройки
- Выбор провайдера: **OpenRouter** или **VSEGPT**
- Ввод API-ключа прямо в UI 
- Выбор модели из списка
- Свой System Prompt
- Сохранение в `data/settings.json`

### Статистика
- Запросы по каждой модели
- Токены на вход / выход
- Стоимость в долларах
- Итоговые карточки: всего токенов, всего потрачено

### График расходов
- Столбчатая диаграмма трат по дням
- Тултип с точным значением стоимости
- Данные из `data/stats.json`

### Интерфейс
- Тёмная тема (Material 3)
- Нижняя навигация — 4 вкладки
- Адаптивный дизайн (телефон / десктоп / браузер)

## Стек

| Слой | Технология |
|---|---|
| Язык | Python 3.10+ |
| UI | [Flet](https://flet.dev/) 0.86+ (Flutter runtime) |
| HTTP | httpx (async) |
| Хранилище | JSON (`data/settings.json`, `data/stats.json`) |
| Сборка | `flet build` (APK, Windows, Web, iOS) |

---

## Быстрый старт

```bash
git clone https://github.com/Banan41k78/AIChatFlutter-Modernized.git
cd AIChatFlutter-Modernized
pip install -r requirements.txt
flet run src/main.py
