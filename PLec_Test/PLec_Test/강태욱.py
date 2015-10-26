import os
import sys
import time


class MidTest:
    def __init__(self, number, name):
        self.number = number
        self.name = name

    def question1(self):
        print('1) 학번 : '+self.number+', 이름 : '+self.name)

    def question2(self, dic, num):
        max = 0

    def question3(self, file):
        if (os._exists('score') == True):
            os.mkdir('./score')
        liststr = []
        for (path, dir, files) in list(os.walk('./score')):
            for item in files:
                (name, etc) = os.path.splitext(item)
                if etc == '.txt':
                    myFile = open('./score/'+item, mode = "r")
                    str = myFile.read()
                    liststr.append(str)
                    myFile.close()
        
        myFile = open('./score/'+file, mode = "w+")
        for item in liststr:
            myFile.write(item)
        myFile.close()

        print('3) '+file+'생성이 완료되었습니다.')

    def question4(self, file):
        try:
            myFile = open('./score/'+file, mode = "r")
        except FileNotFoundError:
            print(sys.exc_info())

    def question5():
        print(time.strftime('5) Current Time : %Y.%m.%d. %I:%M:%S', time.localtime()))


greenjoa = MidTest('201111256', '강태욱')
greenjoa.question1()

data = {'명량':4.5, '베테랑':4.0, '암살':4.6, '마션':4.3}
greenjoa.question2(data, 2)

greenjoa.question3('question3.txt')

greenjoa.question4('question3.txt')

MidTest.question5()