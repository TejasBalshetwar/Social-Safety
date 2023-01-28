import datetime
import os

import pytz
from flask_login import UserMixin
from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String, create_engine, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker


IST = pytz.timezone('Asia/Kolkata')
Base = declarative_base()
engine = create_engine("sqlite:///database.db")
Session = sessionmaker(bind=engine)
session = Session()


class User(Base, UserMixin):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True,autoincrement=True)
    fname = Column(String(250), nullable=False)
    lname = Column(String(250), nullable=False)
    age = Column(String(250), nullable=False)
    adhar = Column(String(250), nullable=False, unique=True)
    gender = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False, unique=True)
    phno = Column(String(250), nullable=False)
    username = Column(String(250), nullable=False, unique=True)
    password = Column(String(250), nullable=False)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())

    def jso(self):
        return {"name": self.username, "phno": self.phno}


