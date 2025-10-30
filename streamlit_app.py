import streamlit as st
import os
from voice_module import speech_to_text
from nlp_module import generate_sql_from_text
from sql_module import init_db, execute_query

st.title("VoiceQuery AI: Speech to SQL Demo")

conn = init_db()

if st.button("Start Recording"):
    user_query = speech_to_text()
    if user_query:
        st.write(f"Recognized Text: {user_query}")
        sql_query = generate_sql_from_text(user_query)
        if sql_query:
            st.code(sql_query, language="sql")
            result = execute_query(conn, sql_query)
            if isinstance(result, str):
                st.error(f"SQL error: {result}")
            else:
                st.dataframe(result)
        else:
            st.warning("Sorry, couldn't generate SQL for your query.")
