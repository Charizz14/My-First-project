from fastapi import APIRouter
from app.schemas.user import UserRegister, UserLogin

router = APIRouter(tags=["auth"])


@router.post("/register")
def register(payload: UserRegister):
    return {"token": "replace_me_later"}


@router.post("/login")
def login(payload: UserLogin):
    return {"token": "replace_me_later"}
