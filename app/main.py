from app.routes.auth import router as auth_router
from fastapi import FastAPI
app = FastAPI()


@app.get("/")
def root():
    return {"message": "API is running"}


app.include_router(auth_router)
