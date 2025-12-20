import mysql.connector
from db.config import db_config

def get_connection():
	db = mysql.connector.connect(
	host="db",
	user="admin", # default user in XAMPP/WAMP
	password="1qaz", # leave empty if no password
	database="myapp" # optional: specify database
	)
	return db

