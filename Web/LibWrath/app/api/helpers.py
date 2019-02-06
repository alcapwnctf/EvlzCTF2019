import os
from base64 import b64decode, b64encode
import hashlib

SALT_LENGTH = 4
SALT = os.getenv('HASH_SALT')[:SALT_LENGTH] or 'DEFAULT_SALT'


def DefaultUUID():
        return b64encode(hasher.update(SALT).digest())

def GenerateUUID(username):
        hasher = hashlib.sha256()
        hasher.update(SALT.encode()+username.encode())
        return b64encode(hasher.digest()).decode()
