from app.services.privacy import redact_text

def run(text: str):
  return {"redacted_test": redact_text(text)}

