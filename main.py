from multiprocessing.sharedctypes import Value

from pip import main
from menu_functions import *
from db import *
import db
import login
import register
import os



os.system("cls")

main_menu_flag = True
logged_menu_flag = True

while main_menu_flag:
    os.system("cls")
    

    show_logging_menu()

    try:
        #unlogged user menu option
        UNLOG_user_option = int(input("Option: "))

    except ValueError:
        print("\nWrong Input Choose option from menu\n".title())



    
    ########    USER LOGIN      #########

    if(UNLOG_user_option == 1):
        #Default user status
        logged = False

        #User input Login and Password
        UNLOG_user_login = str(input("\nEnter Login: "))
        UNLOG_user_password =  str(input("Enter Password: "))

        #Logging user
        logged = login.login_user(UNLOG_user_login,UNLOG_user_password)


        #If user input Correct login and password
        if(logged):
            os.system("cls")
            
            
            #Logged menu
            while (logged_menu_flag):
                user_id_task = get_user_id(UNLOG_user_login)
                os.system("cls")
                print("\nLogged as {} \n".format(UNLOG_user_login))
                

                #Showing Current Tasks of user
                showing_tasks(user_id_task)
                
                #Showing Option Menu of user
                show_menu()
                
                try:
                    #Logged user menu option
                    LOG_user_option = int(input("Option: "))
                
                except ValueError:
                    print("\nWrong Input Choose option from menu\n".title())
                

                ####### ADDING TASK ############
                if(LOG_user_option == 1):
                    print("\nLogged as {} \n".format(UNLOG_user_login))
                    user_task = str(input("\nTask: "))
                    adding_task(user_id_task,user_task)
                
                ########## EDIT TASK  ###########
                elif(LOG_user_option == 2):
                    edit_task_id = int(input("Enter task id: "))
                    edit_task(edit_task_id)
                
                ####### DELETE TASK ##########
                elif (LOG_user_option == 3):
                    print("\nBETA TESTING OPTION UNAVIABLE")
                    #print("\n")
                    #deleted_task = int(input("Enter id to delete: ")) 
                    #delete_task(deleted_task)

                    
                    
                    

                    
                    
                    
                
                    
                

                ########    LOGOUT  ###########
                elif(LOG_user_option == 4):
                    os.system("cls")
                    break
                    
                

                ######## LOGGED EXIT ###########
                elif(LOG_user_option == 5):
                    print("\nLeaving Entire Program\n")
                    logged_menu_flag = False
                    main_menu_flag = False
        
        #If user input WRONG login or password
        else:
            os.system("cls")
            print("\nWrong login Or Password\n".title())



#########   USER REGISTER       #############
    
    elif (UNLOG_user_option == 2):

        #New user REGister login and Password
        REG_user_login = str(input("\nEnter new login: "))
        REG_user_password = str(input("Enter new Password: "))

        #registering user
        register.create_new_user(REG_user_login,REG_user_password)
        os.system("cls")
        print("\nUser Register Successfull\n")


##########   EXIT    ###############

    elif (UNLOG_user_option == 3):
        main_menu_flag = False
        os.system('cls')
        print("\nLeaving Entire Program\n")

    


    #SECRET OPTION TO CLEAR DATABASE (!!!TESTS!!!)
    elif(UNLOG_user_option == 9):
        register.clearing_database()
        os.system('cls')
        print("\nCLEARING DATABASE SUCESSFULL \n")





            


