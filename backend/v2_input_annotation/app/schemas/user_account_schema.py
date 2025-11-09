from pydantic import BaseModel, ConfigDict

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

    model_config = ConfigDict(from_attributes=True)