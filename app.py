import streamlit as st 
from streamlit_option_menu import option_menu
import time
import numpy as np
import pandas as pd
import requests
from streamlit_lottie import st_lottie
import json
import requests
import streamlit_lottie
from streamlit_lottie import st_lottie


with st.sidebar :
  st.logo(
  "logo2.png", # Replace with your logo URL or file path
  size="large", # Options: "small", "medium", "large"
  )
  choose = option_menu(
    "OPI-CAL",
    ["Home","Introduction"],
    icons = ["book","envelope"]
  )

if choose == "Home" :  
  col1, col2, col3 = st.columns(3)
  with col2 :
    def load_lottieurl(url: str):
      r = requests.get(url)
      if r.status_code !=200: 
          return None 
      return r.json()
    lottie_hello = load_lottieurl("https://lottie.host/2cf65467-1261-4054-b579-80d34a87e0d4/gdPBlurvbp.json")
    st_lottie(
      lottie_hello,
      height=150,  # Set the desired height in pixels
      width=150,   # Set the desired width in pixels
      key="hello"
    )
  st.subheader("Web Application for Opioid Dose Calculation for Analgesia in Adult Mechanically Ventilated Patients")


  
  

  time.sleep(5)
  progress_text = "Loading in progress. Please wait."
  my_bar = st.progress(0, text=progress_text)

  for percent_complete in range(100):
      time.sleep(0.01)
      my_bar.progress(percent_complete + 1, text=progress_text)

  time.sleep(1)
  my_bar.empty()
  option_map = {
    0: "Morphine",
    1: "Fentanyl",
    2: "วิธีการเจือจางยา",
    3: "การติดตามความปลอดภัยเเละยาต้านพิษ"
  }
  selection = st.pills(
    "Selection",
    options=option_map.keys(),
    format_func=lambda option: option_map[option],
    selection_mode="single",
  )
  if selection == 0:
    with st.form("my_form"):
      st.write("Morphine Calculator")
      number1 = st.number_input(
          "กรอกน้ำหนัก (kg)", value=None, placeholder="..."
      )
      number2 = st.number_input(
          "กรอกความเข้มข้น (mg/ml)", value=None, placeholder="..."
      )
      number3 = st.number_input(
          "กรอกอัตราเร็วการบริหารยา (ml/hr)", value=None, placeholder="..."
      )
      
    
      submit = st.form_submit_button("Submit")
      if submit:
        dose = number2 * number3 / number1
        max = 0.5 * number1 / number2
        st.write("ขนาดยา : ", dose , "mg/kg/hr" )
        if dose > 5 :
          st.markdown(
            ":red-badge[⚠️ ขนาดยาเกินกำหนดควรปรึกษาแพทย์]"
          )
        st.write("อัตราเร็วการบริหารยาสูงสุด : ", max , "ml/hr")
        st.write("ยาที่ต้องจ่ายต่อวัน : ", number2 * number3*24 / 10 , "10mg/ampule")
        
  elif selection == 1 :
    with st.form("my_form"):
      st.write("Fentanyl Calculator")
      number4 = st.number_input(
          "กรอกน้ำหนัก (kg)", value=None, placeholder="..."
      )
      number5 = st.number_input(
          "กรอกความเข้มข้น (mcg/mg)", value=None, placeholder="..."
      )
      number6 = st.number_input(
          "กรอกอัตราเร็วการบริหารยา (ml/hr)", value=None, placeholder="..."
      )


      submit = st.form_submit_button("Submit")
      if submit:
        dose = number5 * number6 / number4
        max = 10 * number4 / number5
        st.write("ขนาดยา : ", dose , "mg/kg/hr" )
        if dose > 5 :
          st.markdown(
            ":red-badge[⚠️ ขนาดยาเกินกำหนดควรปรึกษาแพทย์]"
          )
        st.write("อัตราเร็วการบริหารยาสูงสุด : ", max , "ml/hr")
        st.write("ยาที่ต้องจ่ายต่อวัน : ", number5 * number6*24 / 500 , "500 mcg/ampule")
        st.write("ยาที่ต้องจ่ายต่อวัน : ", number5 * number6*24 / 100 , "100 mcg/ampule")
  if selection == 2:
    if st.button("Morphine"):
       st.image("IMG_1143.jpeg")
    if st.button("Fentanyl"):
       st.image("IMG_1144 (2).jpeg")
    st.write("กดเพื่อดูข้อมูล")
  if selection ==3 :
      st.image("r.jpeg")


