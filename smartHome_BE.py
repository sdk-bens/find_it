import pymysql
import Crud
import Data
import sys

print("##################################################")
print("Welcome to the application!")
print("Enter the credentials to gain access to the database")
print("WARNING: you are only allowed once to enter a correct username and password, otherwise you will have to re "
      "open the application")
username = input("Enter the username: ")
password = input("Enter the password: ")

"""
This function is where our back end get connected to the front end
"""


def smart_home():
    #
    # error = "Access denied for user 'gg'@'localhost' (using password: YES)"

    try:

        cnx = pymysql.connect(host='localhost', user=username, password=password, db='smart_home',
                              charset='utf8mb4')
        check = True
        while check:
            print("##################################################")
            print("There are different options you can choose from.")
            print("1- CRUD: this option will help you add, update, READ or delete data from the database.")
            print("2- DATA: this option will help you retrieve specific DATA.")
            choice = input("Enter << 1 or CRUD >> OR Enter << 2 or DATA >> or < exit > to quit: ")

            if choice.lower() == "exit":
                print("Good bye!")
                sys.exit()
            if choice == "1" or choice == "2" or choice.lower() == "crud" or choice.lower() == "data":
                if choice.lower() == "data" or choice == "2":
                    Data.data(username, password)

                elif choice.lower() == "crud" or choice == "1":
                    Crud.crud(username, password)

            else:
                print("you entered a wrong choice, lets do this again:")

            print("##################################################")
            print("Do you want to keep working on the DB?")
            check = input("Enter any word to continue using the application OR Enter < exit > to quit: ")
            if check.lower == "yes":
                check = True
            elif check.lower() == "exit":
                print("Good bye!")
                sys.exit()
        else:

            cnx.close()

    except pymysql.err.OperationalError as e:
        print('Error: %d: %s' % (e.args[0], e.args[1]))
        print("""
        You entered a wrong username or password, this database has sensitive information
         and you are only given one chance to enter the correct credentials.
         please re run the application again!
        """)

    finally:
        cnx.close()


