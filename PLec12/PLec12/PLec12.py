#program exam 1
#import re

#str = '''Window
#Unix
#Linux
#Solaris'''
#p = re.compile('^.+', re.M)
#print(p.findall(str))
#p = re.compile('^.+', re.S)
#print(p.search(str))


#program exam 2
#import re

#m = re.match(r'(?P<first_name>\w+) (?P<last_name>\w+)', 'Malcolm Reynolds')
#print(m.group('first_name'))
#print(m.group('last_name'))
#print(m.groups())

#m = re.match(r"(\d+)\.?(\d+)?", "24")
#print(m.groups())
#print(m.groups(0))

#m = re.match(r'(?P<first_name>\w+) (?P<last_name>\w+)', 'Malcolm Reynolds')
#print(m.groupdict())


#program exam 3
#import re

#p = re.compile(".+:")
#m = p.search("http://google.com")
#print(m.group())

#p = re.compile(".+(?=:)")
#m = p.search("http://google.com")
#print(m.group())


#program exam 4
import os
import re
import glob

os.chdir('c:/')
p = re.compile('.*[.](?!bat$|exe$).*$')
l = glob.glob('*')
print(l)


#program exam 5
#import re

#p = re.compile('(?<=abc)def')
#m = p.search('abcdef')
#print(m.group())

#m = re.search('(?<=-)\w+', 'spam-egg')
#print(m.group())


#program exam 6
#import re

#email = "tony@tiremove_thisger.net"
#m = re.search("remove_this", email)
#result = email[:m.start()] + email[m.end():]
#print(m.start(), m.end())
#print(result)


#program exam 6
#import re

#text = """Ross: McFluff: 834.345.1254: 155 Elm Street
#Ronald: Heathmore: 892.345.3428 436: Finley Avenue
#Frank: Burger: 925.541.7625 662: South Dogwood Way
#Heather: Albrecht: 548.326.4584 919: Park Place"""

#entries = re.split('\n', text)
#result = [re.split(':?', entry, 4) for entry in entries]
#print(result)


#program exam 7
import re
import urllib.request

with urllib.request.urlopen('http://www.naver.com/') as f:
    #print(f.read())
    #print(f.read(300)) #300 byte
    r = re.search('<title>(.+)</title>', f.read().decode("utf-8"))
    print(r.groups(0))