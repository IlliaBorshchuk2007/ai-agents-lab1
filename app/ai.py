
import os
import json
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def extract_video(text):
    prompt = f"""
Витягни інформацію про навчальне відео з тексту.

Потрібні поля:
- title: назва відео
- topic: тема відео
- duration_minutes: тривалість у хвилинах

Правила:
1. Усі три поля обов'язкові.
2. Не вигадуй відсутню інформацію.
3. Назва не повинна починатися зі слів "Відео" або "Урок".
4. Тривалість має бути додатним цілим числом.
5. Якщо інформації недостатньо, поверни null.
6. Поверни лише JSON без пояснень.

Текст: {text}
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    content = response.choices[0].message.content.strip()

    try:
        result = json.loads(content)
    except (json.JSONDecodeError, TypeError):
        return None

    if not isinstance(result, dict):
        return None

    title = result.get("title")
    topic = result.get("topic")
    duration = result.get("duration_minutes")

    if not isinstance(title, str) or not title.strip():
        return None

    if not isinstance(topic, str) or not topic.strip():
        return None

    if type(duration) is not int or duration <= 0:
        return None

    return {
        "title": title.strip(),
        "topic": topic.strip(),
        "duration_minutes": duration
    }
