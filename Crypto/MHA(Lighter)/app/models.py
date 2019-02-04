import uuid
import datetime
from functools import reduce
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from database import Base
from sqlalchemy.orm import backref

class User(Base):
    __tablename__ = 'users'
    username = Column(String(50), primary_key=True, unique=True)
    password = Column(String(50))
    admin = Column(Boolean, default=False)
    
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User {}>'.format(self.username)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.username)
    

