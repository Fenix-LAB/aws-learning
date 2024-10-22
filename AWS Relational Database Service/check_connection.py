import psycopg2

"""
Try to connect to the database using the psycopg2 library.
"""

try:
    # Conexión a la base de datos
    conn = psycopg2.connect(
        dbname='postgres',
        user='postgres',
        password='',
        host='',
        port='5432'
    )
    print("Successfully connected to the database :)")
    conn.close()
except psycopg2.Error as e:
    print("Error connecting to the database: ", e)