import os
import sqlite3
from xml.dom import minidom

filename = 'comp.db'
db = sqlite3.connect(filename)
create = os.path.exists(filename)
cursor = db.cursor()
# if create:
#     cursor.execute("Create table pc(id_pc integer PRIMARY KEY AUTOINCREMENT NOT NULL, name text, model text, price integer)")
#     db.commit()
#     cursor.execute("Create table details(id_det integer PRIMARY KEY AUTOINCREMENT NOT NULL, id_pc integer, type text, model text)")
#     db.commit()
#     cursor.execute("Create table pc_sales(id_sale integer PRIMARY KEY AUTOINCREMENT NOT NULL, id_pc integer, name_customer text)")
#     db.commit()
    
#     cursor.execute("Insert into pc (name, model, price) values ('MSI','gx150',50000)")
#     cursor.execute("Insert into pc (name, model, price) values ('ASUS','mz10',45000)")
#     cursor.execute("Insert into pc (name, model, price) values ('Lenovo','ideapad330',47999)")
#     cursor.execute("Insert into pc (name, model, price) values ('MSI','hyperz500',99999)")
#     db.commit()

#     cursor.execute("Insert into details (id_pc, type, model) values (1, 'videocard','MSI gtx1060')")
#     cursor.execute("Insert into details (id_pc, type, model) values (1, 'CPU','interl core i5 8600')")
#     cursor.execute("Insert into details (id_pc, type, model) values (1, 'moterboard','MSI BX320')")
#     cursor.execute("Insert into details (id_pc, type, model) values (1, 'RAM','HyperX 16G')")
#     db.commit()

#     cursor.execute("Insert into details (id_pc, type, model) values (2, 'videocard',' ASUS gtx1050ti')")
#     cursor.execute("Insert into details (id_pc, type, model) values (2, 'CPU','interl core i5 7500')")
#     cursor.execute("Insert into details (id_pc, type, model) values (2, 'moterboard','ASUS BX320')")
#     cursor.execute("Insert into details (id_pc, type, model) values (2, 'RAM','Samsung 16G')")
#     db.commit()

#     cursor.execute("Insert into details (id_pc, type, model) values (3, 'videocard','ASUS gtx1060')")
#     cursor.execute("Insert into details (id_pc, type, model) values (3, 'CPU','AMD Ryzen 1600x')")
#     cursor.execute("Insert into details (id_pc, type, model) values (3, 'moterboard','MSI BX320')")
#     cursor.execute("Insert into details (id_pc, type, model) values (3, 'RAM','HyperX 16G')")
#     db.commit()

#     cursor.execute("Insert into details (id_pc, type, model) values (4, 'videocard','MSI gtx2080')")
#     cursor.execute("Insert into details (id_pc, type, model) values (4, 'CPU','interl core i9 9700')")
#     cursor.execute("Insert into details (id_pc, type, model) values (4, 'moterboard','MSI ZM500')")
#     cursor.execute("Insert into details (id_pc, type, model) values (4, 'RAM','HyperX 32G')")
#     db.commit()

#     cursor.execute("Insert into pc_sales (id_pc, name_customer) values (1,'Ivanov')")
#     cursor.execute("Insert into pc_sales (id_pc, name_customer) values (4,'Petrov')")
#     cursor.execute("Insert into pc_sales (id_pc, name_customer) values (2,'Jitiy')")
#     cursor.execute("Insert into pc_sales (id_pc, name_customer) values (3,'Cukerberg')")
#     db.commit()

#     db.close()

for row in cursor.execute("select * from pc"):
    print(row)
for row in cursor.execute("select * from details"):
    print(row)
for row in cursor.execute("select * from pc_sales"):
    print(row)
cursor.execute("select id_pc FROM pc_sales WHERE name_customer =='Ivanov'")
find = cursor.fetchone()
find = int(find[0])
print(find)
cursor.execute("select type, model FROM details WHERE id_pc =?", [find])
print(cursor.fetchall())