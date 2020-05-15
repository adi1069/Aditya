# #CREATE TABLE
# import os
# import sqlite3
#
#
# #Create A fuction() named create_connections which will return Connections
# from pip._vendor.distlib._backport.shutil import Error
# from pip._vendor.urllib3.util.connection import create_connection
#
#
# def create_connections(db_file):
#     conn = None
#     try:
#         conn = sqlite3.connect(db_file)
#         return conn
#     except Error as e:
#         print(e)
#
#     return conn
#
#
# #Create function named create_table() that accepts a CONNECTION objects and an SQL statement
# #Inside the function,we call the execute() method of the Cursor object to excute the CREATE TABLE statemnt
#
# def create_table(conn, create_table_sql):
#     """ create a table from the create_table_sql statement
#         :conn: Connection object
#         :create_table_sql: a CREATE TABLE statement
#         :return:
#         """
#     try:
#         c = conn.cursor()
#         c.execute(create_table_sql)
#     except Error as e:
#         print(e)
#
#
#
# """ Create a main() functions to create the projecta and tasks table """
#
# def DB():
#
#     sql_create_projects_table=""" CREATE TABLE IF NOT EXISTS projects (
#                                         id integer PRIMARY KEY,
#                                         name text NOT NULL,
#                                         begin_date text,
#                                         end_date text
#                                     ); """
#
#
#     sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS tasks (
#                                     id integer PRIMARY KEY,
#                                     name text NOT NULL,
#                                     priority integer,
#                                     status_id integer NOT NULL,
#                                     project_id integer NOT NULL,
#                                     begin_date text NOT NULL,
#                                     end_date text NOT NULL,
#                                     FOREIGN KEY (project_id) REFERENCES projects (id)
#                                 );"""
#
#     conn = create_connections("pythonsqlite.db")
#
#     if conn is not None:
#         create_table(conn, sql_create_projects_table)    #create project table
#         create_table(conn, sql_create_tasks_table)      #create task table
#
#     else:
#         print("Error! cannot create a database connection")
#
#
# # Execute main() function
#
# if __name__== '__main__' :
#     DB()




import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():
    database = r"C:\sqlite\db\pythonsqlite.db"

    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS projects (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        begin_date text,
                                        end_date text
                                    ); """

    sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS tasks (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    priority integer,
                                    status_id integer NOT NULL,
                                    project_id integer NOT NULL,
                                    begin_date text NOT NULL,
                                    end_date text NOT NULL,
                                    FOREIGN KEY (project_id) REFERENCES projects (id)
                                );"""

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_projects_table)

        # create tasks table
        create_table(conn, sql_create_tasks_table)
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()
