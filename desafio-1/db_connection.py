import psycopg2


def connect_to_db():
    conn = psycopg2.connect(
        host="localhost",
        database="mydatabase",
        user="myuser",
        password="mypassword"
    )
    conn.autocommit = True
    cur = conn.cursor()
    return conn, cur


def close_db_connection(conn, cur):
    cur.close()
    conn.close()