import streamlit as st
from llm_utils import initialize_llm_and_agent
from file_utils import load_text, convert_text_to_docx, convert_text_to_txt
from job_scraper import scrape_job_description
from resume_processor import extract_relevant_sections, generate_tailored_resume

st.title("Tailor Your Resume to a Job Posting")

resume_file = st.file_uploader("Upload your resume (.docx or .txt)", type=["docx", "txt"])
job_url = st.text_input("Enter the job description URL")

if resume_file and job_url and st.button("Generate Tailored Resume"):
    with st.spinner("Processing..."):
        llm, agent = initialize_llm_and_agent()
        resume_text, ext = load_text(resume_file)
        job_description = scrape_job_description(job_url, agent)
        relevant_content = extract_relevant_sections(llm, resume_text, job_description)
        tailored_resume = generate_tailored_resume(llm, relevant_content, job_description)

        st.subheader("Original Resume")
        st.text_area("Resume Text", resume_text, height=300)

        st.subheader("Tailored Resume")
        st.text_area("Tailored Resume Text", tailored_resume, height=300)

        if ext == "docx":
            path = convert_text_to_docx(tailored_resume)
            with open(path, "rb") as f:
                st.download_button("Download Tailored Resume (DOCX)", f, file_name="tailored_resume.docx")
        else:
            path = convert_text_to_txt(tailored_resume)
            with open(path, "rb") as f:
                st.download_button("Download Tailored Resume (TXT)", f, file_name="tailored_resume.txt")
