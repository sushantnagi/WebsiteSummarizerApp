import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from scraper import Website

# ────── Load API Key from .env ──────
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("❌ GEMINI_API_KEY not found in .env file.")

# ────── Configure Gemini ──────
client = genai.Client(api_key=api_key)


# ────── Prompt Templates ──────
system_prompt = (
    "You are an assistant that analyzes the contents of a website "
    "and provides a short summary, ignoring text that might be navigation related. "
    "Respond in markdown."
)


# ────── Main Summary Function ──────
def summarize(url: str) -> str:
    website = Website(url)
    if website.error:
        return website.error

    prompt = (
        "You are an assistant that analyzes the contents of a website "
        "and provides a short summary, ignoring text that might be navigation related. "
        "Respond in markdown.\n\n"
        f"You are looking at a website titled: {website.title}\n\n"
        "The contents of this website are as follows:\n\n"
        f"{website.text}"
    )

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                thinking_config=types.ThinkingConfig(thinking_budget=0)
            )
        )
        return response.text.strip()

    except Exception as e:
        return f"❌ Gemini API Error: {str(e)}"


