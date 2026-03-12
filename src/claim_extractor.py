import re

def extract_claim(text):
    """
    Extract the main claim from the input text.
    For now we take the first meaningful sentence.
    """

    sentences = re.split(r'[.!?]', text)

    for s in sentences:
        if len(s.split()) > 3:
            return s.strip()

    return text