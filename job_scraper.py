import requests
from bs4 import BeautifulSoup

def scrape_job_description(url, agent):
    try:
        return agent.run(f"Extract and summarize the full text content of the job description at this URL: {url}. Return plain text only, no HTML.")
    except Exception:
        try:
            page = requests.get(url)
            soup = BeautifulSoup(page.text, "html.parser")
            return soup.get_text(separator="\n", strip=True)
        except Exception as fallback_error:
            return f"Error retrieving job description: {fallback_error}"
