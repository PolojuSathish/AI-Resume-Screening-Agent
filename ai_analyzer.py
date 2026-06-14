import requests # request is like to ask a question to AI ,Example : request=postman
from prompt import PROMPT_TEMPLATE

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3"

def analyze_resume(resume_text,job_description):
    prompt = PROMPT_TEMPLATE.format(resume = resume_text,job_description = job_description)
    payload = {"model": "llama3",
               "prompt":prompt,
               "stream": False}
    response = requests.post(OLLAMA_URL,json=payload)
    if response.status_code == 200:
        return response.json() ["response"]
    else:
        return "Error while analysing resume"