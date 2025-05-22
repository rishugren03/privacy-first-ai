from fastapi import APIRouter, HTTPException
from app.models.mesh import MeshRequest
from app.mesh.registry import get_task, mesh_tasks  # ← Import mesh_tasks to list them

router = APIRouter(prefix="/mesh", tags=["mesh"])

@router.get("/list-tasks")
def list_tasks():
    return {"tasks": list(mesh_tasks.keys())}

@router.post("/run-task")
def run_task(req: MeshRequest):
    task_func = get_task(req.task)
    if not task_func:
        raise HTTPException(status_code=404, detail=f"Task '{req.task}' not found")
    return task_func(req.text)
