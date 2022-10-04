
import pymysql

"""
This is a function where all the process of retrieving complex data are implemented.
"""


def data(username, password):

    print(""" in this section there ara many option you can choose from:
                    1- Find a person's devices
                    2- find medicines and which closet, room, floor are located
                    3- Find a person's clothes
                    4- Find if there is medicine for specific sickness/ symptom
                    5- Find what medicine will be expired after a specific date
                    6- Find what pet medicine will be expired after a specific date
                    7- Find clothes of a specific gender and size
                    8- Find what devices will have their warranty expired by a specific date
                    9- Find a person's important item
                    10- Find what furniture are in a specific room
                          """)

    chosen = input("Enter the number of the option you want: ")
    if chosen not in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10"):
        print("This option does not exist, lets do this again:")
    else:
        if chosen == "1":
            person_ID = input("You want to know what devices a person has! Okay, Enter the person's ID: ")
            try:
                cnx = pymysql.connect(host='localhost', user=username, password=password, db='smart_home',
                                      charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
            except pymysql.err.OperationalError as e:
                print('Error: %d: %s' % (e.args[0], e.args[1]))
            try:
                cur = cnx.cursor()
                my_tpl = (person_ID,)
                cur.callproc("person_devices", my_tpl)
                rows = cur.fetchall()
                list1 = []
                for row in rows:
                    list1.append(row)
                for i in list1:
                    print(i)
                cnx.close()
                return rows
            except pymysql.Error as e:
                print('Error: %d: %s' % (e.args[0], e.args[1]))

        elif chosen == "2":
            person_ID = input("You want to know what medicines a person is taking and which closet, room, "
                              "floor are located! Okay, Enter the person's ID: ")
            try:
                cnx = pymysql.connect(host='localhost', user=username, password=password, db='smart_home',
                                      charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
            except pymysql.err.OperationalError as e:
                print('Error: %d: %s' % (e.args[0], e.args[1]))
            try:
                cur = cnx.cursor()
                my_tpl = (person_ID,)
                cur.callproc("person_medicines", my_tpl)
                rows = cur.fetchall()
                list1 = []
                for row in rows:
                    list1.append(row)
                for i in list1:
                    print(i)
                cnx.close()
                return rows
            except pymysql.Error as e:
                print('Error: %d: %s' % (e.args[0], e.args[1]))

        elif chosen == "3":
            person_ID = input("You want to know what clothes a person has! Okay, Enter the person's ID: ")
            try:
                cnx = pymysql.connect(host='localhost', user=username, password=password, db='smart_home',
                                      charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
            except pymysql.err.OperationalError as e:
                print('Error: %d: %s' % (e.args[0], e.args[1]))
            try:
                cur = cnx.cursor()
                my_tpl = (person_ID,)
                cur.callproc("person_clothes", my_tpl)
                rows = cur.fetchall()
                list1 = []
                for row in rows:
                    list1.append(row)
                for i in list1:
                    print(i)
                cnx.close()
                return rows
            except pymysql.Error as e:
                print('Error: %d: %s' % (e.args[0], e.args[1]))

        elif chosen == "4":
            sickness = input("You want to know if there are medicines for specific sickness/ symptoms! "
                             "Okay, Enter a medicine type: ")
            try:
                cnx = pymysql.connect(host='localhost', user=username, password=password, db='smart_home',
                                      charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
            except pymysql.err.OperationalError as e:
                print('Error: %d: %s' % (e.args[0], e.args[1]))
            try:
                cur = cnx.cursor()
                my_tpl = (sickness,)
                cur.callproc("medicine_sickness", my_tpl)
                rows = cur.fetchall()
                list1 = []
                for row in rows:
                    list1.append(row)
                for i in list1:
                    print(i)
                cnx.close()
                return rows
            except pymysql.Error as e:
                print('Error: %d: %s' % (e.args[0], e.args[1]))

        elif chosen == "5":
            exp_date = input("You want to know what medicines will be expired! Okay, Enter a date: ")
            try:
                cnx = pymysql.connect(host='localhost', user=username, password=password, db='smart_home',
                                      charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
            except pymysql.err.OperationalError as e:
                print('Error: %d: %s' % (e.args[0], e.args[1]))
            try:
                cur = cnx.cursor()
                my_tpl = (exp_date,)
                cur.callproc("medicine_exp", my_tpl)
                rows = cur.fetchall()
                list1 = []
                for row in rows:
                    list1.append(row)
                for i in list1:
                    print(i)
                cnx.close()
                return rows
            except pymysql.Error as e:
                print('Error: %d: %s' % (e.args[0], e.args[1]))

        elif chosen == "6":
            exp_date = input("You want to know what pet's medicines will be expired! Okay, Enter a date: ")
            try:
                cnx = pymysql.connect(host='localhost', user=username, password=password, db='smart_home',
                                      charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
            except pymysql.err.OperationalError as e:
                print('Error: %d: %s' % (e.args[0], e.args[1]))
            try:
                cur = cnx.cursor()
                my_tpl = (exp_date,)
                cur.callproc("pet_medicine_exp", my_tpl)
                rows = cur.fetchall()
                list1 = []
                for row in rows:
                    list1.append(row)
                for i in list1:
                    print(i)
                cnx.close()
                return rows
            except pymysql.Error as e:
                print('Error: %d: %s' % (e.args[0], e.args[1]))

        elif chosen == "7":
            print("You want to know what clothes are they with specific gender and size! Okay")
            size = input("Enter a size: ")
            gender = input("Enter a gender: ")
            try:
                cnx = pymysql.connect(host='localhost', user=username, password=password, db='smart_home',
                                      charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
            except pymysql.err.OperationalError as e:
                print('Error: %d: %s' % (e.args[0], e.args[1]))
            try:
                cur = cnx.cursor()
                my_tpl = (size, gender,)
                cur.callproc("clothes_gender_size", my_tpl)
                rows = cur.fetchall()
                list1 = []
                for row in rows:
                    list1.append(row)
                for i in list1:
                    print(i)
                cnx.close()
                return rows
            except pymysql.Error as e:
                print('Error: %d: %s' % (e.args[0], e.args[1]))

        elif chosen == "8":
            exp_warranty = input("You want to know what devices' warranty  will be expired! Okay, Enter a date: ")
            try:
                cnx = pymysql.connect(host='localhost', user=username, password=password, db='smart_home',
                                      charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
            except pymysql.err.OperationalError as e:
                print('Error: %d: %s' % (e.args[0], e.args[1]))
            try:
                cur = cnx.cursor()
                my_tpl = (exp_warranty,)
                cur.callproc("device_warranty", my_tpl)
                rows = cur.fetchall()
                list1 = []
                for row in rows:
                    list1.append(row)
                for i in list1:
                    print(i)
                cnx.close()
                return rows
            except pymysql.Error as e:
                print('Error: %d: %s' % (e.args[0], e.args[1]))

        elif chosen == "9":
            person_ID = input("You want to know what important item a person has! Okay, Enter a person ID: ")
            try:
                cnx = pymysql.connect(host='localhost', user=username, password=password, db='smart_home',
                                      charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
            except pymysql.err.OperationalError as e:
                print('Error: %d: %s' % (e.args[0], e.args[1]))
            try:
                cur = cnx.cursor()
                my_tpl = (person_ID,)
                cur.callproc("person_important_items", my_tpl)
                rows = cur.fetchall()
                list1 = []
                for row in rows:
                    list1.append(row)
                for i in list1:
                    print(i)
                cnx.close()
                return rows
            except pymysql.Error as e:
                print('Error: %d: %s' % (e.args[0], e.args[1]))

        elif chosen == "10":
            room = input("You want to know what furniture are is a specific room! Okay, Enter a room ID: ")
            try:
                cnx = pymysql.connect(host='localhost', user=username, password=password, db='smart_home',
                                      charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
            except pymysql.err.OperationalError as e:
                print('Error: %d: %s' % (e.args[0], e.args[1]))
            try:
                cur = cnx.cursor()
                my_tpl = (room,)
                cur.callproc("room_furniture", my_tpl)
                rows = cur.fetchall()
                list1 = []
                for row in rows:
                    list1.append(row)
                for i in list1:
                    print(i)
                cnx.close()
                return rows
            except pymysql.Error as e:
                print('Error: %d: %s' % (e.args[0], e.args[1]))



