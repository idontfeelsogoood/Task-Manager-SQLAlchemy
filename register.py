import string
from sqlalchemy.orm import sessionmaker
import db
from db import *

#new session
Session = sessionmaker(bind=db.engine)
session = Session()

#Counting users to get user_id for new user
def amount_of_users():
    usr_count = 1
    for i in session.query(db.User).all():
        usr_count+=1

    return int(usr_count)

#Creating new User
def create_new_user(new_usr_login, new_usr_password):
    new_usr_id = amount_of_users()
    new_user = db.User(new_usr_id,new_usr_login,new_usr_password)
    session.add(new_user)
    session.commit()

#Secret Function to keep things clean (test)
def clearing_database():
    session.query(db.User).delete()
    session.query(db.Task).delete()
    session.commit()
