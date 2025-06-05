from pydantic import BaseModel, EmailStr

class Usuario(BaseModel):
    nombre: str
    correo: EmailStr
    edad: int
