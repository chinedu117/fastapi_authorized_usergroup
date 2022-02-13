from tokenize import group
from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel

class User(BaseModel):
    username:str
    groups: set[str]


users = [
     User(username="chinedu117", groups=('admin')),
     User(username="emekaE", groups=("student"))
]

app = FastAPI()

# define the middle ware (dependency) 
# It should throw an exception if the user doesnt belong 
# to the group required by the route


class AuthorizedUser:

    def __init__(self, authorized_groups: set[str]) -> None:
        self.authorized_groups = authorized_groups
    
    # def __call__(self, user = Depends(get_current_user)):
    def __call__(self, username: str):
        # resolve the authorization header 
        # fetch the user based on the authorisation header 
        