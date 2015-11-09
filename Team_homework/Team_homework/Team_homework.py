import sqlite3
import webbrowser
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import urljoin

class crawler:
    def crawl(self, pages, depth=2):
        for i in range(depth):  #depth만큼 깊이를 탐색
            newpage= set()
            for page in pages:  #pages의 목록을 탐색
                try:
                    c = urlopen(page)
                except:
                    print("Could not open %s" % page)
                    continue
                soup = BeautifulSoup(c.read(), from_encoding="utf-8")
                print('Found %s' % page)
            links = soup('a')
            for link in links:  #links에는 page의 url을 검색한 결과중 'a' 태그가 들어간 것 들이 저장됨
                print(link)
                if 'href' in dict(link.attrs):  #link의 attribute중 href가 있는 것
                    url= urljoin(page, link['href'])    #urljoin의 기능은 현재 page에서 href가 되는 결과를 얻기위한 url로 만들어주는것
                    if url.find("'")!=-1 : continue     #'를 찾은 결과가 -1이 아니면 ('가 있으면 안된다는 뜻인가?)
                    url= url.split("#")[0]              # #이 있으면 자르고 왼쪽거
                    if url[0:4]=='http':                # http가 있는 경우만 추가
                        newpage.add(url)
            pages = newpage

def getMaxPage(url):
    l = []
    data = urlopen(url)
    soup = BeautifulSoup(data.read(), from_encoding = 'utf-8')
    for link in soup('a'):
        if 'href' in dict(link.attrs):
            if link['href'].find('page=') != -1:
                l.append(link['href'].split('page=')[1])
    page = max(l)

    return page

url = 'http://musicbrainz.org/area/b9f7d640-46e8-313e-b158-ded6d18593b3/artists?page=1'
getMaxPage(url)