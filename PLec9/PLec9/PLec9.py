#program exam 1
#def numcheck(l):
#    return l%2 == 0
#print(list(filter(numcheck, [0,1,2,3,4,5,6])))


#program exam 2
#a = 3
#print(id(3))
#print(id(a))


#program exam 3
#print(list(filter(lambda x : x % 2 == 0, [0,1,2,3,4,5,6])))


#program exam 4
#a = [1,2,3]
#b = list(a)
#c = a
#print('a = ', id(a))
#print('b = ', id(b))
#print('c = ', id(c))


#program exam 5
#print(list(map(lambda a: a*2, [1,2,3,4])))
#print(map(lambda a: a*2, [1,2,3,4]))


#program exam 6
#print(eval(repr("hi".upper())))
#print(eval(str("hi".upper())))


#program exam 7
#list = [1, 2, 3, 5]
#list2 = [123, 35, 12321, 545434, 'gfdsgfds', 'ASD', 'fffffff']

#print(list.sort())
#print(sorted(list))


#program exam 8
#print(list(zip([1,2,3], [4,5,6], [7,8,9])))
#print(list(zip("abc", "def")))


#program exam 9
dic = {'홍길동' : [80, 70, 60, 92],
        '김길동' : [24, 35, 18, 10],
        '고길동' : [10, 20, 8 ,5] }

for item in dic.keys():
    dic[item].sort()
    
print(sorted(dic.items())) #정렬된 dic을 출력한다.