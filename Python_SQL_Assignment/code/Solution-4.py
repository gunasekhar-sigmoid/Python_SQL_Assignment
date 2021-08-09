import psycopg2
import pandas as pd

class departments:

    def total_compensation_by_department(self):

        try:
            #establishing a connection between postgreSQL and Python
            connection= psycopg2.connect(
            database="assignment",
            user="postgres",
            password="root")
            cursor = connection.cursor()

            #executing SQL Query to get required output
            query = """
            select dept.deptno, dept_name, sum(total_compensation) from Compensation, dept
            where Compensation.dept_name=dept.dname
            group by dept_name, dept.deptno
            """
            cursor.execute(query)

            #collecting obtained data from performing the SQL Query
            columns = [desc[0] for desc in cursor.description]
            data = cursor.fetchall()
            df = pd.DataFrame(list(data), columns=columns)

            #storing the collected data in a xlsx file
            writer = pd.ExcelWriter('solution_4.xlsx')
            df.to_excel(writer, sheet_name='bar')
            writer.save()

        except Exception as e:
            print("Error", e)

        finally:
            #closing the connection between PostgreSQL and python
            if connection is not None:
                cursor.close()
                connection.close()


if __name__ == '__main__':
    connection = None
    cur = None
    department = departments()
    department.total_compensation_by_department()