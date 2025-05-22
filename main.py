from fastapi import FastAPI 

from app.mesh.registry import auto_register_tasks

from app.mesh.router import router as mesh_router

app = FastAPI()

app.include_router(mesh_router)    

@app.on_event("startup")
def startup_event():
    auto_register_tasks()


@app.get("/")
def read_root():
    return {"message": "Mesh LLM System is Live!"}

@app.get("/health")
def health_check():
    return {"status": "ok", "app": "privacy-first-mesh-LLM"}