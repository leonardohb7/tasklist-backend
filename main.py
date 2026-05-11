from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

tasks = []

class Task(BaseModel):
    task: str
    priority: int

@app.post("/tasks")
def add_tasks(task: Task):
    tasks.append(task)
    return {"Message": "Task added successfully!", "Task": task}

@app.get("/tasks") 
def get_tasks():
    return tasks

# NOVA ROTA PUT
@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: Task):
    if task_id < 0 or task_id >= len(tasks):
        return {"error": "ID inválido"}

    tasks[task_id] = task
    return {"message": "Tarefa atualizada com sucesso!", "task": task}

# NOVA ROTA DELETE
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    if task_id < 0 or task_id >= len(tasks):
        return {"error": "ID inválido"}
    tasks.pop(task_id)
    return {"message": "Tarefa excluída com sucesso!"}