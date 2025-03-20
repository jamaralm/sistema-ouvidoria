import mysql.connector
from config import DB_CONFIG

connection = mysql.connector.connect(
    user=DB_CONFIG.get("user"),  
    password=DB_CONFIG.get("password"),  
    host=DB_CONFIG.get("host"),  
    database=DB_CONFIG.get("database")  
)
cursor = connection.cursor()