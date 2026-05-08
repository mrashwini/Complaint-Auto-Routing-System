import sys
import os
import tempfile

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

import streamlit as st

from inference_pipeline import run_pipeline
from src.preprocessing.audio_transcriber import transcribe_audio

st.title("Complaint Auto-Routing System")

input_type = st.radio(
    "Choose Input Type",
    ["Text", "Audio"]
)

complaint = ""

# TEXT INPUT
if input_type == "Text":

    complaint = st.text_area(
        "Enter Complaint"
    )

# AUDIO INPUT
elif input_type == "Audio":

    audio_file = st.file_uploader(
        "Upload Audio",
        type=["wav", "mp3"]
    )

    if audio_file:

        with tempfile.NamedTemporaryFile(
            delete=False
        ) as tmp:

            tmp.write(
                audio_file.read()
            )

            temp_path = tmp.name

        complaint = transcribe_audio(
            temp_path
        )

        st.subheader(
            "Transcribed Text"
        )

        st.write(complaint)

# ANALYZE BUTTON
if st.button("Analyze Complaint"):

    if complaint.strip() == "":

        st.warning(
            "Please enter or upload a complaint."
        )

    else:

        result = run_pipeline(
            complaint
        )

        st.success(
            "Analysis Complete"
        )

        # METRICS
        col1, col2 = st.columns(2)

        with col1:

            st.subheader(
                "Priority"
            )

            st.metric(
                "Priority",
                result["priority"]
            )

        with col2:

            st.subheader(
                "ETA"
            )

            st.metric(
                "ETA Days",
                result["eta_days"]
            )

        # TOP OFFICERS
        st.subheader(
            "Recommended Officers"
        )

        officers = result.get(
            "assigned_officers",
            []
        )

        # fallback for old structure
        if not officers and "assigned_officer" in result:

            officers = [
                result["assigned_officer"]
            ]

        for officer in officers:

            st.write(officer)

        # SIMILAR COMPLAINTS
        st.subheader(
            "Similar Complaints"
        )

        for item in result[
            "similar_complaints"
        ]:

            st.write(item)