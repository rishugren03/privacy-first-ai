from fastapi import APIRouter
from pydantic import BaseModel
from app.services.privacy import redact_text

router = APIRouter()

class FilterRequest(BaseModel):
  text: str

class FilterResponse(BaseModel):
  redacted_text: str

@router.post("/filter-private", response_model=FilterResponse)
def filter_private(req: FilterRequest):
  redacted = redact_text(req.text)
  return {"redacted_text": redacted}    