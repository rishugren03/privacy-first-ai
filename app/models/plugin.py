from pydantic import BaseModel

class Plugin(BaseModel):
  name: str
  input_type: str
  output_type: str
  description: str