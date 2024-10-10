import streamlit as st
import openai
def get_app_response(prediction):
    #st.write(f"Predicted Plant Disease or Pest: {prediction}")
    st.markdown(f"<p style='font-size:18px'><strong>Predicted Plant Disease or Pest: {prediction}<strong></p>", unsafe_allow_html=True)
    # Set your OpenAI API key
    if "OPENAI_API_SERVICE_KEY" in st.secrets:
        openai.api_key = st.secrets["OPENAI_API_SERVICE_KEY"]
    else:
        st.error("API Key not found. Please configure the OPENAI_API_KEY in Streamlit Secrets.")

    # Construct the user prompt
    st.markdown(f"<p style='font-size:18px'><strong>*General Information about {prediction}*:<strong></p>", unsafe_allow_html=True)
    #st.write(f"**General Information about '{prediction}'**")
    user_message = f"Please provide general information, causes, specific remedies, where they appear, and similar looking diseases they(use you instead of they in response) should check out should also  for '{prediction}' in 175 words - Go pretty in depth and split the causes remedies and where they appear in sections/lists where it applies. In less than 30 words, please include a sentence that mentions in some way that the model uses image detection and isn't perfect so they should also check out some diseases similar to '{prediction}' of your knowledge that look similar and may get confused by the model."
    messages = [
        {"role": "system", "content": "You are an intelligent assistant."},
        {"role": "user", "content": user_message}
    ]

    # Make the API request to ChatGPT
    try:
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", 
            messages=messages
        )
    except openai.error.RateLimitError:
        st.write("Rate limit exceeded. Please try again later.")
    except Exception as e:
        st.write(f"An error occurred: {str(e)}")
        
    reply = chat.choices[0].message.content
    st.write(f"{reply}")  # Display the reply in Streamlit
    messages.append({"role": "assistant", "content": reply})
