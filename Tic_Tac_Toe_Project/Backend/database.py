import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Suroop@2003",
        database="tic_tac_toe"
    )
