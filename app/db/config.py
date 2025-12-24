import os

db_config = {
    'host': os.getenv('MYSQL_HOST', 'db'),
    'port': os.getenv('MYSQL_PORT', 3306),
    'user': os.getenv('MYSQL_USER',''),
    'password': os.getenv('MYSQL_PASSWORD', ''),
    'database': os.getenv('MYSQL_DATABASE', 'myapp')
}
