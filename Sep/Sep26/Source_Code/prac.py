import re

def find_emails(text):
    pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    return re.findall(pattern, text)

def validate_phone_number(phone):
    pattern = r'^\+?[\d\s]{10,15}$'
    return bool(re.match(pattern, phone))

def extract_words_starting_with_a(text):
    pattern = r'\ba\w*'
    return re.findall(pattern, text, re.IGNORECASE)
