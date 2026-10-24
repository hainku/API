import os
import mysql.connector
from dotenv import load_dotenv
load_dotenv()
class Database:
    def __init__(self):
        self.conn=mysql.connector.connect(
            host=os.getenv("HOST"),
            user=os.getenv("USER"),
            port=int(os.getenv("PORT")),
            password=os.getenv("PASSWORD"),
            database=os.getenv("DB"),
            ssl_disabled=False
        )
