import mysql.connector

cnx = mysql.connector.connect(user='aditya',password='password',
                              host='127.0.0.1',
                              database='employees')

cnx.close()