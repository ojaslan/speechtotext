import streamlit as st
from gtts import gTTS

# Streamlit App Title
st.title("Text-to-Speech Application")
st.markdown("""
A text-to-speech application supporting multiple languages and voices.  
Customize the speech synthesis settings as per your preferences!
""")

# User Input for Text
text = st.text_area("Enter the text you want to convert to speech:", placeholder="Type something here...")

# Language Selection
language = st.selectbox(
    "Select a Language:",
    options=["en", "fr", "es", "hi", "de"]
)

# Generate Speech
if st.button("Convert to Speech"):
    if text.strip():
        try:
            # Generate speech using gTTS
            tts = gTTS(text=text, lang=language)
            tts.save("output.mp3")
            st.audio("output.mp3", format="audio/mp3")
        except Exception as e:
            st.error(f"Error generating speech: {e}")
    else:
        st.warning("Please enter some text to convert to speech!")
