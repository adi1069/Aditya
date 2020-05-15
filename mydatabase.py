import sqlite3
from sqlite3 import Error


def create_connection():
    """ create a database connection to a database that resides
       in the memory
   """
    conn = None
    try:
        conn = sqlite3.connect(':memory:')
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    create_connection()

# import sqlite3
#
# try:
#     sqlite_Connection = sqlite3.connect('temp.db')
#     conn = sqlite_Connection.cursor()
#     print("\nDatabase created and connected to SQLite.")
#     sqlite_select_Query = "select sqlite_version();"
#     conn.execute(sqlite_select_Query)
#     record = conn.fetchall()
#     print("\nSQLite Database Version is: ", record)
#     conn.close()
# except sqlite3.Error as error:
#     print("\nError while connecting to sqlite", error)
# finally:
#     if (sqlite_Connection):
#         sqlite_Connection.close()
#         print("\nThe SQLite connection is closed.")

# import sqlite3
# conn = sqlite3.connect('employee.db')
#
# c = conn.cursor()
#
# # c.execute("""CREATE TABLE employees (
# #             first text,
# #             last text,
# #             pay integer
# #             )""")
#
# c.execute("INSERT INTO employees VALUES ('Sandeep','Deshpande','900000')")
#
# conn.commit()
#
# c.execute("SELECT * FROM employees WHERE last='Deshpande' ")
#
# print(c.fetchall())
#
# conn.commit()
#
# conn.close()
