import mysql.connector
from secret import Secret


class DBHelper:
    def __init__(self):
        sr = Secret()
        self.con = mysql.connector.connect(
            host='localhost',
            user='root',
            password=sr.get_secret_key(),
            database=sr.get_database()
        )
        query = "create table if not exists accounts(user_name varchar(200), user_email varchar(200), app_name varchar(100), url varchar(300), password varchar(100))"
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()

    def store_passwords(self, password, user_email, username, url, app_name):
        query = 'insert into accounts(user_name, user_email, app_name, url, password) values ("{}","{}","{}","{}","{}")'.format(
            username, user_email, app_name, url, password)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()

    def find_password(self, app_name):
        query = "select user_name, user_email, password from accounts where app_name='{}'".format(
            app_name)
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("User name : ", row[0])
            print("user email : ", row[1])
            print("password : ", row[2])

    def find_users(self, user_email):
        query = "select user_name, app_name from accounts where user_email='{}'".format(
            user_email)
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("User name : ", row[0])
            print("application : ", row[1])
