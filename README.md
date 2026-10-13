
# AI Agents Lab 1 — Каталог навчальних відео

## Опис проєкту
Цей проєкт реалізує HTTP API для каталогу навчальних відео з використанням FastAPI та LLM.

Користувач може додавати відео вручну або створювати запис за допомогою штучного інтелекту з текстового опису.

## Структура проєкту
- `app/main.py` — HTTP API на FastAPI.
- `app/ai.py` — отримання даних за допомогою LLM.
- `notebooks/01_experiment.ipynb` — експеримент із rule-based та LLM.
- `notebooks/02_api_verification.ipynb` — перевірка API.
- `tests/test_api.py` — автоматичні тести.
- `specs/` — специфікація, план і завдання.

## Поля відео
- `title` — назва відео.
- `topic` — тема.
- `duration_minutes` — тривалість у хвилинах (додатне ціле число).

## Запуск проєкту

Встановити залежності:

```bash
python -m pip install fastapi uvicorn groq python-dotenv pytest httpx requests
```

Створити файл `.env` та додати власний API-ключ:

```env
GROQ_API_KEY=your_api_key_here
```

Запустити сервер:

```bash
python -m uvicorn app.main:app --reload
```

Відкрити документацію API:

http://127.0.0.1:8000/docs

## HTTP API
- `GET /videos` — отримати список відео.
- `POST /videos` — додати відео вручну.
- `POST /videos/ai` — створити відео з текстового опису за допомогою LLM.

Якщо інформації недостатньо або вона некоректна, API повертає помилку `422`.

## Тестування

```bash
python -m pytest tests/test_api.py -v
```

Результат останнього запуску: 6 тестів пройдено.

## Висновок
У роботі реалізовано каталог навчальних відео, проведено експеримент із витягування даних, створено HTTP API та перевірено його роботу автоматичними тестами й Jupyter Notebook.
