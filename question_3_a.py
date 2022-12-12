# Load libraries
import sqlite3  

# Create and open database
print("\n")
print("********************************************************************************")
print("Answer for Question 3 a: ")
print(" ")
print("Creating database...")

sqliteConnection  = sqlite3.connect('question_3_a_answer.db')  
cursor = sqliteConnection.cursor()

print("Task 1: Database successfully created & opened")
print(" ")

  
# Create table for customers.csv
print("Creating customer.csv table...")

sqliteConnection.execute('''CREATE TABLE "customers.csv"
(
id int PRIMARY KEY,
name varchar(255),
email varchar(255),
tel varchar(15),
created_at DATETIME,
updated_at DATETIME
)''')  

print("Task 2: Table customers.csv successfully created")  

# Create table for invoices.csv
print("Creating invoices.csv table...")

sqliteConnection.execute('''CREATE TABLE "invoices.csv"
(
id int PRIMARY KEY,
number int,
sub_total decimal(5,2),
tax_total decimal(3,2),
total decimal(5,2),
customer_id int,
created_at DATETIME,
updated_at DATETIME
)''')  

print("Task 2: Table invoices.csv successfully created")  

# Create table for invoice_lines.csv
print("Creating invoice_lines.csv table...")

sqliteConnection.execute('''CREATE TABLE "invoice_lines.csv"
(
id int PRIMARY KEY,
description varchar(30),
unit_price decimal(4,2),
quantity int,
sub_total decimal(5,2),
tax_total decimal(3,2),
total decimal(5,2),
tax_id NULL,
sku_id int,
invoice_id int
)''')  

print("Task 2: Table invoice_lines.csv successfully created")
print(" ")


# Insert value into the database
# Insert for customers.csv
print("Inserting customers.csv data...")

insert_customers_csv="INSERT INTO 'customers.csv' (id, name, email, tel, created_at, updated_at) VALUES (?,?,?,?,?,?);"""


records_customers_csv = [(1, 'Irfan Bakti', 'irfan88@example.com', '+60123456789', '2019-08-07 08:13:21', '2019-08-07 08:13:21'),
                   (2, 'Jack Smmith', 'jack.smmith@acme.io', '+60132456781', '2019-08-07 08:13:21', '2019-08-07 08:13:21'), 
                   (3, 'Nazir', '', '+601185434012', '2019-08-07 08:13:21', '2019-08-07 08:13:21'),
                   (4, 'Faiz Ma', 'faiz.ma@jholow.cn', '+6019772002', '2019-08-07 08:13:21', '2019-08-07 08:13:21'), 
                   (5, 'Isham Rais', 'isham@pmo.gov.my', '+60135482020', '2019-08-07 08:13:21' , '2019-08-07 08:13:21'), 
                   (6, 'Shanon Teoh', 'shahnon.teoh@st.com.sg', '', '2019-08-07 08:13:21', '2019-08-07 08:13:21')]


cursor.executemany(insert_customers_csv, records_customers_csv)

print("Task 3: Records for customers.csv successfully inserted")


# Insert for invoices.csv
print("Inserting invoices.csv data...")

insert_invoices_csv="INSERT INTO 'invoices.csv' (id, number, sub_total, tax_total, total, customer_id, created_at, updated_at) VALUES (?,?,?,?,?,?,?,?);"""


records_invoices_csv = [(1,'20190001',30.00,0.00,30.00,1,'2019-08-07 08:13:21','2019-08-07 08:13:21'),
                   (2,'20190002',150.00,0.00,150.00,2,'2019-08-07 08:13:21','2019-08-07 08:13:21'),  
                   (3,'20190003',30.00,0.00,30.00,2,'2019-09-15 08:13:21','2019-09-15 08:13:21'),    
                   (4,'20190004',55.00,0.00,55.00,3,'2019-09-15 08:13:21','2019-09-15 08:13:21'),    
                   (5,'20190005',450.00,0.00,450.00,6,'2019-09-15 08:13:21','2019-09-15 08:13:21')]





cursor.executemany(insert_invoices_csv, records_invoices_csv)

print("Task 3: Records for invoices.csv successfully inserted")


# Insert for invoice_lines.csv
print("Inserting invoice_lines.csv data...")

insert_invoice_lines_csv="INSERT INTO 'invoice_lines.csv' (id, description, unit_price, quantity, sub_total, tax_total, total, tax_id, sku_id, invoice_id) VALUES (?,?,?,?,?,?,?,?,?,?);"""


records_invoice_lines_csv = [(1, 'Book #1', 30.00, 1, 30.00, 0.00, 30.00, None, 1, 1),
                   (2, 'Book #2', 25.00, 4, 100.00, 0.00, 100.00, None, 2, 2),
                   (3, 'Book #3', 50.00, 1, 50.00, 0.00, 50.00, None, 3,2),   
                   (4, 'Book #1', 30.00, 1, 30.00, 0.00, 30.00, None, 1,3),
                   (5, 'Book #1', 30.00, 1, 30.00, 0.00, 30.00, None, 1,4),
                   (6, 'Book #2', 25.00, 1, 25.00, 0.00, 25.00, None, 2,4),
                   (7, 'Book #1', 30.00, 5, 150.00, 0.00, 150.00, None, 1, 5),
                   (8, 'Book #3', 50.00, 6, 300.00, 0.00, 300.00, None, 3, 5)]



cursor.executemany(insert_invoice_lines_csv, records_invoice_lines_csv)

print("Task 3: Records for invoice_lines.csv successfully inserted")

# Commit
sqliteConnection.commit()  

# Close
sqliteConnection.close()

print(" ")
print("All processes done!")
print("********************************************************************************")
