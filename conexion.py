from peewee import *

database= MySQLDatabase(
    'infoapi',
    user='root', password='',
    host='localhost', port=3306
)