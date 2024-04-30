from src.models import SessionLocal, ToDoModel
from src.schemas import ToDoPydanticModel
from fastapi import HTTPException, status
      
        
class ToDoManager:
    @staticmethod
    def create(todo: ToDoPydanticModel):
        with SessionLocal() as session:
            todo_dict = todo.dict()
            obj = ToDoModel(**todo_dict)
            session.add(obj)
            session.commit()
            return obj
        

    @staticmethod
    def get():
        with SessionLocal() as session:
            return session.query(ToDoModel).all()
        
        
    @staticmethod
    def get_by_id(task_id):
        with SessionLocal() as session:
            return session.query(ToDoModel).filter(ToDoModel.id==task_id).first()
        

    @staticmethod
    def delete_by_id(task_id):
        with SessionLocal() as session:
            obj = session.query(ToDoModel).filter(ToDoModel.id==task_id).first()
            if obj:
                session.delete(obj)
                session.commit()
                return {"message": "This task was deleted successfully"}
            else: 
                raise HTTPException(status_code=404, detail="Task with such ID not found")
            
    

    