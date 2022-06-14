from pydantic import BaseModel
from typing import List, Union

class thisbase(BaseModel):
    title: str
    body: str
    user_id: int

class User(BaseModel):
    name: str
    email: str
    password: str
    Tel: int


class this(thisbase):


    class Config():
        orm_mode = True

class ShowUser(BaseModel):
    name: str
    email: str
    Tel: int
    blog: List[this] = []

    class Config():
        orm_mode = True


class showthis(BaseModel):
    title:str
    body:str
    creator: ShowUser

    # when calling with db and query always use orm
    class Config():
        orm_mode = True


class Login (BaseModel):
    username: str
    password :str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Union[str, None] = None


