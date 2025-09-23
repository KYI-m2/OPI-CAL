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
import streamlit.components.v1 as html
import io 
from pathlib import Path
import base64
import openpyxl
from streamlit_webrtc import webrtc_streamer
import gspread
from oauth2client.service_account import ServiceAccountCredentials


with st.sidebar :
  st.logo(
  "Add a heading.png", # Replace with your logo URL or file path
  size="large", # Options: "small", "medium", "large"
  )
  choose = option_menu(
    "OPI-CAL",
    ["Home","Introduction", "How to use", "Reference","Survey"],
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
        dose = f"{number2*number3/number1:.3f}"
        doses = number2*number3/number1
        max = 0.5 * number1/number2
        st.write("ขนาดยา : ", dose , "mg/kg/hr" )
        if doses > 0.5 :
          st.markdown(
            ":red-badge[⚠️ ขนาดยาเกินกำหนดควรปรึกษาแพทย์]"
          )
        st.write("อัตราเร็วการบริหารยาสูงสุด : ", max , "ml/hr")
        st.write("ปริมาณยาที่ต้องจ่ายต่อวัน (10mg/ampule) : ", number2 * number3*24 / 10 , "ampule")
        
  elif selection == 1 :
    with st.form("my_form"):
      st.write("Fentanyl Calculator")
      st.write("ขนาดยาสำหรับระงับปวดในผู้ป่วยที่ใช้เครื่องช่วยหายใจ (Barr et al., 2013)")
      st.write("Intermittent dosage 0.35 to 0.5 mcg/kg IV every 0.5 to 1 hour")
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
        dose = f"{number5 * number6 / number4:.3f}"
        doses = number5 * number6 / number4
        max = 10 * number4 / number5
        st.write("ขนาดยา : ", dose , "mcg/kg/hr" )
        if doses > 10 :
          st.markdown(
            ":red-badge[⚠️ ขนาดยาเกินกำหนดควรปรึกษาแพทย์]"
          )
        st.write("อัตราเร็วการบริหารยาสูงสุด : ", max , "ml/hr")
        st.write("ปริมาณยาที่ต้องจ่ายต่อวัน  (500 mcg/ampule) : ", number5 * number6*24 / 500,"amplue" )
        st.write("หรือ")
        st.write("ปริมาณยาที่ต้องจ่ายต่อวัน (100 mcg/ampule): ", number5 * number6*24 / 100 ,"ampule")
  if selection == 2:
    option_map = {
    0: "Morphine",
    1: "Fentanyl",
}
    select = st.segmented_control(
        "Tool",
        options=option_map.keys(),
        format_func=lambda option: option_map[option],
        selection_mode="single",
    )
    if select == 0:
       st.image("IMG_1143.jpeg")
    if select == 1:
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
if choose == "Survey" :
  # ตั้งค่า API URL ของ SheetDB
  SHEETDB_URL = "https://sheetdb.io/api/v1/smgl4hh9a6bqa"
  
  # สร้างฟอร์มใน Streamlit
  st.title("ประเมินประโยชน์การใช้งานของเว็บเเอปพลิเคชันการคำนวณขนาดยากลุ่ม Opioid")
  
  with st.form("data_form"):
    first = st.text_input("First name")
    last = st.text_input("Last name")
    
    one = st.selectbox("ระดับความพึงพอใจด้านความชัดเจนของเนื้อหา",
                    ["5", "4", "3", "2", "1"])
    if one == "5":
     one = 5
    elif one == "4":
     one = 4
    elif one == "3":
     one = 3
    elif one == "2":
     one = 2
    else:
     one = 1
    
    two = st.selectbox("ระดับความพึงพอใจด้านการคำนวณได้อย่างถูกต้องแม่นยำ",
                    ["5", "4", "3", "2", "1"])
    if two == "5":
     two = 5
    elif two == "4":
     two = 4
    elif two == "3":
     two = 3
    elif two == "2":
     two = 2
    else:
     two = 1
    
    three = st.selectbox("ระดับความพึงพอใจด้านเคุณค่าในการใช้ประโยชน์ของเนื้อหา",
                      ["5", "4", "3", "2", "1"])
    if three == "5":
     three = 5
    elif three == "4":
     three = 4
    elif three == "3":
     three = 3
    elif three == "2":
     three = 2
    else:
     three = 1
    
    four = st.selectbox("ระดับความพึงพอใจด้านความรวดเร็วของการแสดงผล",
                     ["5", "4", "3", "2", "1"])
    if four == "5":
     four = 5
    elif four == "4":
     four = 4
    elif four == "3":
     four = 3
    elif four == "2":
     four = 2
    else:
     four = 1
    
    five = st.selectbox("ระดับความพึงพอใจด้านความสะดวกในการใช้งาน",
                     ["5", "4", "3", "2", "1"])
    if five == "5":
     five = 5
    elif five == "4":
     five = 4
    elif five == "3":
     five = 3
    elif five == "2":
     five = 2
    else:
     five = 1
    
    mean = (one + two + three + four + five) / 5
    
    if mean >= 1 and mean <= 1.50:
     satisfaction = "น้อยที่สุด"
    elif mean >= 1.51 and mean <= 2.50:
     satisfaction = "น้อย"
    elif mean >= 2.51 and mean <= 3.50:
     satisfaction = "ปานกลาง"
    elif mean >= 3.51 and mean <= 4.50:
     satisfaction = "มาก"
    elif mean >= 4.51 and mean <= 5:
     satisfaction = "มากที่สุด"
    else:
     satisfaction = "ข้อมูลผิดพลาด"
    submitted = st.form_submit_button("ส่งข้อมูล")
    if submitted:
      # ส่งข้อมูลไปยัง SheetDB
      data = {"data": [{"First name": first, "Last name": last, "Mean": mean, "Satisfaction": satisfaction }]}
      response = requests.post(SHEETDB_URL, json=data)
  
      if response.status_code == 201:
          st.success("บันทึกข้อมูลสำเร็จ!")
      else:
          st.error(f"เกิดข้อผิดพลาด: {response.text}")































