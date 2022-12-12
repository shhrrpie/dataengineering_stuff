# Load libraries
import pandas as pd
from sqlalchemy import create_engine

# Create database engine for question_3_a_answer.db
engine = create_engine('sqlite:///question_3_a_answer.db')

# Write query to answer question 2_b
query_3_b = """
WITH CTE_b as
(SELECT "customers.csv".id, SUM("invoice_lines.csv".quantity) AS Quantity
FROM (("invoices.csv"
INNER JOIN "invoice_lines.csv" ON "invoices.csv".id = "invoice_lines.csv".invoice_id)
INNER JOIN "customers.csv" ON "invoices.csv".customer_id = "customers.csv".id)
GROUP BY "customers.csv".name
HAVING SUM(Quantity)>5
)
Select count(id) AS Total_who_purchase_more_than_5_books
FROM CTE_b
"""

# Make a dataframe by passing query and engine to read_sql()
second_question_3_b = pd.read_sql(query_3_b, engine)

# View the resulting dataframe
print("\n")
print("Answer for Question 3 b: ")
print(" ")
print(second_question_3_b)
print("\n")
print("****************************************************************")

# Write query to answer question 2_b
query_3_c = """
WITH CTE_c as
(SELECT "customers.csv".name, "invoices.csv".sub_total AS Total_Spending
FROM "customers.csv"
LEFT JOIN "invoices.csv"
ON "customers.csv".id="invoices.csv".customer_id
WHERE Total_Spending is null
)
Select name 
FROM CTE_c
"""

# Make a dataframe by passing query and engine to read_sql()
second_question_3_c = pd.read_sql(query_3_c, engine)

# View the resulting dataframe
print("\n")
print("Answer for Question 3 c: ")
print(" ")
print(second_question_3_c)
print("\n")
print("****************************************************************")

# Write query to answer question 2_c
query_3_d = """
SELECT "invoice_lines.csv".description, "customers.csv".name
FROM (("invoices.csv"
INNER JOIN "invoice_lines.csv" ON "invoices.csv".id = "invoice_lines.csv".invoice_id)
INNER JOIN "customers.csv" ON "invoices.csv".customer_id = "customers.csv".id)
"""

# Make a dataframe by passing query and engine to read_sql()
second_question_3_d = pd.read_sql(query_3_d, engine)

# View the resulting dataframe
print("\n")
print("Answer for Question 3 d: ")
print(" ")
print(second_question_3_d)
print("\n")
print("****************************************************************")
