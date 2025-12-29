# -*- coding: utf-8 -*-
import streamlit as st
import google.generativeai as genai

# 1. Page Config
st.set_page_config(page_title="AI Tutor", page_icon="🎓")
st.title("🎓 AI Tutor for Freshers")

# 2. Get API Key safely from Streamlit Secrets
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
except Exception:
    st.error("Please set GEMINI_API_KEY in Streamlit Secrets.")
    st.stop()

# 3. System Prompt
SYSTEM_PROMPT = (
    "You are an AI tutor for freshers. "
    "Explain concepts step-by-step using simple language and examples."
)

# 4. Initialize Model
model = genai.GenerativeModel(
    model_name="gemini-pro",
    system_instruction=SYSTEM_PROMPT
)

# 5. Initialize Chat History
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

# 6. Display chat history
for msg in st.session_state.chat.history:
    role = "user" if msg.role == "user" else "assistant"
    with st.chat_message(role):
        st.markdown(msg.parts[0].text)

# 7. Chat Input
if prompt := st.chat_input("Ask me anything about coding..."):
    with st.chat_message("user"):
        st.markdown(prompt)

    response = st.session_state.chat.send_message(prompt)

    with st.chat_message("assistant"):
        st.markdown(response.text)
