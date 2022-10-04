import pymysql

"""
A function where all process (CRUD) for table pet medicine are implemented.
"""


def pet_med(username, password):
    selected_option = input("you can ADD, DELETE, UPDATE or DISPLAY, choose one: ")
    if selected_option.lower() == "add":
        pmid = input("Enter the pet medicine ID: ")
        med_type = input("Enter the type of the medicine: ")
        exp = input("What is the expiration date of this medicine: ")
        pet_type = input("What type of pet can take this medicine?: ")
        size = input("What size of pet is required for this medicine?: ")
        owner = input("Who is taking this medicine (pet)?: ")
        location = input("Enter the location of the medicine: ")
        try:
            cnx = pymysql.connect(host='localhost', user=username, password=password, db='smart_home',
                                  charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
            cur = cnx.cursor()
            cur.execute("INSERT INTO Pet_medicine VALUES (%s, %s, %s, %s, %s, %s, %s)", (pmid, med_type, exp, pet_type,
                                                                                         size, owner, location))
            cnx.commit()
            cnx.close()
        except pymysql.err.OperationalError as e:
            print('Error: %d: %s' % (e.args[0], e.args[1]))

    elif selected_option.lower() == "delete":
        pmid = input("Enter the pet medicine ID: ")
        try:
            cnx = pymysql.connect(host='localhost', user=username, password=password, db='smart_home',
                                  charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
            cur = cnx.cursor()
            cur.execute("DELETE FROM Pet_medicine WHERE pet_medicine_ID =%s", pmid)
            cnx.commit()
            cnx.close()

        except pymysql.err.OperationalError as e:
            print('Error: %d: %s' % (e.args[0], e.args[1]))

    elif selected_option.lower() == "update":
        pmid = input("Enter the pet medicine ID: ")
        med_type = input("Enter the type of the medicine: ")
        exp = input("What is the expiration date of this medicine: ")
        pet_type = input("What type of pet can take this medicine?: ")
        size = input("What size of pet is required for this medicine?: ")
        owner = input("Who is taking this medicine (pet)?: ")
        location = input("Enter the location of the medicine: ")
        try:
            cnx = pymysql.connect(host='localhost', user=username, password=password, db='smart_home',
                                  charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
            cur = cnx.cursor()
            cur.execute("UPDATE Pet_medicine SET pet_medicine_type = %s, expiration_date = %s, pet_type = %s,"
                        "good_for_size = %s, p_owner = %s, location = %s WHERE pet_medicine_ID = %s",
                        (med_type, exp, pet_type, size, owner, location, pmid))
            cnx.commit()
            cnx.close()
        except pymysql.err.OperationalError as e:
            print('Error: %d: %s' % (e.args[0], e.args[1]))

    elif selected_option.lower() == "display":
        try:
            cnx = pymysql.connect(host='localhost', user=username, password=password, db='smart_home',
                                  charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
            cur = cnx.cursor()
            cur.execute("SELECT * FROM Pet_medicine")
            rows = cur.fetchall()
            list1 = []
            for row in rows:
                list1.append(row)
            print("The pet medicines available in the database are: ")
            for i in list1:
                print(i)
            cnx.close()
            return rows

        except pymysql.err.OperationalError as e:
            print('Error: %d: %s' % (e.args[0], e.args[1]))