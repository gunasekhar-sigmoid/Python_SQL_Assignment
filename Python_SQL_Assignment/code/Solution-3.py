import psycopg2
import pandas as pd

#storing data from xlsx
df = pd.read_excel("solution_2.xlsx")

#establishing connection with postgreSQL
database = psycopg2.connect (database = "assignment", user="postgres", password="root")

cursor = database.cursor()

#creating a table
create_query="""
CREATE TABLE Compensat (
   emp_name varchar(10) ,
   emp_no integer PRIMARY KEY,
   dept_name VARCHAR ( 50 ) ,
   Total_Compensation numeric,
   Months_Spent numeric
);
"""
cursor.execute(create_query)

#adding data from the dataframe
query = """INSERT INTO Compensat (emp_name, emp_no, dept_name, Total_Compensation, Months_Spent) VALUES (%s, %s, %s, %s, %s)"""

for r in range(1,len(df)):
    emp_name=df['ename'][r]
    emp_no=df['empno'][r]
    dept_name=df['dname'][r]
    Total_Compensation = df['total_compensation'][r]
    Months_Spent=df['months_spent'][r]

    values = (emp_name, emp_no, dept_name, Total_Compensation, Months_Spent)
    cursor.execute(query, values)

cursor.close()

database.commit