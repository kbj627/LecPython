#program exam 1

#fileName = 'greenjoa.txt'
#MODE = 'w+'
#with open(fileName, MODE) as myfile :
#    myfile.write('201111256 홍길동\n')
#    myfile.write('201111256 고길동\n')
#    myfile.write('201111256 김길동\n')
#    myfile.write('201111256 이길동\n')
#myfile.close()

#MODE = 'r'
#with open(fileName, MODE) as myfile :
#    content = myfile.read()
#    print(content)
    
#MODE = 'r'
#with open(fileName, MODE) as myfile :
#    while True :
#        content = myfile.readline()
#        if not content : break
#        print(content)

#program exam 2
#fileName = '파일입출력예제1.txt'
#fileName2 = 'Monica.txt'
#MODE = 'r'

#with open(fileName, MODE) as myfile, open(fileName2, 'w+') as myfile2 :
#    for content in myfile :
#        (role, etc) = content.strip().split(':')
#        print(role)
#        if role == 'Monica' :
#            myfile2.write(etc)
#            myfile2.write('\n')
            
#program exam 3
#fileName = '파일입출력예제2.txt'
#fileName2 = 'Monica2.txt'
#roles = []

#with open(fileName, 'r') as myfile, open(fileName2, 'w+') as myfile2 :
#    for content in myfile :
#        (role, etc) = content.strip().split(':', 1)
#        roles.append(role)
#        if role == 'Monica' :
#            myfile2.write(etc)
#            myfile2.write('\n')

#program exam 4
#import pickle

#roles = []

#with open('파일입출력예제2.txt', 'r') as myfile, open('Monica3.txt', 'wb+') as Monica :
#    for content in myfile :
#        (role, etc) = content.strip().split(':', 1)
#        roles.append(role)
#    pickle.dump(roles, Monica)

#with open('Monica3.txt', 'rb') as Monica :
#    result = pickle.load(Monica)
#    print(result)

#program exam 5
import csv

fileName = 'test.txt'

with open(fileName, 'r') as myfile :
    data = csv.reader(myfile)