import mysql.connector
from config import db_config

def get_connection():
	db = mysql.connector.connect(
	host=db_config['host'],
	user=db_config['user'],
	password=db_config['password'],
	database=db_config['database']
	)
	return db

