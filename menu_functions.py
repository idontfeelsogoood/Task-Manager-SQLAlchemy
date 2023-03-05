from gettext import bind_textdomain_codeset
from select import select
import string
from click import edit
from pip import main
from sqlalchemy.orm import sessionmaker
import db
from db import *

#new session
Session = sessionmaker(bind=db.engine)
session = Session()

#Adding tasks to database
def adding_task(bool_user,task_information):
    task_counter = get_task_id()
    
    task = Task(bool_user,task_information,task_counter,)
    session.add(task)
    session.commit()

#Getting user id from database
def get_user_id(login_user):
    for i in session.query(db.User).filter(db.User.user_login == login_user):
        return i.user_id

#showing current tasks based of user_id
def showing_tasks(id_user):
    
    for  i in (session.query(db.Task).filter(db.Task.task_bool == id_user)):
        print(i.taks_id,i.task_info)
    print("\n")
        

#getting task id (Used to showing_tasks() to filter tasks for each user)
def get_task_id():
    counter = 1
    for i in session.query(db.Task).all():
        counter+=1
    return counter

#EDIT Task
def edit_task(task_id):
    for i in session.query(db.Task).filter(db.Task.taks_id == task_id):
        print("\n")
        print(i.taks_id,i.task_info)

        edited_task = str(input("Enter new Task Information: "))
        i.task_info = edited_task

#DELETE Task
def delete_task(task_id):
    obj = session.query(db.Task).filter(db.Task.taks_id == task_id)
    session.delete(obj)                                                             #jak usunac Rekord o podanym id?????
    session.commit()     
        

def show_logging_menu():
    print("(1) Login")
    print("(2) Register new user")
    print("(3) Exit")
    print("(9) Clear Database (TEST)")


def show_menu():
    print("(1) Add Task")
    print("(2) Edit Task")
    print("(3) Delete Task")
    print("(4) Log out ")
    print("(5) Exit")



