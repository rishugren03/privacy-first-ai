import spacy
import re

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Define the entity labels you want to redact
REDACTABLE_ENTITIES = {"PERSON", "GPE", "ORG", "LOC"}

# Common regex patterns
PATTERNS = {
    "EMAIL": r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b",
    "PHONE": r"\b(?:\+91[\-\s]?)?[6-9]\d{9}\b",
    "AADHAAR": r"\b\d{4}[\s-]?\d{4}[\s-]?\d{4}\b",
    "PAN": r"\b[A-Z]{5}\d{4}[A-Z]\b",
    "IP": r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b"
}

def redact_text(text: str) -> str:
  doc = nlp(text)
  redacted_text = text

  # 1. Redact named entities (PERSON, ORG, etc.)
  for ent in reversed(doc.ents):
    if ent.label_ in REDACTABLE_ENTITIES:
      redacted_text = redacted_text[:ent.start_char] + "[REDACTED]" + redacted_text[ent.end_char:]

  # 2. Redact patterns (emails, phone, etc.)
  for label, pattern in PATTERNS.items():
      redacted_text = re.sub(pattern, "[REDACTED]", redacted_text)    

  return redacted_text    