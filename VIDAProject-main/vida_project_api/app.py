from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import select


from vida_project_api.models import User
from vida_project_api.schemas import UserResponseSchema, UserSchema
from vida_project_api.settings import Settings
from vida_project_api.database import get_session



app = FastAPI()


@app.get("/")
def hello_world():
    return {"message": "Hello, World!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/users", status_code=201, response_model=UserResponseSchema)
def create_user(user: UserSchema, session=Depends(get_session)):
    existing_user = session.scalar(select(User).where((User.username == user.username) | (User.email == user.email)))
    if existing_user:
        if existing_user.username == user.username:
            raise HTTPException(status_code=409, detail="Username already exists")
        elif existing_user.email == user.email:
            raise HTTPException(status_code=409, detail="Email already exists")

    new_user = User(username=user.username, email=user.email, voice=user.voice)
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return new_user