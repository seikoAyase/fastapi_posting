from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str

class UserRespone(BaseModel):
    id: int
    username: str

    class config:
        from_attributes = True

    