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
  st.title("Pest Detection")
  st.header("By Vikram Anand")
  st.subheader("Insert an image to see if your plant has a disease!")
