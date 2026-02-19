import streamlit as st
import os

from translator import translate_text

st.title("🌍 Language Translation Tool")

# Language dictionary
languages = {
    "English": "en",
    "Hindi": "hi",
    "Marathi": "mr",
    "French": "fr",
    "German": "de"
}

text = st.text_area("Enter text")

source_language = st.selectbox(
    "Source Language",
    list(languages.keys())
)

target_language = st.selectbox(
    "Target Language",
    list(languages.keys())
)

# ---- session state (put once near top of file) ----
if "result" not in st.session_state:
    st.session_state.result = ""

# ---- Translate Button ----
if st.button("Translate"):
    st.session_state.result = translate_text(
        text,
        languages[source_language],
        languages[target_language]
    )

# ---- Show Result ----
if st.session_state.result:
    st.success(st.session_state.result)


