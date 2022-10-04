import pymysql

"""
A function where all process (CRUD) for table room are implemented.
"""


def room(username, password):
    selected_option = input("you can ADD, DELETE, UPDATE or DISPLAY, choose one: ")
    if selected_option.lower() == "add":
        rid = input("Enter the room ID: ")
        rtype = input("Enter the room type:")
        rname = input("Enter the room name:")
        location = input("Enter the room location: ")
        ac = input("Does the room have an AC?: ")
        try:
            cnx = pymysql.connect(host='localhost', user=username, password=password, db='smart_home',
                                  charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
            cur = cnx.cursor()
            cur.execute("INSERT INTO Room VALUES (%s, %s, %s, %s, %s)", (rid, rtype, rname, location, ac))
            cnx.commit()
            cnx.close()

        except pymysql.err.OperationalError as e:
            print('Error: %d: %s' % (e.args[0], e.args[1]))

    elif selected_option.lower() == "delete":
        rid = input("Enter the room ID: ")
        try:
            cnx = pymysql.connect(host='localhost', user=username, password=password, db='smart_home',
                                  charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
            cur = cnx.cursor()
            cur.execute("DELETE FROM Room WHERE room_ID =%s", (rid))
            cnx.commit()
            cnx.close()
        except pymysql.err.OperationalError as e:
            print('Error: %d: %s' % (e.args[0], e.args[1]))

    elif selected_option.lower() == "update":
        rid = input("Enter the room ID: ")
        rtype = input("Enter the room type: ")
        rname = input("Enter the room name: ")
        location = input("Enter the room location: ")
        ac = input("Does the room have an AC?: ")
        try:
            cnx = pymysql.connect(host='localhost', user=username, password=password, db='smart_home',
                                  charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

            cur = cnx.cursor()
            cur.execute("UPDATE Room SET room_type = %s, room_name = %s, location = %s, has_AC = %s WHERE room_ID = %s",
                        (rtype, rname, location, ac, rid))
            cnx.commit()
            cnx.close()
        except pymysql.err.OperationalError as e:
            print('Error: %d: %s' % (e.args[0], e.args[1]))

    elif selected_option.lower() == "display":
        try:
            cnx = pymysql.connect(host='localhost', user=username, password=password, db='smart_home',
                                  charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
            cur = cnx.cursor()
            cur.execute("SELECT * FROM Room")
            rows = cur.fetchall()
            list1 = []
            for row in rows:
                list1.append(row)
            print("The rooms available in the database are: ")
            for i in list1:
                print(i)
            cnx.close()
            return rows

        except pymysql.err.OperationalError as e:
            print('Error: %d: %s' % (e.args[0], e.args[1]))