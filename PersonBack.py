import pymysql

"""
A function where all process (CRUD) for table person are implemented.
"""


def person(username, password):
    selected_option = input("you can ADD, DELETE, UPDATE or DISPLAY, choose one: ")
    if selected_option.lower() == "add":
        pid = input("Enter the person ID: ")
        name = input("Enter the person name: ")
        gender = input("Enter the person gender: ")
        title = input("Enter the person title: ")
        try:
            cnx = pymysql.connect(host='localhost', user=username, password=password, db='smart_home',
                                  charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
            cur = cnx.cursor()
            cur.execute("INSERT INTO Person VALUES (%s, %s, %s, %s)", (pid, name, gender, title))
            cnx.commit()
            cnx.close()

        except pymysql.err.OperationalError as e:
            print('Error: %d: %s' % (e.args[0], e.args[1]))

    elif selected_option.lower() == "delete":
        pid = input("Enter the person ID: ")
        try:
            cnx = pymysql.connect(host='localhost', user=username, password=password, db='smart_home',
                                  charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
            cur = cnx.cursor()
            cur.execute("DELETE FROM Person WHERE person_ID =%s", pid)
            cnx.commit()
            cnx.close()
            print("You successfully deleted person with ID: {} from the database".format(pid))

        except pymysql.err.OperationalError as e:
            print('Error: %d: %s' % (e.args[0], e.args[1]))
        # PersonBack.delete(id)

    elif selected_option.lower() == "update":
        id = input("Enter the person ID: ")
        name = input("Enter the person name: ")
        gender = input("Enter the person gender: ")
        title = input("Enter the person title: ")

        try:
            cnx = pymysql.connect(host='localhost', user=username, password=password, db='smart_home',
                                  charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
            cur = cnx.cursor()
            cur.execute(
                "UPDATE Person SET  person_name= %s, person_gender = %s,  person_title = %s"
                " WHERE person_ID= %s",
                (name, gender, title, id))
            cnx.commit()
            cnx.close()
        except pymysql.err.OperationalError as e:
            print('Error: %d: %s' % (e.args[0], e.args[1]))

    # elif selected_option.lower() == "search":
    #     pid = input("Enter the person ID: ")
    #     name = input("Enter the person name: ")
    #     gender = input("Enter the person gender: ")
    #     title = input("Enter the person title: ")
    #
    #     try:
    #         cnx = pymysql.connect(host='localhost', user=username, password=password, db='smart_home',
    #                               charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    #         cur = cnx.cursor()
    #         cur.execute("SELECT * FROM Person WHERE person_ID = %s OR person_name= %s OR person_gender= %s "
    #                     "OR person_title= %s "
    #                     , (pid, name, gender, title))
    #         rows = cur.fetchall()
    #         cnx.close()
    #         return rows
    #     except pymysql.err.OperationalError as e:
    #         print('Error: %d: %s' % (e.args[0], e.args[1]))

    elif selected_option.lower() == "display":
        try:
            cnx = pymysql.connect(host='localhost', user=username, password=password, db='smart_home',
                                  charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
            cur = cnx.cursor()
            cur.execute("SELECT * FROM Person")
            rows = cur.fetchall()
            list1 = []
            for row in rows:
                list1.append(row)
            print("The Persons available in the database are: ")
            for i in list1:
                print(i)
            cnx.close()
            return rows
        except pymysql.err.OperationalError as e:
            print('Error: %d: %s' % (e.args[0], e.args[1]))




