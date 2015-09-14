#coding:cp949
#프로그램을 cp949모드로 실해한다는 뜻(Python 기본은 UTF-8

#program exam 1
#def sum_and_mul(a, b) :
#    return a+b, a*b

#answer = sum_and_mul(10,30)
#sum, mul = sum_and_mul(10,30)

#print('answer = ', answer, '\nsum : ', sum, '\nmul : ', mul)

#program exam 2
#import PrintData
            
#data = ['홍길동', ['베테랑', '암살'], '고길동', ['베테랑', '암살', '미니언즈'], '김길동', ['베테랑']]
#data2 = ['홍길동', ['베테랑', ['류승환', '황정민', '유아인'], '암살'], '고길동', ['베테랑', '암살', '미니언즈'], '김길동', ['베테랑']]
#PrintData.printData(data)
#PrintData.printData2(data2)

#program exam3
import os

#print(os.getcwd())
#os.mkdir('sample')
os.chdir('.//sample')
#print(os.getcwd())
#os.system('python setup.py sdist') #배포 패키지 만드는 명령
#os.system('python setup.py install') #배포 패키지를 인스톨하는 명령