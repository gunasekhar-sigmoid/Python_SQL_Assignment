import psycopg2
import pandas as pd

class employees:

    def emp(self):

        try:
            #establishing a connection with postgreSQL
            connection = psycopg2.connect(
            database="assignment",
            user="postgres",
            password="root")
            cursor = connection.cursor()

            #running the query for required output
            query = """
            SELECT e1.empno, e1.ename, (case when mgr is not null then (select ename from emp as e2 where e1.mgr=e2.empno limit 1) else null end) as manager
            from emp as e1 
            """
            cursor.execute(query)

            #collecting the data obtained by executing the query
            columns = [desc[0] for desc in cursor.description]
            data = cursor.fetchall()
            df = pd.DataFrame(list(data), columns=columns)

            #storing the data collecting in a xlsx file
            writer = pd.ExcelWriter('solution_1.xlsx')
            df.to_excel(writer, sheet_name='bar')
            writer.save()

        except Exception as e:
            print("Error", e)

        finally:
            #closing the connection between postgreSQL and python
            if connection is not None:
                cursor.close()
                connection.close()


if __name__ == '__main__':
 connection = None
 cur = None
 employee = employees()
 employee.emp()