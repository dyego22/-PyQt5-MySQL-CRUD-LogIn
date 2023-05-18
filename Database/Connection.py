import pymysql

import psycopg2

def connection():
    conn = psycopg2.connect(
            host='localhost',
            user='postgres',
            password='1234',
            database='proyecto'
        )
    print('Database is Connected!')
    return conn