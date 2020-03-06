
'''Create a new connections'''
import sqlite3



def create_connection(db_file):
    conn = None
    try:
        conn=sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)

'''Create a project'''

def create_project(conn,project):
    sql=""
    cur=conn.cursor()
    cur.execute(sql, project)
    return cur.lastrowid

'''Create another function for inserting rows into the tasks'''

