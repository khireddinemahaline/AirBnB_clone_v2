#!/usr/bin/python3
"""__init__"""


import os


hbnb_type_storage = os.getenv("HBNB_TYPE_STORAGE")

if hbnb_type_storage == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()

classes = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]
