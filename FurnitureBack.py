
import pymysql

"""
A function where all process (CRUD) for table furniture are implemented.
"""


def furniture(username, password):
    selected_option = input("you can ADD, DELETE, UPDATE or DISPLAY, choose one: ")
    if selected_option.lower() == "add":
        fid = input("Enter the furniture ID: ")
        ftype = input("Enter the furniture type:")
        location = input("Enter the furniture location: ")
        try:
            cnx = pymysql.connect(host='localhost', user=username, password=password, db='smart_home',
                                  charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
            cur = cnx.cursor()
            cur.execute("INSERT INTO Furniture VALUES (%s, %s, %s)", (fid, ftype, location))
            cnx.commit()
            cnx.close()

        except pymysql.err.OperationalError as e:
            print('Error: %d: %s' % (e.args[0], e.args[1]))

    elif selected_option.lower() == "delete":
        fid = input("Enter the furniture ID: ")
        try:
            cnx = pymysql.connect(host='localhost', user=username, password=password, db='smart_home',
                                  charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

            cur = cnx.cursor()
            cur.execute("DELETE FROM Furniture WHERE furniture_ID = %s", fid)
            cnx.commit()
            cnx.close()

        except pymysql.err.OperationalError as e:
            print('Error: %d: %s' % (e.args[0], e.args[1]))

    elif selected_option.lower() == "update":
        fid = input("Enter the furniture ID: ")
        ftype = input("Enter the furniture type:")
        location = input("Enter the furniture location: ")
        try:
            cnx = pymysql.connect(host='localhost', user=username, password=password, db='smart_home',
                                  charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
            cur = cnx.cursor()
            cur.execute("UPDATE Furniture SET furniture_type= %s, location= %s  WHERE furniture_ID= %s",
                        (ftype, location, fid))
            cnx.commit()
            cnx.close()

        except pymysql.err.OperationalError as e:
            print('Error: %d: %s' % (e.args[0], e.args[1]))

    elif selected_option.lower() == "display":
        try:
            cnx = pymysql.connect(host='localhost', user=username, password=password, db='smart_home',
                                  charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

            cur = cnx.cursor()
            cur.execute("SELECT * FROM Furniture")
            rows = cur.fetchall()
            list1 = []
            for row in rows:
                list1.append(row)
            print("The Furniture available in the database are: ")
            for i in list1:
                print(i)
            return rows

        except pymysql.err.OperationalError as e:
            print('Error: %d: %s' % (e.args[0], e.args[1]))
