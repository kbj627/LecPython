#program exam 1
#import os

#os.system('python test.py a b c')
#print(os.sys.path)


#program exam 2
#import pickle

#class Student:
#    def __init__(self, name, age):
#        self.name = name
#        self.age = age

#    def show(self):
#        print(self.name, ' : ', self.age)

#s1 = Student('greenjoa', 20)
#s1.show()

#f = open('test.txt', 'wb')
#pickle.dump(s1, f)
#f.close()

#f = open('test.txt', 'rb')
#s2 = pickle.load(f)
#f.close()

#s2.show()


#program exam 3
#import os

##print(os.environ)  #환경변수
#print(os.getcwd())
#os.chdir('..')      #Parant directory로 이동
#print(os.getcwd())


#program exam 4
#import os

#print(list(os.walk('..')))


#program exam 5
#import os
#import shutil

#check = True
#for (path, dir, files) in list(os.walk('.')):  #os.getcwd(), '.'는 같은 뜻
#    for d in dir:
#        if d == 'sample':
#            check = False
#    if check == True:
#        os.mkdir('sample')
#    for filename in files:
#        (s1, s2) = filename.split('.')
#        if s2 == 'txt':
#            shutil.copy(filename, 'sample/'+filename)


#program exam 6
import os

print(os.path.dirname('C:\\python34/파일명.확장자'))
print(os.path.expanduser('~\\파일명.확장자'))
print(os.path.expandvars('$JAVA_HOME\\파일명.확장자'))