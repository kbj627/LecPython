#program exam 1
#from bs4 import BeautifulSoup

#html_doc= """
#<html><head><title>The Dormouse's story</title></head>
#<body>
#<p class="title"><b>The Dormouse's story</b></p>
#<p class="story">Once upon a time there were three little sisters; and their names were
#<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
#<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
#<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
#and they lived at the bottom of a well.</p>
#<p class="story">...</p>
#"""

#soup = BeautifulSoup(html_doc, "html.parser")
#print(soup.prettify())
#print(soup.a.prettify())
#print(soup.html.head.title.string)
#print(soup.p['class'])
#print(soup('p'))
#print(soup('a'))
#print(soup('a')[0])
#print(soup('a', {'class' : 'sister'}))
#print(soup('img', {'name' : 'main'}))
#print(soup('p', {'class' : 'layout'}))


#program exam 2
#from bs4 import BeautifulSoup
#from urllib.request import urlopen
#from urllib.parse import urljoin

#soup = BeautifulSoup(html_doc, "html.parser")
#print(soup.find('a')['href'])
#print(soup.find_all(id='link3'))

#print(soup.find_all('p'))
#print(soup.find_all(class_='sister'))


#program exam 3
#from bs4 import BeautifulSoup
#from urllib.request import urlopen
#from urllib.parse import urljoin
#import webbrowser

#url = 'http://comic.naver.com/webtoon/list.nhn?titleId=400742&weekday=wed'

#data = urlopen(url)
#soup = BeautifulSoup(data.read(), from_encoding='utf-8')
##print(soup.encode('utf-8'))
#cartoons = soup.find_all('td', {'class' : 'title'})
#print(cartoons)

#for i in range(len(cartoons)):
#    title = cartoons[i].find('a').string
#    ref = cartoons[i].find('a')['href']
#    tempurl= urljoin(url, ref)
#    print(title, " " , tempurl)

#webbrowser.open_new(tempurl)


#program exam 4
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
                    print(url.find("'"), ' '+url)
                    if url.find("'")!=-1 : continue     #'를 찾은 결과가 -1이 아니면 ('가 있으면 안된다는 뜻인가?)
                    url= url.split("#")[0]              # #이 있으면 자르고 왼쪽거
                    if url[0:4]=='http':                # http가 있는 경우만 추가
                        newpage.add(url)
            pages = newpage

pagelist=['http://www.naver.com']
crawler = crawler()
crawler.crawl(pagelist)
