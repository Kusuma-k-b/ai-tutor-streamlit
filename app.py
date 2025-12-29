import streamlit as st
import google.generativeai as genai

# -------------------------------
# 1. Page Configuration
# -------------------------------
st.set_page_config(
    page_title="🎓 AI Tutor for Freshers",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 AI Tutor for Freshers")
st.caption("Ask anything about Python, SQL, DSA, ML, or coding basics")

# -------------------------------
# 2. Configure Gemini API Key
# -------------------------------
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
except Exception:
    st.error("❌ GEMINI_API_KEY not found. Please add it in Streamlit Secrets.")
    st.stop()

# -------------------------------
# 3. System Prompt
# -------------------------------
SYSTEM_PROMPT = (
    "You are an AI tutor for freshers. "
    "Explain concepts step-by-step using very simple language, "
    "real-world examples, and short code snippets when helpful."
)

# -------------------------------
# 4. Initialize Gemini Model
# -------------------------------
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash-latest",
    system_instruction=SYSTEM_PROMPT
)

# -------------------------------
# 5. Initialize Chat Memory
# -------------------------------
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

# -------------------------------
# 6. Display Chat History
# -------------------------------
for msg in st.session_state.chat.history:
    role = "user" if msg.role == "user" else "assistant"
    with st.chat_message(role):
        st.markdown(msg.parts[0].text)

# -------------------------------
# 7. Chat Input
# -------------------------------
user_input = st.chat_input("Ask me anything about coding...")

if user_input:
    # Show user message
    with st.chat_message("user"):
        st.markdown(user_input)

    # Get Gemini response
    response = st.session_state.chat.send_message(user_input)

    # Show assistant message
    with st.chat_message("assistant"):
        st.markdown(response.text)
