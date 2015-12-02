import numpy as np


#data = np.array([[1,2,3],[4,5,6],[7,8,9]])

#print(data+2)
#print(data-2)
#print(data*data)
#print(data/3)
#print(data**2)
#print(data**0.5)
#print(data.dot(data))

#a = np.array([1, 2, 3, 4])
#b = np.array([4, 2, 2, 4])
#print(a == b)
#print(a > b)

#a = np.array([1, 2, 3, 4])
#b = np.array([4, 2, 2, 4])
#c = np.array([1, 2, 3, 4])
#print(np.array_equal(a, b))
#print(np.array_equal(a, c))

#a = np.array([1, 1, 0, 0], dtype=bool)
#b = np.array([1, 0, 1, 0], dtype=bool)
#print('np.logical_or :', np.logical_or(a, b))
#print('np.logical_and :', np.logical_and(a, b))
#print('np.all([True, True, False]) :', np.all([True, True, False]))
#print('np.any([True, True, False]) :', np.any([True, True, False]))

#a = np.arange(5)
#print(np.sin(a))
#print(np.log(a))
#print(np.exp(a))

#a = np.triu(np.ones((3, 3)), 1)
#print(a.T)

#x = np.array([1, 2, 3, 4])
#print(np.sum(x))   # np객체의 sum이나 np객체를 레퍼런스하는 x의 sum이나 같다.
#print(x.sum())

#x = np.array([[1, 1],[ 2, 2]])
#print(x.sum())          #all
#print(x.sum(axis=0))    #columns (first dimension)
#print(x.sum(axis=1))    #rows (second dimension)
#print((x[0, :].sum(), x[1, :].sum()))

#x = np.array([1, 3, 2])
#print(x.min())
#print(x.max())
#print(x.argmin()) # index of minimum
#print(x.argmax()) # index of maximum


#x = np.array([1, 2, 3, 1])
#y = np.array([[1, 2, 3], [5, 6, 1]])
#print(x.mean())     #값들의 평균
#print(np.median(x)) #값들의 중간값
#print(np.median(y, axis=-1)) # last axis
#print(x.std()) # full population standard dev (표준 편차)


#data = np.loadtxt('data.txt')
#year, hares, lynxes, carrots = data.T

#print('토끼 평균 :', hares.mean())
#print('시라소니 평균 :', lynxes.mean())
#print('당근 평균 :', carrots.mean())

#print('토끼 표준편차 :', hares.std())
#print('시라소니 표준편차 :', lynxes.std())
#print('당근 표준편차 :', carrots.std())

#print('토끼 최대 수 년도, 최대값 :', year[hares.argmax()], hares.max())
#print('시라소니 최대 수 년도, 최대값 :', year[lynxes.argmax()], lynxes.max())
#print('당근 최대 수 년도, 최대값 :', year[carrots.argmax()], carrots.max())

data = np.array([[0,1,2,3,4,5]]).T
print(data + [10,20,30,40,50])