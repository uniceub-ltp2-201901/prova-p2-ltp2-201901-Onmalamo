from random import *

def get_urls(cursor):
    cursor.execute('SELECT old_url,new_url FROM url_data')

    url = cursor.fetchall()

    return url

def get_db(mysql):
    conn = mysql.connect()
    cursor = conn.cursor()

    return conn, cursor

def get_random():
    return randint(10001,99999)

def associar_urls(conn,cursor,url,random_number):
    cursor.execute(f'insert into url_data (old_url,new_url) values("{url}","http://localhost:5000/{random_number}")')
    conn.commit()