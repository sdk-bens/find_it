-- *************************************************************
-- This script creates the databases find_it
-- 
-- *************************************************************

-- ********************************************
-- CREATE THE smart_home DATABASE
-- *******************************************

-- create the database
DROP DATABASE IF EXISTS find_it;
CREATE DATABASE find_it;

-- select the database
USE find_it;

-- create the tables

# table for Person
CREATE TABLE Person
(
  person_ID              INT            PRIMARY KEY,
  person_name     VARCHAR(50)    NOT NULL,
  person_gender VARCHAR(50) NOT NULL,
  person_title VARCHAR(50) NOT NULL
);

# table for Room
CREATE TABLE Room
(
  room_ID                  INT            PRIMARY KEY,
  room_type VARCHAR(50),
  room_name VARCHAR(50),
  location VARCHAR(50) NOT NULL,
  has_AC VARCHAR(50)
);

# table for Pet
CREATE TABLE Pet
(
  pet_tag            INT            PRIMARY KEY,
  pet_name VARCHAR(50) NOT NULL,
  pet_type VARCHAR(50) NOT NULL,
  pet_size VARCHAR(50) NOT NULL
);


# table for Closet
CREATE TABLE Closet
(
  closet_ID            INT            PRIMARY KEY,
  closet_type VARCHAR(50),
  location INT NOT NULL,
  CONSTRAINT located_in FOREIGN KEY (location) REFERENCES Room (room_ID)
  ON UPDATE CASCADE ON DELETE CASCADE
);

# table for Safe
CREATE TABLE Safe
(
  safe_ID            INT            PRIMARY KEY,
  safe_password VARCHAR(50) NOT NULL,
  location INT NOT NULL,

  CONSTRAINT hidden_in FOREIGN KEY (location) REFERENCES Room (room_ID)
  ON UPDATE CASCADE ON DELETE RESTRICT
);

# table for Personal_device
CREATE TABLE Device 
(
device_SN          VARCHAR(50)            PRIMARY KEY, 
device_type VARCHAR(50) NOT NULL,
brand VARCHAR(50) NOT NULL,
warranty_expiration date,
device_owner INT NOT NULL,
CONSTRAINT belong_to FOREIGN KEY (device_owner) REFERENCES Person (person_ID)
ON UPDATE CASCADE ON DELETE CASCADE
);

# table for Clothing
CREATE TABLE Clothing
(
  clothing_ID           INT            PRIMARY KEY,
  clothing_type VARCHAR(50),
  clothing_gender VARCHAR(50),
  clothing_color VARCHAR(50),
  clothing_size VARCHAR(50),
  clothing_owner INT,
  location INT NOT NULL,
  CONSTRAINT stored_in FOREIGN KEY (location) REFERENCES Closet (closet_ID)
  ON UPDATE CASCADE ON DELETE RESTRICT,
  CONSTRAINT worn_by FOREIGN KEY (clothing_owner) REFERENCES Person (person_ID)
  ON UPDATE CASCADE ON DELETE CASCADE
);

# table for Medecine_pharmacy

CREATE TABLE Medicine
(
  medicine_ID           INT            PRIMARY KEY,
  medicine_name VARCHAR(50),
  medicine_type VARCHAR(50),
  medicine_owner INT,
  prescription VARCHAR(50),
  expiration_date VARCHAR(50) NOT NULL,
  location INT NOT NULL,
  CONSTRAINT taken_by FOREIGN KEY (medicine_owner) REFERENCES Person (person_ID)
  ON UPDATE CASCADE ON DELETE CASCADE,
  CONSTRAINT preserved_in FOREIGN KEY (location) REFERENCES Closet (closet_ID)
  ON UPDATE CASCADE ON DELETE RESTRICT
);

# table for Home_appliance
CREATE TABLE Home_appliance
(
  appliance_SN           VARCHAR(50)             PRIMARY KEY,
  appliance_type VARCHAR(50),
  brand VARCHAR(50), 
  size VARCHAR(50), 
  location INT NOT NULL,
  CONSTRAINT installed_in FOREIGN KEY (location) REFERENCES Room (Room_ID)
  ON UPDATE CASCADE ON DELETE RESTRICT
);


# table for Important_item
CREATE TABLE Important_item
(
  important_item_ID           INT            PRIMARY KEY,
  important_item_type VARCHAR(50),  
  important_item_value VARCHAR(50), 
  important_item_owner INT, 
  location INT NOT NULL,
  CONSTRAINT protected_in FOREIGN KEY (location) REFERENCES Safe (safe_ID)
  ON UPDATE CASCADE ON DELETE CASCADE,
  CONSTRAINT owned_by FOREIGN KEY (important_item_owner) REFERENCES Person (person_ID)
  ON UPDATE CASCADE ON DELETE RESTRICT
);

# table for furniture
CREATE TABLE Furniture
(
  furniture_ID                  INT            PRIMARY KEY,
  furniture_type VARCHAR(50),
  location INT NOT NULL,
  CONSTRAINT found_in FOREIGN KEY (location) REFERENCES Room (room_ID)
  ON UPDATE CASCADE ON DELETE RESTRICT
);

# table for Pet_item
CREATE TABLE Pet_item
(
  pet_item_ID            INT            PRIMARY KEY,
  pet_item_type VARCHAR(50),
  used_for VARCHAR(50),
  p_owner INT,
  CONSTRAINT used_by FOREIGN KEY (p_owner) REFERENCES Pet (pet_tag)
  ON UPDATE CASCADE ON DELETE CASCADE
);

# table for Pet_medecine
CREATE TABLE Pet_medicine
(
  pet_medicine_ID            INT            PRIMARY KEY,
  pet_medicine_type VARCHAR(50),
  expiration_date date NOT NULL,
  pet_type VARCHAR(50),
  good_for_size VARCHAR(50),
  p_owner INT,
  location INT NOT NULL,
  CONSTRAINT gotten_by FOREIGN KEY (p_owner) REFERENCES Pet (pet_tag)
  ON UPDATE CASCADE ON DELETE CASCADE,
  CONSTRAINT located FOREIGN KEY (location) REFERENCES closet (closet_ID)
  ON UPDATE CASCADE ON DELETE RESTRICT
);

# table for authorized relation

CREATE TABLE Authorized (
safe_id INT,
person_id INT,
CONSTRAINT person_safe PRIMARY KEY (safe_id, person_id),
FOREIGN KEY (safe_id) REFERENCES Safe(safe_id)
ON UPDATE CASCADE ON DELETE RESTRICT,
FOREIGN KEY (person_id) REFERENCES Person(person_id)
ON UPDATE CASCADE ON DELETE RESTRICT
);

-- ----------------------------------------------------------
-- ----------------------------------------------------------
-- ----------------------------------------------------------

-- Creating indexes

-- index for the person name
CREATE INDEX idx_p_name ON Person(person_name);

-- index for the person gender
CREATE INDEX idx_p_gender ON Person(person_gender);

-- index for the Clothing size
CREATE INDEX idx_c_size ON Clothing(clothing_size);

-- index for the Clothing gender
CREATE INDEX idx_c_gender ON Clothing(clothing_gender);

-- index for the Medicine expiration date
CREATE INDEX idx_m_expiration_date ON Medicine(expiration_date);

-- index for the pet Medicine expiration date
CREATE INDEX idx_pm_expiration_date ON Pet_medicine(expiration_date);

-- ----------------------------------------------------------
-- ----------------------------------------------------------
-- ----------------------------------------------------------
-- ----------------------------------------------------------
-- ----------------------------------------------------------
-- ----------------------------------------------------------


-- The section below is for creating procedures funcftion/ triggers/ events
 
-- 1 find person devices

DELIMITER //
CREATE PROCEDURE person_devices
(
person VARCHAR(50)
)
BEGIN
  SELECT  d.device_type, d.device_SN
  FROM Person  as p JOIN Device as d
  ON d.device_owner = p.person_ID
  where person_ID = person;
END// 

DELIMITER ; 

-- ----------------------------------------------------------


-- 2 find medicines and which closet, room, floor are located

DELIMITER //
CREATE PROCEDURE person_medicines
(
person INT
)
BEGIN
  SELECT med, mtype, mdate, mloc, table2.ct, r.room_type, r.location  FROM 
(
SELECT med, mtype, mdate, mloc, c.closet_type as ct, c.location as loc FROM (
SELECT m.medicine_name as med, m.medicine_type as mtype, m.expiration_date as mdate, m.location as mloc
  FROM Medicine as m JOIN Person as p
  ON p.person_ID = m.medicine_owner
  where person_ID = person
  ) AS table1
JOIN Closet as c ON c.closet_ID = table1.mloc
) AS table2
JOIN Room as r ON table2.loc = r.room_ID;
END// 

DELIMITER ; 

-- ----------------------------------------------------------

-- 3- Find a person's clothes

DELIMITER //
CREATE PROCEDURE person_clothes
(
person INT
)
BEGIN

  SELECT clothing_type, clothing_gender, clothing_size,
  clothing_color, location FROM
  (SELECT  c.*, p.person_ID as pid, p.person_name as pname FROM Clothing as c
  JOIN Person as p
  ON clothing_owner = person_ID
  ) as f
  WHERE pid = person;
END// 

DELIMITER ; 

-- ----------------------


-- 4 find medicine of specific sickness

DELIMITER //
CREATE PROCEDURE medicine_sickness
(
sickness VARCHAR(255)
)
BEGIN
  SELECT *
  FROM Medicine
  where medicine_type = sickness;
END// 

DELIMITER ; 

-- ----------------------------------------------------------

-- 5- Find what medicine will be expired after a specific date
DELIMITER //
CREATE PROCEDURE medicine_exp
(
exp_date date
)
BEGIN
  SELECT  * FROM Medicine
  WHERE exp_date > expiration_date;
END// 

DELIMITER ; 

-- ----------------------------------------------------------

-- 7- Find what pet medicine will be expired after a specific date

DELIMITER //
CREATE PROCEDURE pet_medicine_exp
(
exp_date date
)
BEGIN
  SELECT  * FROM Pet_medicine
  WHERE exp_date > expiration_date;
END// 

DELIMITER ; 


-- ----------------------------------------------------------

--  8- Find clothes of a specific gender and size
DELIMITER //
CREATE PROCEDURE clothes_gender_size
(
size VARCHAR(50),
gender VARCHAR(50)
)
BEGIN
  SELECT  * FROM Clothing
  WHERE clothing_size = size
  AND clothing_gender = gender;
END// 

DELIMITER ; 

-- ----------------------------------------------------------

-- 9- Find what devices will have their warranty expired by a specific date

DELIMITER //
CREATE PROCEDURE device_warranty
(
w_date date
)
BEGIN
  SELECT  * FROM Device
  WHERE warranty_expiration < w_date;
END// 

DELIMITER ; 

-- -------------------

-- 10- Find a person's important item

DELIMITER //
CREATE PROCEDURE person_important_items
(
person int
)
BEGIN
  SELECT  * FROM important_item
  WHERE important_item_owner =  person;
END// 

DELIMITER ; 

-- -------------------------------------

-- 11- Find how many appliance there are of a specific type

DELIMITER //
CREATE FUNCTION number_of_appliances
(
appliance VARCHAR(50)
)
RETURNS INT
DETERMINISTIC READS SQL DATA
BEGIN
DECLARE result_var INT;

SELECT cc INTO result_var
FROM (
SELECT COUNT(*) AS cc FROM
Home_appliance
WHERE 
appliance_type = appliance
) AS r;

RETURN result_var;
END//

DELIMITER ;

-- ----------------------
-- 12 Find how many furnitures are in a specific room

DELIMITER //
CREATE PROCEDURE room_furniture
(
room_n INT
)
BEGIN
  SELECT f.furniture_type, r.room_type
  FROM Furniture  as f JOIN Room as r
  ON f.location = room_ID
  where room_ID = room_n;
END// 

DELIMITER ; 

