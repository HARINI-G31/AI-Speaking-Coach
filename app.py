import os
import streamlit as st

from services.video_processor import get_video_metadata

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
    save_path = os.path.join("data", "raw", video.name)

    with open(save_path, "wb") as f:
        f.write(video.getbuffer())

    st.success("Video uploaded successfully!")

    st.video(save_path)

    metadata = get_video_metadata(save_path)

    if metadata:
        st.subheader("📊 Video Information")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Duration",
                f"{metadata['duration']} sec"
            )
            st.metric(
                "FPS",
                metadata["fps"]
            )

        with col2:
            st.metric(
                "Frame Count",
                metadata["frame_count"]
            )
            st.metric(
                "Resolution",
                metadata["resolution"]
            )
    else:
        st.error("Unable to process the uploaded video.")