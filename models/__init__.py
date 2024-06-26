#!/usr/bin/python3
"""__init__"""


from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()

classes = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]
