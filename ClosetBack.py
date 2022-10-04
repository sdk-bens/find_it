import pymysql

"""
A function where all process (CRUD) for table closet are implemented.
"""


def closet(username, password):
    selected_option = input("you can ADD, DELETE, UPDATE or DISPLAY, choose one: ")
    if selected_option.lower() == "add":
        cid = input("Enter the closet ID: ")
        ctype = input("Enter the closet type:")
        location = input("Enter the closet location: ")
        try:
            cnx = pymysql.connect(host='localhost', user=username, password=password, db='smart_home',
                                  charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
            cur = cnx.cursor()
            cur.execute("INSERT INTO Closet VALUES (%s, %s, %s)", (cid, ctype, location))
            cnx.commit()
            cnx.close()

        except pymysql.err.OperationalError as e:
            print('Error: %d: %s' % (e.args[0], e.args[1]))

    elif selected_option.lower() == "delete":
        cid = input("Enter the closet ID: ")
        try:
            cnx = pymysql.connect(host='localhost', user=username, password=password, db='smart_home',
                                  charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
            cur = cnx.cursor()
            cur.execute("DELETE FROM Closet WHERE closet_ID =%s", (cid))
            cnx.commit()
            cnx.close()
        except pymysql.err.OperationalError as e:
            print('Error: %d: %s' % (e.args[0], e.args[1]))

    elif selected_option.lower() == "update":
        cid = input("Enter the closet ID: ")
        ctype = input("Enter the closet type:")
        location = input("Enter the closet location: ")
        try:
            cnx = pymysql.connect(host='localhost', user=username, password=password, db='smart_home',
                                  charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
            cur = cnx.cursor()
            cur.execute("UPDATE Closet SET closet_type = %s, location = %s WHERE closet_ID = %s",
                        (ctype, location, cid))
            cnx.commit()
            cnx.close()

        except pymysql.err.OperationalError as e:
            print('Error: %d: %s' % (e.args[0], e.args[1]))

    elif selected_option.lower() == "display":
        try:
            cnx = pymysql.connect(host='localhost', user=username, password=password, db='smart_home',
                                  charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
            cur = cnx.cursor()
            cur.execute("SELECT * FROM Closet")
            rows = cur.fetchall()
            list1 = []
            for row in rows:
                list1.append(row)
            print("The Closets available in the database are: ")
            for i in list1:
                print(i)
            cnx.close()
            return rows

        except pymysql.err.OperationalError as e:
            print('Error: %d: %s' % (e.args[0], e.args[1]))

