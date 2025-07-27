import streamlit as st
from main import get_groq_response
import datetime

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Streamlit app layout
st.set_page_config(page_title="Business AI Assistant", layout="wide")
st.markdown("""
    <style>
        .main {
            background-color: #f0f2f6;
        }
        .stTextInput>div>div>input {
            font-size: 16px;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🤖 Business AI Chatbot")
st.markdown("Ask your business questions or get AI-powered assistance instantly.")

# Chat display area
chat_container = st.container()
with chat_container:
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.chat_message("user").markdown(msg["content"])
        else:
            st.chat_message("assistant").markdown(msg["content"])

# Chat input
user_input = st.chat_input("Type your message here...")

if user_input:
    # Store user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.chat_message("user").markdown(user_input)

    # Call the actual Groq backend for AI response
    with st.spinner("Groq is typing..."):
        response = get_groq_response(st.session_state.messages)

    # Store and display assistant message
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.chat_message("assistant").markdown(response)

# Footer or info section
st.sidebar.title("🧠 About this Bot")
st.sidebar.markdown("This AI Assistant helps business owners with queries like:")
st.sidebar.markdown("- 📈 Market insights\n- 🧾 Invoice clarification\n- 💼 Client communication\n- 📊 Data summaries")


