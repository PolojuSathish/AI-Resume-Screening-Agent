#import liabraries
import streamlit as st
from resume_parser import extract_text_from_pdf
from ai_analyzer import analyze_resume

#=====================================================================
#page Configuration
st.set_page_config(
    page_title= "AI Resume Screening Agent",
    page_icon="📄",
    layout="wide"
)

#=========================================================================
#Title and Description
st.title("📄 AI-Powered Resume Screening Agent")
st.markdown("Analyze resumes intelligently using Llama 3 and Ollama")

uploaded_resume = st.file_uploader("Upload Resume(pdf)",
                                   type=["pdf"])


job_description = st.text_area("Paste Job Description",
                               height=250)


if st.button("Analyze Resume"):
    if uploaded_resume is not None and job_description != " ":
        with st.spinner("Analyzing Resume..."):
            resume_text = extract_text_from_pdf(uploaded_resume)
            analysis_result = analyze_resume(resume_text,job_description)

            st.success("Analysis Completed")

            st.subheader("Analysis Result")
            st.write(analysis_result)
else:
        st.warning("Please upload resume and enter job description")            
     
