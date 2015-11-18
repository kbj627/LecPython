#-*- coding: utf-8 -*-
import sqlite3
from bs4 import BeautifulSoup
from urllib.request import urlopen

def dataParse(url):
    l = []
    data = urlopen(url)
    soup = BeautifulSoup(data.read(), from_encoding = 'utf-8')
    
    for link in soup('a'):
        if 'href' in dict(link.attrs):
            if link['href'].find('page=') != -1:
                url, t = link['href'].split('page=')
                l.append(t)
    
    page = max(l)
    l = []
    
    for i in range(int(page)):
        urli = url+'page='+str(i+1)
        data = urlopen(urli)
        soup = BeautifulSoup(data.read(), from_encoding = 'utf-8')
        
        print(i+1, '번째 페이지 파싱중')
        for link in soup('a'):
            if 'href' in dict(link.attrs):
                if 'title' in dict(link.attrs):
                    if 'class' not in dict(link.attrs):
                        try:
                            l.append(link['title'])
                        except:
                            print('ô 이거 때문에 unicode Exception 난다.')
                            pass

    insertData(l)

def getDB():
    return sqlite3.connect("test.db")

def init_DB():
    db = getDB()
    cur = db.cursor()
    cur.execute('drop table if exists music;')
    cur.execute('create table music(name string, artist string not null);')
    db.commit()
    db.close()

def insertData(dataList):
    db = getDB()
    cur = db.cursor()
    sql = 'insert into music(artist) values(?);'

    db.commit()
    db.close()

init_DB()
dataParse('http://musicbrainz.org/area/b9f7d640-46e8-313e-b158-ded6d18593b3/artists?page=1')