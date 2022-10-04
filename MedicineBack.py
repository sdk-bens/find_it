import pymysql

"""
A function where all process (CRUD) for table medicine are implemented.
"""

def medicine(username, password):
    selected_option = input("you can ADD, DELETE, UPDATE or DISPLAY, choose one: ")
    if selected_option.lower() == "add":
        mid = input("Enter the medicine ID: ")
        name = input("Enter the medicine name: ")
        type = input("Enter the medicine type: ")
        owner = input("Enter the medicine owner: ")
        prescription = input("does the medicine require prescription? Y/N: ")
        exp = input("Enter the medicine expiration date: ")
        location = input("Enter the medicine location: ")
        try:
            cnx = pymysql.connect(host='localhost', user=username, password=password, db='smart_home',
                                  charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
            cur = cnx.cursor()
            cur.execute("INSERT INTO Medicine VALUES (%s, %s, %s, %s, %s, %s, %s)", (mid, name, type, owner,
                                                                                     prescription, exp, location))
            cnx.commit()
            cnx.close()

        except pymysql.err.OperationalError as e:
            print('Error: %d: %s' % (e.args[0], e.args[1]))

    elif selected_option.lower() == "delete":
        mid = input("Enter the medicine ID: ")
        try:
            cnx = pymysql.connect(host='localhost', user=username, password=password, db='smart_home',
                                  charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
            cur = cnx.cursor()
            cur.execute("DELETE FROM Medicine WHERE medicine_ID=%s", mid)
            cnx.commit()
            cnx.close()
        except pymysql.err.OperationalError as e:
            print('Error: %d: %s' % (e.args[0], e.args[1]))

    elif selected_option.lower() == "update":
        mid = input("Enter the medicine ID: ")
        name = input("Enter the medicine name: ")
        type = input("Enter the medicine type: ")
        owner = input("Enter the medicine owner: ")
        prescription = input("does the medicine require prescription? Y/N: ")
        exp = input("Enter the medicine expiration date: ")
        location = input("Enter the medicine location: ")
        try:
            cnx = pymysql.connect(host='localhost', user=username, password=password, db='smart_home',
                                  charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
            cur = cnx.cursor()
            cur.execute("UPDATE Medicine SET medicine_name = %s, medicine_type = %s, medicine_owner = %s,"
                        " prescription = %s, expiration_date = %s, location = %s WHERE medicine_ID = %s",
                        (name, type, owner, prescription, exp, location, mid))
            cnx.commit()
            cnx.close()
        except pymysql.err.OperationalError as e:
            print('Error: %d: %s' % (e.args[0], e.args[1]))

    elif selected_option.lower() == "display":
        try:
            cnx = pymysql.connect(host='localhost', user=username, password=password, db='smart_home',
                                  charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
            cur = cnx.cursor()
            cur.execute("SELECT * FROM Medicine")
            rows = cur.fetchall()
            list1 = []
            for row in rows:
                list1.append(row)
            print("The Medicines available in the database are: ")
            for i in list1:
                print(i)
            cnx.close()
            return rows
        except pymysql.err.OperationalError as e:
            print('Error: %d: %s' % (e.args[0], e.args[1]))