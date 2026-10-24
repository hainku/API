import os
import mysql.connector
class Database:
    def __init__(self):
        self.con=mysql.connector.connect(
            host=os.getenv("HOST"),
            user=os.getenv("USER"),
            password=os.getenv("PASSWORD"),
            database=os.getenv("DB")
        )
