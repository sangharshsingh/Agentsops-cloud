
from fastapi import FastAPI, HTTPException, status
from uuid import uuid4

from app.schemas import TaskCreate


app = FastAPI(
    title="AgentOps Cloud",
    version="0.1.0"
)

# Temporary in-memory task storage
tasks_db = {}


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "agentops-control-plane"
    }


@app.post("/tasks", status_code=status.HTTP_202_ACCEPTED)
def create_task(task: TaskCreate):
    task_id = str(uuid4())

    task_data = {
        "task_id": task_id,
        "status": "accepted",
        "agent_type": task.agent_type,
        "prompt": task.prompt
    }

    tasks_db[task_id] = task_data

    return task_data


@app.get("/tasks/{task_id}")
def get_task(task_id: str):
    if task_id not in tasks_db:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return tasks_db[task_id]
