import psycopg2  #
from flask import Flask, request
from flask_restful import Api
from sqlalchemy import Column, String, Integer, Date, BOOLEAN, and_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
import os
import json

app = Flask(__name__)
api = Api(app)


Base = declarative_base()
database_url = "postgresql://postgres:1234@localhost:5433/postgres"

# disable sqlalchemy pool using NullPool as by default Postgres has its own pool
engine = create_engine(database_url, echo=True, poolclass=NullPool)

Session = sessionmaker(bind=engine)
session = Session()

# original table
class Student_info(Base):
    __tablename__ = 'student_info'
    Name = Column("name", String)
    Age = Column("age", Integer,primary_key=True)
    marks=Column("marks",Integer)
    teacher_name=Column("teacher_name",String)
    school_name=Column("school_name",String)
    std_address=Column("std_address",String)
    date=Column("date",String,)
    Section=Column("section",String)
    Mobile=Column("mobile",Integer)
    IsNewStudent=Column("is_new_student",String)


class class_info(Base):
    __tablename__ = 'class_info'
    Name = Column("name", String)
    Age = Column("age", Integer,primary_key=True)
    marks=Column("marks",Integer)
    teacher_name=Column("teacher_name",String)
    school_name=Column("school_name",String)
    std_address=Column("std_address",String)
    date=Column("date",String,)
    Section=Column("section",String)
    Mobile=Column("mobile",Integer)
    IsOldStudent=Column("is_old_student",String)


    
