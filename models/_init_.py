#!/usr/bin/python3
"""Init module for Filestorage package"""


from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
