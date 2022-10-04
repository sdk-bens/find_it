import pymysql

"""
A function where all process (CRUD) for table pet are implemented.
"""


def pet(username, password):
    selected_option = input("you can ADD, DELETE, UPDATE or DISPLAY, choose one: ")
    if selected_option.lower() == "add":
        tag = input("Enter the pet tag: ")
        name = input("Enter the pet name:")
        type = input("Enter the pet type: ")
        size = input("Enter the pet size: ")
        try:
            cnx = pymysql.connect(host='localhost', user=username, password=password, db='smart_home',
                                  charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

            cur = cnx.cursor()
            cur.execute("INSERT INTO Pet VALUES (%s, %s, %s, %s)", (tag, name, type, size))
            cnx.commit()
            cnx.close()

        except pymysql.err.OperationalError as e:
            print('Error: %d: %s' % (e.args[0], e.args[1]))

    elif selected_option.lower() == "delete":
        tag = input("Enter the pet tag: ")
        try:
            cnx = pymysql.connect(host='localhost', user=username, password=password, db='smart_home',
                                  charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

            cur = cnx.cursor()
            cur.execute("DELETE FROM Pet WHERE pet_tag =%s", (tag))
            cnx.commit()
            cnx.close()

        except pymysql.err.OperationalError as e:
            print('Error: %d: %s' % (e.args[0], e.args[1]))

    elif selected_option.lower() == "update":
        tag = input("Enter the pet tag: ")
        name = input("Enter the pet name: ")
        type = input("Enter the pet type: ")
        size = input("Enter the pet size: ")
        try:
            cnx = pymysql.connect(host='localhost', user=username, password=password, db='smart_home',
                                  charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

            cur = cnx.cursor()
            cur.execute("UPDATE Pet SET pet_name = %s, pet_type = %s, pet_size = %s WHERE pet_tag = %s",
                        (name, type, size, tag))
            cnx.commit()
            cnx.close()

        except pymysql.err.OperationalError as e:
            print('Error: %d: %s' % (e.args[0], e.args[1]))

    elif selected_option.lower() == "display":
        try:
            cnx = pymysql.connect(host='localhost', user=username, password=password, db='smart_home',
                                  charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

            cur = cnx.cursor()
            cur.execute("SELECT * FROM Pet")
            rows = cur.fetchall()
            list1 = []
            for row in rows:
                list1.append(row)
            print("The Pets available in the database are: ")
            for i in list1:
                print(i)
            cnx.close()
            return rows

        except pymysql.err.OperationalError as e:
            print('Error: %d: %s' % (e.args[0], e.args[1]))