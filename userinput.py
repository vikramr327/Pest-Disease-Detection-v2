import streamlit as st
import cv2
import numpy as np
from PIL import Image
def get_user_input():
  help_text = "Please upload a  JPG, image file."

  #uploaded_file = cv2.imread('IMG_1184.JPG')
  with st.form("upload-form", clear_on_submit=True):

      uploaded_file = st.file_uploader("", accept_multiple_files=False,
                                      type=['jpg'],
                                      help=help_text)
      submit_button = st.form_submit_button("Submit")

  if submit_button:
      if uploaded_file is not None:
          st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True)
          uploaded_file = Image.open(uploaded_file)
          uploaded_file = uploaded_file.save("image.jpg")
#          OpenCv Read
          uploaded_file = cv2.imread("image.jpg")
          # st.write("Image uploaded successfully!")
          # uploaded_file = np.array(uploaded_file)

      else:
          #uploaded_file = cv2.imread('IMG_1184.JPG')
          st.write("No file uploaded.")
          return uploaded_file
  else:
    #uploaded_file = cv2.imread('IMG_1184.JPG')
    return uploaded_file

  # blood_pressure = st.number_input("What is your blood pressure?")
  # heart_rate = st.number_input("What is your maximum heart rate during exercise in beats per minute?")
  #input_features = [[uploaded_file]]
  uploaded_file = cv2.cvtColor(uploaded_file, cv2.COLOR_BGR2RGB)
  print(uploaded_file)
  return uploaded_file
