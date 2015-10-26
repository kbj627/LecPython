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
#import os

#print(os.path.dirname('C:\\python34/파일명.확장자'))
#print(os.path.expanduser('~\\파일명.확장자'))
#print(os.path.expandvars('$JAVA_HOME\\파일명.확장자'))


#program exam 7
#import glob

#print(glob.glob('./tes?.*'))
#print(list(glob.iglob('*.*')))


#program exam 8
#import glob, os.path

#ndir = nfile = 0

#def traverse(dir, depth):
#    global ndir, nfile
#    for obj in glob.glob(dir + '/*'):
#        if depth == 0:
#            prefix = '|--'
#        else:
#            prefix = '|' + ' ' * depth + '|--'
#        if os.path.isdir(obj):
#            ndir += 1
#            print(prefix + os.path.basename(obj))
#            traverse(obj, depth+1)
#        elif os.path.isfile(obj) :
#            nfile +=1
#            print(prefix + os.path.basename(obj))
#        else:
#            print(prefix + 'unknown object:',obj)

#if __name__ == '__main__':
#    traverse('..', 0)
#    print('\n',ndir,'directories,',nfile, 'files')


#program exam 9
#import tempfile

#with tempfile.TemporaryFile('w+') as fp:
#    fp.write('Hello world!')
#    fp.seek(0)
#    data = fp.read()
#    print(data)
#    print(fp.name)


#program exam 10
#import time

#print(time.strftime('%B %dth %A %H:%M', time.localtime()))
#print(time.strftime('%Y-%m-%d %H:%M', time.localtime()))
#print(time.localtime())

#t1 = time.ctime(1234567)
#print(time.strptime(t1))
#print(time.strftime('%B %dth %A %H:%M', time.strptime(t1)))
#print(time.strftime('%Y-%m-%d %H:%M', time.strptime(t1)))


#program exam 11
#import calendar

#calendar.prmonth(2015, 10)
#print(calendar.monthrange(1993,1))


#program exam 12
#import random

#l = random.sample(range(100), 10)
#random.shuffle(l)
#print(random.choice(l))


#program exam 13
#import random

#data = [('Red', 3), ('Blue', 1), ('Green', 4), ('Yellow', 2)]
#datalist = []

#for val, cnt in data:
#    for i in range(cnt):
#        datalist.append(val)
#print(datalist)

#datalist = [val for val, cnt in data for i in range(cnt)]
#print(datalist)


#program exam 14
#import webbrowser
#url = 'http://google.com'
#webbrowser.open_new_tab(url)
#webbrowser.open_new(url)
