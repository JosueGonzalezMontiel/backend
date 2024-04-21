from pydantic import BaseModel

class UserRequestModel(BaseModel):
    nombre: str
    numero: str
    
class UserResponseModel(UserRequestModel):
    id: int