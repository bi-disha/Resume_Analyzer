import os
os.system("python -m spacy download en_core_web_sm")
import streamlit as st
from parser import extract_text
from nlp_utils import preprocess, extract_skills, match_score

st.title("Resume Analyzer using NLP")

resume_file = st.file_uploader("Upload Resume")
job_desc = st.text_area("Paste Job Description")

if resume_file and job_desc:
    resume_text = extract_text(resume_file)
    
    clean_resume = preprocess(resume_text)
    clean_job = preprocess(job_desc)

    score = match_score(clean_resume, clean_job)

    res_skills = extract_skills(clean_resume)
    job_skills = extract_skills(clean_job)

    missing = list(set(job_skills) - set(res_skills))

    st.subheader(f"Match Score: {score}%")
    st.write("Resume Skills:", res_skills)
    st.write("Missing Skills:", missing)