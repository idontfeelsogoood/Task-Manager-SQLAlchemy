import string
from sqlalchemy.orm import sessionmaker
import db
from db import *

#new session
Session = sessionmaker(bind=db.engine)
session = Session()


#Checking if user login and password are correct
def login_user(usr_login,usr_password):
    for i in session.query(db.User).filter(User.user_login == usr_login):
        if(i.user_password == usr_password):
            return True
        else:
            return False

    return False
       