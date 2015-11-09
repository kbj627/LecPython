#program exam 1
import sqlite3
from werkzeug import check_password_hash, generate_password_hash

def get_DB():
    db = sqlite3.connect("test.db")
    return db

def init_DB():
    db = get_DB()
    with open('schema.sql') as f:
        db.cursor().executescript(f.read())
        db.commit()
    db.close()

def register():
    print("**** Register ****\n")
    userid = input("id : ")
    
    db = get_DB()
    cur = db.cursor()
    cur.execute("select * from user where userid=?", [userid])
    if cur.fetchone() != None :
        print("중복")
        return
    
    name = input("name : ")
    userpw = input("password : ")
    sql = "insert into user(userid, username, userpw) values(?,?,?);"
    cur.execute(sql, [userid, name, generate_password_hash(userpw)])
    cur.execute("select * from user;")
    print(cur.fetchall())
    db.commit()
    db.close()
    

def login():
    print("**** Login ****\n")
    userid = input("id : ")
    name = input("name : ")
    userpw = input("password : ")
    
    db = get_DB()
    cur = db.cursor()
    cur.execute("select * from user where userid=?", [userid])
    temp = cur.fetchone()
    if temp != None :
        print("ID가 존재합니다.")
        return
    elif check_password_hash(temp[3], userpw):
        print("Login 성공")
        return
    else:
        print("Password 틀림")
        return
    
    db.commit()
    db.close()

init_DB()
register()
login()