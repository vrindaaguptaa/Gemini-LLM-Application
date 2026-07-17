from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
api_key = st.secrets.get("GOOGLE_API_KEY") or os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=api_key)
        
model=genai.GenerativeModel("gemini-flash-latest")
def get_genai_response(input, image):
    if input !="":
      response=model.generate_content([input, image])
    else:
      response=model.generate_content(image)  
    return response.text
st.set_page_config(page_title="Gemini Image Demo")
st.header("Gemini Application")
input=st.text_input("Input Prompt: ", key="input")
uploaded_file=st.file_uploader("Choose an image...",type=["jpg", "jpeg", "png"] )
image=""
if uploaded_file is not None:
   image=Image.open(uploaded_file)
   st.image(image, caption="uploaded image", use_column_width=True)
submit=st.button("tell me about the image")   
#if submit is clicked
if submit:
   response=get_genai_response(input, image)
   st.subheader("the response is")
   st.write(response)
   
