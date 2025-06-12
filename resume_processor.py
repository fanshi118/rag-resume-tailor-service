from langchain.prompts import ChatPromptTemplate

def extract_relevant_sections(llm, resume_text, job_description):
    prompt = ChatPromptTemplate.from_template("""
You are a resume expert. Given the following resume and job description, identify which experiences, skills, and achievements from the resume are most relevant to the job. Do not remove any content, but annotate or emphasize the most relevant parts.

Job Description:
{job_description}

Resume:
{resume_text}

Return the resume with the most relevant content clearly highlighted or annotated.
""")
    messages = prompt.format_messages(resume_text=resume_text, job_description=job_description)
    return llm(messages).content

def generate_tailored_resume(llm, relevant_content, job_description):
    prompt = ChatPromptTemplate.from_template("""
You are a professional resume writer. Given the full resume with highlighted relevant content and the job description, rewrite the resume by keeping all the original content, but organize and format it to prioritize and emphasize the most relevant experiences and skills for the job.

Job Description:
{job_description}

Annotated Resume:
{relevant_content}

Return the tailored resume in plain text.
""")
    messages = prompt.format_messages(job_description=job_description, relevant_content=relevant_content)
    return llm(messages).content
