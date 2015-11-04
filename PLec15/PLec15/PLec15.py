#program exam 1
import sqlite3

con = sqlite3.connect('test.db')    # 디스크에 만드는 DB
#con = sqlite3.connect(':memory:')   # 메모리에 만드는 임시 DB


sql = '''create table if not exists phonebook(name text, phoneNum text);''' # table이 없으면 생성
dropsql = '''drop table if exists phonebook;''' # table을 삭제
insertsql = '''insert into phonebook values('greenjoa1','010-1111-2222');'''  # table에 값을 입력
selectsql = '''select * from phonebook'''       # table의 내용 검색

cur = con.cursor()

#con.isolation_level = None   # 자동 커밋모드 설정

#cur.execute(dropsql)
#cur.execute(sql)
#cur.execute(insertsql)  # 쿼리문을 사용

#name = 'greenjoa2'
#phoneNumber = '010-2222-2222'
#insertsql = '''insert into phonebook values(?,?);'''
#cur.execute(insertsql, (name, phoneNumber)) # ?을 사용한 인자 입력

#name = 'GREENJOA3'
#phoneNumber = '010-3333-3333'
#insertsql = '''insert into phonebook values(:inputName, :inputNum);'''
#cur.execute(insertsql, {"inputNum":phoneNumber, "inputName":name})  # 인자의 이름을 부여해서 사용

#insertsql = '''insert into phonebook values(?,?);'''
#datalist = (('greenjoa4','010-4444-4444'), ('greenjoa5','010-5555-5555'))
#cur.executemany(insertsql, datalist)    #iterator를 사용해서 많은 데이터를 입력

#def dataGenerator():
#    datalist = (('greenjoa6','010-6666-6666'),('greenjoa7','010-7777-7777'))
#    for item in datalist:
#        yield item  # yield는 return과 같이 반환 하지만 메소드를 종료시키지 않는다.
#cur.executemany(insertsql, dataGenerator())

#cur.execute("insert into phonebook(phoneNum) values('010-9999-9999');")


#cur.execute('create table if not exists user(name text, age int);')
#cur.executemany('insert into user values(?, ?)', (('강태욱', 23), ('홍길동', 20), ('김길동', 26)))


con.commit()    # 커밋을 해서 DB에 적용


#cur.execute("select count(*) from phoneBook;")
#print(cur.fetchone()[0])

#cur.execute("select count(name)from phoneBook;")
#print(cur.fetchone()[0])

#cur.execute(selectsql)
#print(cur.fetchone())

#cur.execute(selectsql)
#print(cur.fetchmany(2))

#cur.execute(selectsql)
#print(cur.fetchall())

#cur.execute("select * from phoneBook order by name;")
#print(cur.fetchall())

def OrderFunc(str1, str2):
    s1 = str1.upper()
    s2 = str2.upper()
    return (s1 > s2) -(s1 < s2) # 앞(음수), 같음(0), 뒤(양수)
con.create_collation('myordering', OrderFunc)

cur.execute("select * from phoneBook order by name collate myordering;")
print(cur.fetchall())

cur.execute("select * from user order by age collate myordering;")
print(cur.fetchall())
cur.execute("select max(age) from user;")
print(cur.fetchone())

#program exam 2
