from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_info():
    return {"Message": "This is your the first todo list app!"}