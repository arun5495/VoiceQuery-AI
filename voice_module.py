import speech_recognition as sr
import streamlit as st

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Please speak your query after the beep...")
        audio = recognizer.listen(source, phrase_time_limit=5)
        st.success("Processing your voice...")
    try:
        text = recognizer.recognize_google(audio)
        return text
    except Exception as e:
        st.error(f"Could not understand audio: {e}")
        return None
