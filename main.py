from fastapi import FastAPI
from conexion import database as connection
from modelos import user
from limitaciones import UserRequestModel
from limitaciones import UserResponseModel
from fastapi import HTTPException

app = FastAPI(title='api ccc    ',
              description='api para maneacion de archivos',#aqui se nombra y crea la app que vas a subir en el servidor 
              version='1.1')#tambien se ocupa el nombre de este archivo 



@app.on_event('startup')
async def startup_event():
    if connection.is_closed():
        connection.connect()#con esto se crean tablas 
        connection.create_tables([user])

@app.on_event('shutdown')
def shutdown_event():
    if not connection.is_closed():
        connection.close()


@app.get('/')
async def index():
    return 'hola dfrr'

@app.post('/user')
async def create_user(user_request: UserRequestModel):
    new_user =user.create(
        nombre=user_request.nombre,
        numero=user_request.numero
    )
    return user_request

@app.get('/user/{user_id}')
async def get_user(user_id, page: int= 0, limit:int=0):
    get_nombre=user.select().where(user.id == user_id).first()
    if get_nombre:
        return UserResponseModel(id=get_nombre.id, nombre=get_nombre.nombre, numero=get_nombre.numero)
    else:
        return HTTPException(404, 'no encontrado')
    
@app.put('/user/{user_id}')
async def update_user(user_id: int, user_request: UserRequestModel):
    updated_user = user.select().where(user.id == user_id).first()
    if updated_user:
        updated_user.nombre = user_request.nombre
        updated_user.numero = user_request.numero
        updated_user.save()  # Guardar los cambios en la base de datos
        return {"message": "Usuario actualizado correctamente"}
    else:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

@app.delete('/user/{user_id}')
async def delete_user(user_id):
    delete_nombre=user.select().where(user.id == user_id).first()
    if delete_nombre:
        delete_nombre.delete_instance()
        return True
    else:
        return HTTPException(404, 'no encontrado')    