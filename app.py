import streamlit as str
from pypdf import PdfReader
from gtts import gTTS
import io

#website layout and title setup
str.set_page_config(page_title="AI Audiobook Creator", page_icon="🎧", layout="centered")

str.title("AI PDF AudioBook Converter")
str.caption("Made by Samit Singh ✨")
str.write("Uplod your pdf file and convert it into audio file directly in your phone")

uploaded_file = str.file_uploader("Select PDF File", type=["pdf"])

lang_choice = str.selectbox(
    "Select Voice Accent:",
    ["English (India)", "English (US)", "Hindi"]

)
tld_val = "com"
lang_val = "en"
if lang_choice == "English (India)":
    tld_val = "co.in"
elif lang_choice == "Hindi":
    lang_val = "hi"

if uploaded_file is not None:
    if str.button("⚡ Convert to Audio", type="primary"):
        with str.spinner("Extracting text and generating audio... Please wait..."):
            try:
                reader = PdfReader(uploaded_file)
                full_text = ""
                for page in reader.pages:
                    text = page.extract_text()
                    if text:
                        full_text += text + " "

                if not full_text.strip():
                    str.error("There is no error in this pdf!")
                else:
                    tts = gTTS(text=full_text, lang=lang_val, tld=tld_val, slow=False)

                    audio_fp = io.BytesIO()
                    tts.write_to_fp(audio_fp)
                    audio_fp.seek(0)

                    str.success("🎉 Sucess! Your Audiobook is ready")

                    str.audio(audio_fp, format="audio/mp3")

                    str.download_button(
                        label="📥 Download MP3 Audio",
                        data=audio_fp,
                        file_name="my_audiobook.mp3",
                        mime="audio/mp3"
                    )
            except Exception as e:
                str.error(f"Something went wrong: {e}")