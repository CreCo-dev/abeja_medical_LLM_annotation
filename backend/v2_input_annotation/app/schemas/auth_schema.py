from pydantic import BaseModel

class TokenResponse(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    sub: str | None = None

class Config:
    from_attributes = True