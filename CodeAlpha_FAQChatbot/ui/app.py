import streamlit as st
import sys
import os

# allow src imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.data_loader import load_faqs
from src.chatbot import FAQChatbot


# -------- Load chatbot --------
faq_data = load_faqs("data/faqs.txt")
bot = FAQChatbot(faq_data)

st.set_page_config(page_title="FAQ Chatbot")

st.title("FAQ Chatbot")

# -------- Chat memory --------
if "messages" not in st.session_state:
    st.session_state.messages = []

# show chat
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# input
user_input = st.chat_input("Type your question...")

if user_input:
    # user LEFT
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )
    with st.chat_message("user"):
        st.write(user_input)

    # bot RIGHT
    response = bot.get_response(user_input)

    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )
    with st.chat_message("assistant"):
        st.write(response)

