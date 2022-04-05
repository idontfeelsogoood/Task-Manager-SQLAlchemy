from importlib.metadata import metadata
import string
from xmlrpc.client import Boolean
from flask import session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String,Integer
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker




#Create enginge
engine = create_engine('sqlite:///users')

#Create Base 
base = declarative_base()






class User(base):
    __tablename__ = "user_database"
    
    #Table Structure

    user_id = Column(Integer, primary_key = True)
    user_login  = Column(String)
    user_password = Column(String)

    #Constructor

    def __init__(self,user_id,user_login,user_password):

        self.user_id = user_id
        self.user_login = user_login
        self.user_password = user_password




#Task tables
class Task(base):
    __tablename__ = "task_database"

    #Table Structure
    
    taks_id = Column(Integer,primary_key = True)
    task_info = Column(String)
    task_bool = Column(Integer)


    
    #Constructor
    def __init__(self,task_bool,task_info,task_id):

        self.taks_id = task_id
        self.task_info = task_info
        self.task_bool = task_bool





#Create Database
base.metadata.create_all(engine)







