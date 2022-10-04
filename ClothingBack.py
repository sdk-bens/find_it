
import pymysql

"""
A function where all process (CRUD) for table clothing are implemented.
"""


def clothing(username, password):
    selected_option = input("you can ADD, DELETE, UPDATE or DISPLAY, choose one: ")
    if selected_option.lower() == "add":
        clid = input("Enter the clothing ID: ")
        cltype = input("Enter the clothing type: ")
        gender = input("Enter the clothing gender: ")
        color = input("Enter the clothing color: ")
        size = input("Enter the clothing size: ")
        owner = input("Enter the clothing owner: ")
        location = input("Enter the clothing location: ")
        try:
            cnx = pymysql.connect(host='localhost', user=username, password=password, db='smart_home',
                                  charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
            cur = cnx.cursor()
            cur.execute("INSERT INTO Clothing VALUES (%s, %s, %s, %s, %s, %s, %s)", (clid, cltype, gender, color, size,
                                                                                     owner, location))
            cnx.commit()
            cnx.close()
        except pymysql.err.OperationalError as e:
            print('Error: %d: %s' % (e.args[0], e.args[1]))

    elif selected_option.lower() == "delete":
        cid = input("Enter the clothing ID: ")
        try:
            cnx = pymysql.connect(host='localhost', user=username, password=password, db='smart_home',
                                  charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
            cur = cnx.cursor()
            cur.execute("DELETE FROM Clothing WHERE clothing_ID=%s", (cid))
            cnx.commit()
            cnx.close()

        except pymysql.err.OperationalError as e:
            print('Error: %d: %s' % (e.args[0], e.args[1]))

    elif selected_option.lower() == "update":
        clid = input("Enter the clothing ID: ")
        cltype = input("Enter the clothing type: ")
        gender = input("Enter the clothing gender: ")
        color = input("Enter the clothing color: ")
        size = input("Enter the clothing size: ")
        owner = input("Enter the clothing owner: ")
        location = input("Enter the clothing location: ")
        try:
            cnx = pymysql.connect(host='localhost', user=username, password=password, db='smart_home',
                                  charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
            cur = cnx.cursor()
            cur.execute(
                "UPDATE Clothing SET clothing_type= %s, clothing_gender= %s, clothing_color= %s, clothing_size= %s, "
                "clothing_owner= %s, location = %s WHERE clothing_ID = %s",
                (cltype, gender, color, size, owner, location, clid))
            cnx.commit()
            cnx.close()
        except pymysql.err.OperationalError as e:
            print('Error: %d: %s' % (e.args[0], e.args[1]))

    elif selected_option.lower() == "display":
        try:
            cnx = pymysql.connect(host='localhost', user=username, password=password, db='smart_home',
                                  charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

            cur = cnx.cursor()
            cur.execute("SELECT * FROM Clothing")
            rows = cur.fetchall()
            list1 = []

            for row in rows:
                list1.append(row)
            print("The clothing available in the database are: ")
            for i in list1:
                print(i)
            cnx.close()
            return rows

        except pymysql.err.OperationalError as e:
            print('Error: %d: %s' % (e.args[0], e.args[1]))