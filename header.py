import streamlit as st

def create_background(color: str, text_color: str = None, h1_color: str = None, button_bg_color: str = None, button_text_color: str = None, header_color: str = None, subheader_color: str = None, title_color: str = None):
    # Define custom CSS with optional parameters for text, h1, and button colors
    css = f"""
    <style>
    /* Target the main elements in Streamlit */
    .main {{
        background-color: {color} !important; /* Change the background color */
    }}
    .block-container {{
        background-color: {color} !important; /* Change the background color */
    }}
    .stApp {{
        background-color: {color} !important; /* Change the background color */
    }}
    {f'body {{ color: {text_color} !important; }}' if text_color else ''}
    {f'h1 {{ color: {h1_color} !important; }}' if h1_color else ''}
    {f'.stButton>button {{ background-color: {button_bg_color} !important; color: {button_text_color} !important; }}' if button_bg_color and button_text_color else ''}
    </style>
    """
    # Inject the CSS
    st.markdown(css, unsafe_allow_html=True)


def create_header():
    st.markdown(
        """
        <h1 style='margin-bottom: 0; text-align: center;'>AgriSpection</h1>
        <h2 style='margin-top: 0; text-align: center;'>By Vikram Anand</h2>
        <h5 style='text-align: center;'>This application utilizes image detection and integrates AI in order to identify a pest or disease from over 35 trained categories</h5>
        <h5 style='text-align: center;'>Upload a clear image to see if your plant has a disease or pest!</h5>
        """,
        unsafe_allow_html=True
    )
