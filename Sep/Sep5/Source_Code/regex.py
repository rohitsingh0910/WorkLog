import re

def extract_emails(text):
    pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    return re.findall(pattern, text)

def validate_phone_number(number):
    pattern = r'^\+?\d{10,15}$'
    return bool(re.match(pattern, number))

def find_dates(text):
    pattern = r'\b\d{2}/\d{2}/\d{4}\b'
    return re.findall(pattern, text)

def split_sentences(text):
    pattern = r'(?<=[.!?])\s+'
    return re.split(pattern, text)
