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
  "Add a heading.png", # Replace with your logo URL or file path
  size="large", # Options: "small", "medium", "large"
  )
  choose = option_menu(
    "OPI-CAL",
    ["Home","Introduction", "How to use", "Reference"],
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
    lottie_hello = load_lottieurl("https://lottie.host/ad42cd73-5b45-489e-926b-430e3360f365/Bhm0HXK9It.json")
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
      st.write("ขนาดยาสำหรับระงับปวดในผู้ป่วยที่ใช้เครื่องช่วยหายใจ (Jacobi et al., 2002)")
      st.write("Intermittent dosage 0.01 to 0.15 mg/kg IV every 1 to 2 hours")
      st.write("Continuous infusion 0.07 to 0.5 mg/kg/hr IV")
      number1 = st.number_input(
          "กรอกน้ำหนักผู้ป่วย (kg)", value=None, placeholder="..."
      )
      number2 = st.number_input(
          "กรอกความเข้มข้นของยา (mg/ml)", value=None, placeholder="..."
      )
      number3 = st.number_input(
          "กรอกอัตราเร็วการบริหารยาที่เเพทย์สั่ง (ml/hr)", value=None, placeholder="..."
      )
      
    
      submit = st.form_submit_button("Submit")
      if submit:
        dose = number2*number3/number1
        max = 0.5 * number1/number2
        st.write("ขนาดยา : ", dose , "mg/kg/hr" )
        if dose > 5 :
          st.markdown(
            ":red-badge[⚠️ ขนาดยาเกินกำหนดควรปรึกษาแพทย์]"
          )
        st.write("อัตราเร็วการบริหารยาสูงสุด : ", max , "ml/hr")
        st.write("ปริมาณยาที่ต้องจ่ายต่อวัน (10mg/ampule) : ", number2 * number3*24 / 10 , "ampule")
        
  elif selection == 1 :
    with st.form("my_form"):
      st.write("Fentanyl Calculator")
      st.write("ขนาดยาสำหรับระงับปวดในผู้ป่วยที่ใช้เครื่องช่วยหายใจ (Barr et al., 2013)")
      st.write("ขนาดยา: Intermittent dosage 0.35 to 0.5 mcg/kg IV every 0.5 to 1 hour")
      st.write("Continuous infusion 0.7 to 10 mcg/kg/hr IV")
      number4 = st.number_input(
          "กรอกน้ำหนักผู้ป่วย (kg)", value=None, placeholder="..."
      )
      number5 = st.number_input(
          "กรอกความเข้มข้นของยา (mcg/mg)", value=None, placeholder="..."
      )
      number6 = st.number_input(
          "กรอกอัตราเร็วการบริหารยาที่เเพทย์สั่ง (ml/hr)", value=None, placeholder="..."
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
        st.write("ปริมาณยาที่ต้องจ่ายต่อวัน  (500 mcg/ampule) : ", number5 * number6*24 / 500,"amplue" )
        st.write("หรือ")
        st.write("ปริมาณยาที่ต้องจ่ายต่อวัน (100 mcg/ampule): ", number5 * number6*24 / 100 ,"ampule")
  if selection == 2:
    if st.button("Morphine"):
       st.image("IMG_1143.jpeg")
    if st.button("Fentanyl"):
       st.image("IMG_1144 (2).jpeg")
    st.write("กดเพื่อดูข้อมูล")
  if selection ==3 :
      st.image("r.jpeg")
if choose == "Introduction" :
  st.title("วัตถุประสงค์ของเว็บเเอปพลิเคชัน")
  st.write("เว็บเเอปพลิเคชันนี้จัดทำขึ้นเพื่อใช้คำนวณขนาดยากลุ่ม Opioid สำหรับระงับปวดในผู้ป่วยที่ใช้เครื่องช่วยหายใจ ซึ่งจะช่วยลดขั้นตอนในการคำนวณขนาดยาที่ผู้ป่วยได้รับ อัตราเร็วสูงสุดในการบริหารยา ปริมาณยาที่ต้องจ่ายต่อวัน รวมถึงสามารถให้ข้อมูลวิธีการเจือจางยา สำหรับให้ทางหลอดเลือดดำ และการติดตามความปลอดภัยของยากลุ่ม Opioid")
  st.badge("โดยข้อมูลทั้งหมดนี้ ได้รับการตรวจสอบความถูกต้องจาก งานติดตามอาการไม่พึงประสงค์จากยาเเละเภสัชนเทศ")
  st.badge("รพ.นพรัตนราชธานี")
  st.divider()
  st.header("แนะนำสมาชิก")
  st.image("aoon.jpg", width=200)
  st.markdown("ด.ญ. กานต์ปภา ประจิตร ม.3/3 เลขที่ 21 (หัวหน้ากลุ่ม)")
  
  st.divider()
  
  st.image("arm.jpg", width=200)
  st.markdown("ด.ช. พีรณัฐ ธนฤกษ์ ม.3/3 เลขที่ 17")
  
  st.divider()
  
  st.image("Peem3.jpeg", width=200)
  st.markdown("ด.ญ. ชนันธร มามีชัย ม.3/3 เลขที่ 23")
  
  st.divider()
  
  st.image("miu.jpg", width=200)
  st.markdown("ด.ญ. ฐิตามร กณิกนันต์ ม.3/3 เลขที่ 24")
  
  st.divider()
  
  st.image("parn.jpg", width=200)
  st.markdown("ด.ญ. นพภัสสร ลิขิตธีรวุฒิ ม.3/3 เลขที่ 28")


if choose == "How to use" :  
  st.image("1.png")
  st.image("2.png")
  st.image("3.png")
  st.image("4.png")
  st.image("5.png")

if choose == "Reference" :
  st.image("ref.jpeg")


















