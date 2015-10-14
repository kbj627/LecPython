#program exam 1
#import re

#pattern = re.compile("d")
#result = pattern.search("dog")
#print(result)
#result = pattern.search("dog", 1)
#print(result)

##raw mode(둘다 같은 의미)
#re.search("\\\\", "C:\\test")
#re.search(r"\\", "C:\\test")

#pattern = re.compile("o")
#result = pattern.match("dog")
#print(result)
#result = pattern.match("dog",1)
#print(result)


#program exam 2
#import re

#str = '''sample1.
#sample2.
#sample3.'''

#p = re.compile('^.*$', re.S)
#result = p.search(str)
#print(result.group())


#program exam 3
#import re

#pattern = re.compile("o[gh]")

#result = pattern.fullmatch("dog")
#if result != None:
#    print('1 : ', result.group())

#result = pattern.fullmatch("ogre")
#if result != None:
#    print('2 : ', result.group())

#result = pattern.fullmatch("doggie",1,3)
#if result != None:
#    print('3 : ', result.group())


#program exam 4
#import re

#pattern = re.compile('\W+')
#result = pattern.split('words, words, words.')
#print(result)

#result = pattern.split('words, words, words.',1)
#print(result)

#pattern = re.compile("x*")
#result = pattern.split('axbc')
#print(result)

#result = re.sub(r'\W','','a:b:c, d.') #문자열이 아닌것을 ''로 치환한다. 결과 abcd
#print(result)


#program exam 5
#import re

#str= '<a href="index.html">HERE</a><font size="10">'
#result = re.search(r'href="(.*?)">', str)
#print(result.group(1))


#program exam 6
import re

num = '123456-1234567'

result = re.compile('(\d{6})-(\d{7})')
result = result.fullmatch(num)
print(result.group(1))
print(result.group(2))