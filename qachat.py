from dotenv import load_dotenv
load_dotenv()
import os
import streamlit as st
import google.generativeai as genai
from PIL import Image
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
#function to load gemini pro model and get response
model=genai.GenerativeModel("gemini-pro")
chat=model.start_chat(history=[])
def get_gemini_response(question):
    response=chat.send_message(question, stream=True)
    return response
st.set_page_config(page_title="Q&A Demo")
st.header("Gemini LLM Application")
#initialize session state for chat history if it doesn't exist.
if 'chat_history' not in st.session_state:
    st.session_state['chat_history']=[] 
input=st.text_input("Input:", key="input") 
submit=st.button("ask the question")  
if submit and input:
    response=get_gemini_response(input) 
    #add user query and response to session chat history.
    st.session_state['chat_history'].append(("you", input))
    st.subheader("the response is")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot",chunk.text))
st.subheader("chat history is")
for role, text in st.session_state['chat_history']:
    st.write(f"(role):{text}")
            
 