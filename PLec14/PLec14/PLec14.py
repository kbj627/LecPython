#program exam 1
#from bs4 import BeautifulSoup

#f = open('../test.xml', encoding='utf-8')
#xml = f.read()
#soup = BeautifulSoup(xml,'html.parser')

#for node in soup.findAll('node'):
#    print("Node : "+node.string)
#    print("Attr1 : "+node['attr1'])


#program exam 2
#f = open('../song.xml', encoding='utf-8')
#xml = f.read()
#soup = BeautifulSoup(xml,'html.parser')

#for nodes in soup.test('song'):
#    for node in nodes:
#        print(node.string)


#program exam 3
#f = open('../alcohol.xml', encoding='utf-8')
#xml = f.read()
#soup = BeautifulSoup(xml,'html.parser')

#for nodes in soup.alcohol('cate1'):
#    if nodes['tt'] == '안주':
#        print('Cate1 :' + nodes['tt'])
#        for node in nodes('cate2'):
#            print('\tCate2 :' + node['tt'])
#            for item in node('item'):
#                print('\t\t' + item.string)


#program exam 4
#import json

#data = {1:'a',2:'b'}
#data2 = json.dumps(data)
#data3 = json.loads(data2)
#print(type(data2))
#print(data2)
#print(type(data3))
#print(data3)


#program exam 5
import json

s = """
{
"name": "cybaek",
"detail" : { "last": "baek" },
"emails": [ "cybaek@xxx.com", "cybaek@yyy.com" ]
}
"""

data = json.loads(s)
print(data['name'])
print(data['detail'])
print(data['detail']['last'])


#program exam 6
import json

s = """
{
"name": "cybaek",
"detail" : { "last": "baek" },
"emails": [ "cybaek@xxx.com", "cybaek@yyy.com" ]
}
"""

class JsonObject:
    def __init__(self, d):
        self.__dict__ = d

data = json.loads(s, object_hook=JsonObject)
print(data.name)
print(data.detail)
print(data.detail.last)

for email in data.emails:
    print(email)