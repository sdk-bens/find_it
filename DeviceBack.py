
import pymysql

"""
A function where all process (CRUD) for table device are implemented.
"""


def device(username, password):
    selected_option = input("you can ADD, DELETE, UPDATE or DISPLAY, choose one: ")
    if selected_option.lower() == "add":
        sn = input("Enter the device serial number: ")
        dtype = input("Enter the device type: ")
        brand = input("Enter the device brand: ")
        warranty = input("Enter the device warranty: ")
        owner = input("Enter the device owner: ")
        try:
            cnx = pymysql.connect(host='localhost', user=username, password=password, db='smart_home',
                                  charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

            cur = cnx.cursor()
            cur.execute("INSERT INTO Device VALUES (%s, %s, %s, %s, %s)",
                        (sn, dtype, brand, warranty, owner))
            cnx.commit()
            cnx.close()

        except pymysql.err.OperationalError as e:
            print('Error: %d: %s' % (e.args[0], e.args[1]))

    elif selected_option.lower() == "delete":
        sn = input("Enter the device serial number: ")
        try:
            cnx = pymysql.connect(host='localhost', user=username, password=password, db='smart_home',
                                  charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

            cur = cnx.cursor()
            cur.execute("DELETE FROM Device WHERE device_SN=%s", sn)
            cnx.commit()
            cnx.close()

        except pymysql.err.OperationalError as e:
            print('Error: %d: %s' % (e.args[0], e.args[1]))

    elif selected_option.lower() == "update":
        sn = input("Enter the device serial number: ")
        dtype = input("Enter the device type: ")
        brand = input("Enter the device brand: ")
        warranty = input("Enter the device warranty: ")
        owner = input("Enter the device owner: ")
        try:
            cnx = pymysql.connect(host='localhost', user=username, password=password, db='smart_home',
                                  charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

            cur = cnx.cursor()
            cur.execute("UPDATE Device SET device_type= %s, brand = %s, warranty_expiration = %s, device_owner = %s"
                        " WHERE device_SN = %s",
                        (dtype, brand, warranty, owner, sn))
            cnx.commit()
            cnx.close()

        except pymysql.err.OperationalError as e:
            print('Error: %d: %s' % (e.args[0], e.args[1]))

    elif selected_option.lower() == "display":
        try:
            cnx = pymysql.connect(host='localhost', user=username, password=password, db='smart_home',
                                  charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

            cur = cnx.cursor()
            cur.execute("SELECT * FROM Device")
            cnx.commit()
            rows = cur.fetchall()
            list1 = []

            for row in rows:
                list1.append(row)
            print("The Devices available in the database are: ")
            for i in list1:
                print(i)
            cnx.close()
            return rows

        except pymysql.err.OperationalError as e:
            print('Error: %d: %s' % (e.args[0], e.args[1]))