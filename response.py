import streamlit as st
import openai
def get_app_response(prediction):
    st.write(f"Predicted Plant Disease or Pest: {prediction}")

    # Set your OpenAI API key
    if "OPENAI_API_SERVICE_KEY" in st.secrets:
        openai.api_key = st.secrets["OPENAI_API_SERVICE_KEY"]
    else:
        st.error("API Key not found. Please configure the OPENAI_API_KEY in Streamlit Secrets.")

    # Construct the user prompt
    st.write(f"General Information about '{prediction}'")
    user_message = f"Please provide general information, causes, remedies, and where they appear for '{prediction}' and limit output to 100 words"
    # Append the user message to the messages list
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
