
import pymysql

"""
A function where all process (CRUD) for table important item are implemented.
"""


def important(username, password):
    selected_option = input("you can ADD, DELETE, UPDATE or DISPLAY, choose one: ")
    if selected_option.lower() == "add":
        iid = input("Enter the important item ID: ")
        type = input("Enter the important item type: ")
        value = input("Enter the important item gender: ")
        owner = input("Enter the important item owner: ")
        location = input("Enter the important item location: ")
        try:
            cnx = pymysql.connect(host='localhost', user=username, password=password, db='smart_home',
                                  charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
            cur = cnx.cursor()
            cur.execute("INSERT INTO Important_item VALUES (%s, %s, %s, %s, %s)", (iid, type, value, owner, location))
            cnx.commit()
            cnx.close()

        except pymysql.err.OperationalError as e:
            print('Error: %d: %s' % (e.args[0], e.args[1]))

    elif selected_option.lower() == "delete":
        iid = input("Enter the important item ID: ")
        try:
            cnx = pymysql.connect(host='localhost', user=username, password=password, db='smart_home',
                                  charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
            cur = cnx.cursor()
            cur.execute("DELETE FROM Important_item WHERE important_item_ID=%s", (iid))
            cnx.commit()
            cnx.close()

        except pymysql.err.OperationalError as e:
            print('Error: %d: %s' % (e.args[0], e.args[1]))

    elif selected_option.lower() == "update":
        iid = input("Enter the important item ID: ")
        type = input("Enter the important item type: ")
        value = input("Enter the important item gender: ")
        owner = input("Enter the important item owner: ")
        location = input("Enter the clothing location: ")
        try:
            cnx = pymysql.connect(host='localhost', user=username, password=password, db='smart_home',
                                  charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

            cur = cnx.cursor()
            cur.execute(
                "UPDATE Important_item SET important_item_type = %s, important_item_value = %s, "
                "important_item_owner = %s, location = %s "
                "WHERE important_item_ID = %s",
                (type, value, owner, location, iid))
            cnx.commit()
            cnx.close()

        except pymysql.err.OperationalError as e:
            print('Error: %d: %s' % (e.args[0], e.args[1]))

    elif selected_option.lower() == "display":
        try:
            cnx = pymysql.connect(host='localhost', user=username, password=password, db='smart_home',
                                  charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
            cur = cnx.cursor()
            cur.execute("SELECT * FROM Important_item")
            rows = cur.fetchall()
            list1 = []
            for row in rows:
                list1.append(row)
            print("The Important items available in the database are: ")
            for i in list1:
                print(i)
            cnx.close()
            return rows

        except pymysql.err.OperationalError as e:
            print('Error: %d: %s' % (e.args[0], e.args[1]))