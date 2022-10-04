import pymysql

"""
A function where all process (CRUD) for table pet item are implemented.
"""


def pet_item(username, password):
    selected_option = input("you can ADD, DELETE, UPDATE or DISPLAY, choose one: ")
    if selected_option.lower() == "add":
        piid = input("Enter the pet item ID: ")
        pitype = input("Enter the pet item type: ")
        used_for = input("what type of pet use this item: ")
        owner = input("which pet own this item: ")
        try:
            cnx = pymysql.connect(host='localhost', user=username, password=password, db='smart_home',
                                  charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
            cur = cnx.cursor()
            cur.execute("INSERT INTO Pet_item VALUES (%s, %s, %s, %s)", (piid, pitype, used_for, owner))
            cnx.commit()
            cnx.close()

        except pymysql.err.OperationalError as e:
            print('Error: %d: %s' % (e.args[0], e.args[1]))

    elif selected_option.lower() == "delete":
        piid = input("Enter the pet item ID: ")
        try:
            cnx = pymysql.connect(host='localhost', user=username, password=password, db='smart_home',
                                  charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
            cur = cnx.cursor()
            cur.execute("DELETE FROM Pet_item WHERE pet_item_ID =%s", (piid))
            cnx.commit()
            cnx.close()

        except pymysql.err.OperationalError as e:
            print('Error: %d: %s' % (e.args[0], e.args[1]))

    elif selected_option.lower() == "update":
        piid = input("Enter the pet item ID: ")
        pitype = input("Enter the pet item type: ")
        used_for = input("what type of pet use this item: ")
        owner = input("which pet own this item: ")
        try:
            cnx = pymysql.connect(host='localhost', user=username, password=password, db='smart_home',
                                  charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

            cur = cnx.cursor()
            cur.execute("UPDATE Pet_item SET pet_item_type = %s, used_for = %s, p_owner = %s WHERE pet_item_ID = %s",
                        (pitype, used_for, owner, piid))
            cnx.commit()
            cnx.close()

        except pymysql.err.OperationalError as e:
            print('Error: %d: %s' % (e.args[0], e.args[1]))

    elif selected_option.lower() == "display":
        try:
            cnx = pymysql.connect(host='localhost', user=username, password=password, db='smart_home',
                                  charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

            cur = cnx.cursor()
            cur.execute("SELECT * FROM Pet_item")
            rows = cur.fetchall()
            list1 = []
            for row in rows:
                list1.append(row)
            print("The pet items available in the database are: ")
            for i in list1:
                print(i)
            cnx.close()
            return rows

        except pymysql.err.OperationalError as e:
            print('Error: %d: %s' % (e.args[0], e.args[1]))


