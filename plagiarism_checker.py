import requests
from bs4 import BeautifulSoup
from sentence_transformers import SentenceTransformer, util
import re

# Google API credentials
API_KEY = "AIzaSyAYYSSVruHFunVUfYQw6HrPtn0_Epabz7I"
CSE_ID = "b553681ed7b664992"

# Load semantic model
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

def clean_text(text):
    text = re.sub(r'[^\w\s]', '', text.lower())
    return text

def search_google(query, api_key, cse_id):
    url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={api_key}&cx={cse_id}"
    response = requests.get(url)
    results = response.json().get("items", [])
    return [item["link"] for item in results]

def extract_text_from_url(url):
    try:
        page = requests.get(url, timeout=5)
        soup = BeautifulSoup(page.text, "html.parser")
        paragraphs = soup.find_all('p')
        return ' '.join([p.get_text() for p in paragraphs])
    except:
        return ""

def check_plagiarism(input_text):
    print("Searching for similar content\n")
    search_links = search_google(clean_text(input_text), API_KEY, CSE_ID)
    
    input_embedding = model.encode(input_text, convert_to_tensor=True)
    for link in search_links:
        page_text = extract_text_from_url(link)
        if not page_text.strip():
            continue

        page_embedding = model.encode(page_text, convert_to_tensor=True)
        similarity = util.cos_sim(input_embedding, page_embedding).item()
        
        print(f" {link}")
        print(f" Similarity: {round(similarity * 100, 2)}%\n")
        
        if similarity > 0.75:
            print(" High similarity — Possible Plagiarism Detected!\n")
        elif similarity > 0.5:
            print(" Moderate similarity — Needs review.\n")

# === Run the checker ===
input_text = """
Machine learning is a field of computer science that gives computers the ability to learn without being explicitly programmed.
"""
check_plagiarism(input_text)
