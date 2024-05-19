import streamlit as st
from googletrans import Translator

def translate_text(text, source_language, target_language):
    translator = Translator()
    translated_text = translator.translate(text, src=source_language, dest=target_language)
    return translated_text.text

def main():
    st.title("Language Translation App")
    
    input_text = st.text_area("Enter text to translate:")
    
    source_language = st.selectbox("Select source language:", ["Auto", "English", "French", "German", "Spanish", "Italian", "Chinese", "Japanese", "Korean"])
    
    target_language = st.selectbox("Select target language:", ["Select", "English", "French", "German", "Spanish", "Italian", "Chinese", "Japanese", "Korean"])
    
    if st.button("Translate"):
        if input_text.strip() == "":
            st.warning("Please enter some text to translate.")
        elif target_language == "Select":
            st.warning("Please select a target language.")
        else:
            translated_text = translate_text(input_text, source_language.lower(), target_language.lower())
            st.success(f"Translated text ({target_language}):")
            st.write(translated_text)

if __name__ == "__main__":
    main()