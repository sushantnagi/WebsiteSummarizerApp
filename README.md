# 🧠 Website Summarizer App

[Run on StreamLit](https://websitesummarizer-gemini.streamlit.app/)

This is a simple Streamlit web app that scrapes content from any public webpage and uses Google's Gemini AI to generate a short, clean summary — skipping menus, navigation, and boilerplate.

Built just for fun by [Sushant Nagi](https://instagram.com/sushant_nagi) 😄

---
## 🔄 Update 1.0

- 🔐 Added user input for **Gemini API key** (no longer hardcoded or stored in `.env`)
- 🧠 API key now stored using `st.session_state` — per-user, per-session memory
- 💡 This makes the app safe for **Streamlit Cloud deployment**
- 🧪 `.env`-based fallback removed for simplicity

## 🚀 Features

- 🌐 Enter any website URL
- 🔹 Fixes the URL (Adds https://)
- 🧽 Cleans out unwanted tags (scripts, ads, navbars)
- 🤖 Uses Gemini 2.5 Flash (free-tier friendly) to generate summaries
- 📄 Outputs summaries in Markdown format
- 📬 About page with contact info and AI-generated creator photo

---

## 🛠️ Tech Stack

- [Python 3.12](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- [Google GenAI SDK](https://ai.google.dev/)
- [dotenv](https://pypi.org/project/python-dotenv/)

---

## ▶️ Run the App

```bash
streamlit run app.py
```

Then open `http://localhost:8501` in your browser.

---

## 📬 Contact

- 📧 [sushantnagi667@gmail.com](mailto:sushantnagi667@gmail.com)
- 💼 [LinkedIn](https://linkedin.com/in/sushant_nagi)
- 🐱 [GitHub](https://github.com/sushant_nagi)
- 📸 [Instagram](https://instagram.com/sushant_nagi)

---

## ⚠️ Disclaimer

This is a personal project built for learning and fun.  
The summary quality may vary depending on the structure and content of the target website.  
Free API limits from Google Gemini may affect availability.

---

