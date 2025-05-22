from pydantic import BaseModel

class MeshRequest(BaseModel):
  task: str
  text: str