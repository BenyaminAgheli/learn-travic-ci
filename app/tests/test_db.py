from db.functions import get_connection

def test_check_db_connection():
	conn=get_connection()
	assert conn.is_connected()

	cursor = conn.cursor()
	cursor.execute("SELECT 1")
	result = cursor.fetchone()
	assert result[0] == 1

	cursor.close()
	conn.close()
