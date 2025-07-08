import streamlit as st

st.set_page_config(
    page_title="Website Summarizer",
    page_icon="🧠",
    layout="wide"
)
# Custom styling for layout and image size
st.markdown("""
    <style>
        .container {
            display: flex;
            align-items: flex-start;
        }
        .form-area {
            flex: 1;
        }
    </style>
""", unsafe_allow_html=True)


st.markdown('<h1>🧠 Website Summarizer</h1>', unsafe_allow_html=True)

# Layout starts
st.markdown('<div class="container">', unsafe_allow_html=True)

# Image container with scaled-down size
st.image("anime-welcome.gif", width=240, use_container_width=False)

# Text and form section
st.markdown('<div class="form-area">', unsafe_allow_html=True)
st.markdown("### Welcome!")
st.markdown(
    "Enter the URL of the website you'd like to summarize. "
    "Our AI will extract the content and provide a clear, concise summary."
)

with st.form("url_input_form"):
    user_url = st.text_input("🔗 Website URL", placeholder="e.g. www.example.com")
    submit = st.form_submit_button("Summarize")

if submit:
    if not user_url:
        st.error("Please enter a valid URL.")
    else:
        with st.spinner("🔍 Scraping and summarizing the website..."):
            from gemini import summarize  # ✅ new function name

            summary = summarize(user_url)  # ✅ pass raw URL directly
            if summary.startswith("❌") or summary.startswith("⚠️"):
                st.error(summary)  # Show error from scraper or Gemini
            else:
                st.success("✅ Summary generated!")
                st.markdown("### 🔎 Summary:")
                st.markdown(summary, unsafe_allow_html=True)  # markdown output

st.markdown("---")
st.markdown(
    "**Note:** This tool uses a free tier of the Gemini API. "
    "If it fails to respond or throws an error, it's likely due to temporary rate limits or quota exhaustion. "
    "Try again after a few minutes."
)

st.markdown('</div>', unsafe_allow_html=True)  # Close form-area
st.markdown('</div>', unsafe_allow_html=True)  # Close container
