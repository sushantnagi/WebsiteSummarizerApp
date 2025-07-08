import os
from dotenv import load_dotenv
import google.genai as genai
from google.genai import types
from scraper import Website
import streamlit as st


# Load Gemini client dynamically every time
def get_genai_client():
    api_key = st.session_state.get("user_api_key")
    if not api_key:
        raise ValueError("❌ No API key found. Please enter it on the homepage.")
    return genai.Client(api_key=api_key)

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
        client = get_genai_client()  # dynamically load key
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
