from fastapi import APIRouter, HTTPException
from src.schemas import ToDoPydanticModel
from src.managers import ToDoManager

router = APIRouter()


@router.post("/create")
def create(todo: ToDoPydanticModel):
    ToDoManager.create(todo)
    return {"message": "Successfully!"}


@router.get("/get")
def get():
    return ToDoManager.get()


@router.get("/get_by_id/{task_id}")
def get_by_id(task_id: int):
    if not task_id:
        raise HTTPException(status_code=404, detail="Task with such ID not found")
    return ToDoManager.get_by_id(task_id)


@router.delete("/delete/{task_id}")
def delete_by_id(task_id: int):
    return ToDoManager.delete_by_id(task_id)
    

