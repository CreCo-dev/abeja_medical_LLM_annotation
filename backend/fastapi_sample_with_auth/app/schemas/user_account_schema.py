from pydantic import BaseModel

class UserAccountCreate(BaseModel):
    login_id: str
    password: str
    name: str

class UserAccountUpdate(BaseModel):
    login_id: str
    password: str
    name: str

class UserAccount(BaseModel):
    id: int
    login_id: str
    name: str

    class Config:
        orm_mode = True
