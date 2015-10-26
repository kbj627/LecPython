#program exam 1
#dic1 = {}
#dic2 = dict() #새로운 빈 directory
#dic = {'name':'pey', 'phone':'0119993323', 'birth':'1118'}
#a = {1:'hi'}
#b = {'a':[1,2,3]}
#print(a[1])
#print(b['a'])
#print(dic['name'])

#program exam 2
#a = {'name':'pey', 'phone':'0119993323', 'birth':'1118'}
#b = a.keys()
#print(b)
##결과를 list형으로 받는 함수 list()
#b = list(a.keys())
#print(b)
############################################################
#a = {'name':'pey', 'phone':'0119993323', 'birth':'1118'}
#b = a.values()
#print(b)
#b = list(a.values())
#print(b)

#program exam 3
#a = {'name':'pey', 'phone':'0119993323', 'birth':'1118'}
#b = a.items()
#print(b)
#a.clear()
#a.get('name')
#a.get('foo', 'bar')

#program exam 4
#a = {'홍길동': {'베테랑': 5.0, '암살': 4.5, '미니언즈': 5.0}, '고길동': {'베테랑': 4.0, '암살': 3.5, '미니언즈': 5.0}}
#print('홍길동 : ', a.get('홍길동'))
#print('홍길동 암살 평점 :', a.get('홍길동').get('암살'))
#print('고길동 : ', a.get('고길동'))

#program exam 5
#answer = input('Would you like express shipping?')
#if answer.lower() == 'yes':
#    print("That will be an extra $10")

#program exam 6
#a = [(1,2), (3,4), (5,6)]
#for (first, last) in a:
#    print(first + last)

#program exam 7
#for i in range(2,10):
#    for j in range(1,10):
#        print('%2d *'%i, '%2d'%j, '=', i*j, end=' ')
#    print('')

#program exam 8
#import turtle
#select = input("1.사각형 2.사각형*16 3.오각형 4.사각형(색)")

#if select == '1':
#    for step in range(4):
#        turtle.forward(100)
#        turtle.right(90)
#elif select == '2':
#    for step in range(4):
#        turtle.forward(100)
#        turtle.right(90)
#        for step in range(4):
#            turtle.forward(100)
#            turtle.right(90)
#elif select == '3':
#    nSide = 5
#    for step in range(nSide):
#        turtle.forward(100)
#        turtle.right(360/nSide)
#        for morestep in range(nSide):
#            turtle.forward(50)
#            turtle.right(360/nSide)
#elif select == '4':
#    for step in ['red', 'blue', 'green', 'black']:
#        turtle.color(step)
#        turtle.forward(100)
#        turtle.right(90)