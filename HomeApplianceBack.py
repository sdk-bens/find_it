
import pymysql

"""
A function where all process (CRUD) for table home appliance are implemented.
"""


def home_appliance(username, password):
    selected_option = input("you can ADD, DELETE, UPDATE or DISPLAY, choose one: ")
    if selected_option.lower() == "add":
        sn = input("Enter the home appliance serial number: ")
        htype = input("Enter the home appliance type: ")
        brand = input("Enter the home appliance brand: ")
        size = input("Enter the home appliance size: ")
        location = input("Enter the home appliance location: ")
        try:
            cnx = pymysql.connect(host='localhost', user=username, password=password, db='smart_home',
                                  charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
            cur = cnx.cursor()
            cur.execute("INSERT INTO Home_appliance VALUES (%s, %s, %s, %s, %s)", (sn, htype, brand, size, location))
            cnx.commit()
            cnx.close()

        except pymysql.err.OperationalError as e:
            print('Error: %d: %s' % (e.args[0], e.args[1]))

    elif selected_option.lower() == "delete":
        hid = input("Enter the home appliance serial number: ")
        try:
            cnx = pymysql.connect(host='localhost', user=username, password=password, db='smart_home',
                                  charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
            cur = cnx.cursor()
            cur.execute("DELETE FROM Home_appliance WHERE appliance_SN=%s", (hid))
            cnx.commit()
            cnx.close()

        except pymysql.err.OperationalError as e:
            print('Error: %d: %s' % (e.args[0], e.args[1]))

    elif selected_option.lower() == "update":
        sn = input("Enter the home appliance serial number: ")
        htype = input("Enter the home appliance type: ")
        brand = input("Enter the home appliance brand: ")
        size = input("Enter the home appliance size: ")
        location = input("Enter the home appliance location: ")
        try:
            cnx = pymysql.connect(host='localhost', user=username, password=password, db='smart_home',
                                  charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
            cur = cnx.cursor()
            # id should be at the end of the tuple in order to match the row
            cur.execute("UPDATE Home_appliance SET appliance_type = %s, brand = %s, size = %s, location = %s "
                        "WHERE appliance_SN = %s",
                        (htype, brand, size, location, sn))
            cnx.commit()
            cnx.close()

        except pymysql.err.OperationalError as e:
            print('Error: %d: %s' % (e.args[0], e.args[1]))

    elif selected_option.lower() == "display":
        try:
            cnx = pymysql.connect(host='localhost', user=username, password=password, db='smart_home',
                                  charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
            cur = cnx.cursor()
            cur.execute("SELECT * FROM Home_appliance")
            rows = cur.fetchall()
            list1 = []
            for row in rows:
                list1.append(row)
            print("The Home appliance available in the database are: ")
            for i in list1:
                print(i)
            cnx.close()
            return rows

        except pymysql.err.OperationalError as e:
            print('Error: %d: %s' % (e.args[0], e.args[1]))