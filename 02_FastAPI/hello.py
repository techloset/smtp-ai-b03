from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    name: str
    age:  int
    height: float
    weight: float
    email: str

@app.get("/")
def get_root():
    return {"message": "Hello Ali, Howu are you?"}


@app.get("/items/{item_id}")
def get_item(item_id: int, age: int, height: Optional[float] = None):
    return {"item_id": item_id, "age": age, "height": height}

@app.post("/create_user")
def create_user(user: User):
    return {"user_name": user.name, "user_age": user.ageuu, "user_email": user.email,  "user_height": user.height, "user_weight": user.weight}