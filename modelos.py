from peewee import *
from conexion import database


class user(Model):
    nombre = CharField(max_length=50, unique=True)
    numero = CharField(max_length=50)
    
    def __str__(self):
        return self.nombre
    class Meta:
        database=database
        table_name = 'user'