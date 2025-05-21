from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Mesh LLM System is Live!"}

@app.get("/health")
def health_check():
    return {"status": "ok", "app": "privacy-first-mesh-LLM"}