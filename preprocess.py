import re

def clean_text(text):
    text = text.encode('latin1', errors='ignore').decode('utf-8', errors='ignore')
    text = re.sub(r'[^\x00-\x7F]+', ' ', text)  # remove non-ASCII
    text = re.sub(r'\s+', ' ', text).strip()
    text = text.lower()
    return text
