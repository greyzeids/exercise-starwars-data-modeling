import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    firstname = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    favourites = relationship('Favourite', backref='user', lazy=True)

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name_id = Column(String(100), nullable=False)
    gender = Column(String(10))
    hair_color = Column(String(30))
    eye_color = Column(String(30))

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name_id = Column(String(100), nullable=False)
    climate = Column(String(50))
    population = Column(Integer)
    terrain = Column(String(50))

class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name_id = Column(String(100), nullable=False)
    model = Column(String(50))
    manufacturer = Column(String(50))
    cost_in_credits = Column(Integer)

class Favourite(Base):
    __tablename__ = 'favourite'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    char_id = Column(Integer, ForeignKey('character.id'), nullable=True)
    planet_id = Column(Integer, ForeignKey('planet.id'), nullable=True)
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'), nullable=True)
    add = Column(String(50))
    delete = Column(String(50))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
