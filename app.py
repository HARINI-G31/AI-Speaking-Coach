import streamlit as st

st.set_page_config(
    page_title="AI Public Speaking Coach",
    layout="wide"
)

st.title("🎤 AI Public Speaking Coach")

st.write(
    "Upload a speech video to receive AI-powered feedback."
)

video = st.file_uploader(
    "Upload your speech video",
    type=["mp4", "mov", "avi"]
)

if video:
    st.success("Video uploaded successfully!")
