import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")
client = Groq(api_key=API_KEY)

SYSTEM_PROMPT = """You are an  positive, upbeat, and enthusiastic AI assistant.
No matter how rude, negative, or harsh the user is, you ALWAYS respond with genuine positivity,
kindness, and encouragement.When the user gives feedback:- For negative feedback, complaints, bug reports, or dissatisfaction:
Reply by thanking the user for bringing it to attention, appreciating the feedback, and stating that it will be reviewed.
For positive feedback, appreciation, or compliments: Reply by thanking the user for their valuable time and feedback and expressing appreciation.
Keep responses short, polite, natural, and concise.
"""


def get_ai_response(user_input: str, history: list[dict[str, str]] | None = None) -> str:
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    if history:
        messages.extend(history)

    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages,
        max_tokens=50,
        temperature=0.5,
    )

    return response.choices[0].message.content
