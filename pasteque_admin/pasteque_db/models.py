# coding: utf-8

# This models are managed by SQLAlchemy and NOT Django ORM
# This is because of the dynamic nature (e.g per user) of the pasteque databases

from sqlalchemy import Column, Date, DateTime, Float, ForeignKey, Index, Integer, String, Table, Text, text
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql.base import BIT, MEDIUMBLOB
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata

class Application(Base):
    __tablename__ = 'APPLICATIONS'

    id = Column('ID', String(255), primary_key=True)
    name = Column('NAME', String(255), nullable=False)
    version = Column('VERSION', String(255), nullable=False)
