# 🧠 Website Summarizer App

[Run on StreamLit](https://websitesummarizer-gemini.streamlit.app/)

This is a simple Streamlit web app that scrapes content from any public webpage and uses Google's Gemini AI to generate a short, clean summary — skipping menus, navigation, and boilerplate.

Built just for fun by [Sushant Nagi](https://instagram.com/sushant_nagi) 😄

---

## 🚀 Features

- 🌐 Enter any website URL
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

## 🧪 Installation

1. Clone the repo:

```bash
git clone https://github.com/yourusername/website-summarizer-app.git
cd website-summarizer-app
```

2. (Optional) Create a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Add your Gemini API key to a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

Then open `http://localhost:8501` in your browser.

---

## 📸 Screenshot

![screenshot](preview.png)

---

## 🧠 Quote at the Footer

> *"Finally, brethren, whatsoever things are true..."*  
> — Philippians 4:8

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

## ✨ License

MIT — use freely, learn endlessly.