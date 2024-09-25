import streamlit as st
from joblib import load

# Imports the functions we coded above
from header import *
from userinput import *
from response import *
from predictor import *



#with st.form("upload-form", clear_on_submit=True):
#    uploaded_file = st.file_uploader("upload", accept_multiple_files=False,
#                                     type=['png', 'jpg', 'jpeg'],
 #                                    help =   model.upload_help)
#    submitted = st.form_submit_button("submit")
#
  #  if submitted and uploaded_file is not None:
  #    ret = self.upload_file(uploaded_file)
#
  #    if ret is not False:
  #      file_names = self.get_existing_file_names('docs/image/')

# Load our DecisionTree model into our web app
# **temp** model = load("DiseaseDetection.joblib")
#st.write ("Model uploaded!") # You may remove this in your finalized web app!
create_background(
    color="#718565",
    text_color="#c0c7bb",
    h1_color="#ffffff",
    button_bg_color="#262b23",
    button_text_color="white",
    header_color="#c0c7bb",
    subheader_color="#c0c7bb",
    title_color="#c0c7bb"
)

create_header()


input_features = get_user_input()

if input_features is not None:
  prediction = make_prediction(input_features)
  get_app_response(prediction)
