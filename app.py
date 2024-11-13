from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai


#now we have to load our api key means we have to configure it.
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#function to load gemini pro model and get responses.
model=genai.GenerativeModel("gemini-pro")
def get_gemini_response(question):
    response=model.generate_content(question)
    return response.text 

# setting aur streamlit app.

st.header("Gemini LLM Application")
input=st.text_input("Input: ", key="input")
submit=st.button("ask the question")

#when submit is clicked
if submit:
    response=get_gemini_response(input)
    st.subheader("the response is")
    st.write(response)

