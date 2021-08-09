import psycopg2
import pandas as pd

class Total_compensation:

    def compensation(self):

        try:
            #establishing a connection with postgreSQL
            connection = psycopg2.connect(
                host="localhost",
                database="assignment",
                user="postgres",
                password="root")
            cur = connection.cursor()

            #query for obtaining required output
            query = """select emp.ename, emp.empno, dept.dname, (case when enddate is not null then ((enddate-startdate+1)/30)*(jobhist.sal) else ((current_date-startdate+1)/30)*(jobhist.sal) end)as Total_Compensation,
(case when enddate is not null then ((enddate-startdate+1)/30) else ((current_date-startdate+1)/30) end)as Months_Spent from jobhist, dept, emp 
where jobhist.deptno=dept.deptno and jobhist.empno=emp.empno"""
            cur.execute(query)

            #collecting the data obatined by executing the query
            columns = [desc[0] for desc in cur.description]
            data = cur.fetchall()
            df = pd.DataFrame(list(data), columns=columns)

            #Storing the data collected in a xlsx file
            writer = pd.ExcelWriter('solution_2.xlsx')
            df.to_excel(writer, sheet_name='bar')
            writer.save()

        except Exception as e:
            print("Error", e)

        finally:
            #closing the connection between postgreSQL and python
            if connection is not None:
                cur.close()
                connection.close()


if __name__=='__main__':
    connection = None
    cur = None
    comp = Total_compensation()
    comp.compensation()