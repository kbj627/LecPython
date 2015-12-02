import numpy as np

#data = np.array([[1,2,3,4], [2,3,4,5], [6,7,8,9]])
#print(data.T, '\n')

#print(np.arange(10), '\n')  #  0, . . . n-1
#print(np.arange(10,1,-1), '\n')     # start, end(exclusive), step
#print(np.arange(10,1,-1)[:, np.newaxis], '\n')  #행증가
#print(np.arange(2, 8, dtype=np.float), '\n')
#print(np.arange(35).reshape(5,7), '\n')

#print(np.linspace(1., 4., 6), '\n')   # start, end, num-points
#print(np.linspace(1., 4., 6, endpoint=False), '\n')

#data = np.random.rand(4)
#print(data, '\n')
#data = np.random.randn(4)   # Gaussian
#print(data, '\n')


from matplotlib import pyplot as plt

#data = np.loadtxt('data.txt')
#year, hares, lynxes, carrots = data.T
#print(data[1:4:2, ::3])
##plt.plot(year, hares, year, lynxes, year, carrots)
##plt.show()

#x = np.arange(10,1,-1)
#print(x[np.array([3, 3, 1, 8])])
#print(x[np.array([[1,1],[2,3]])])

#y = np.arange(35).reshape(5,7)
#print(y[np.array([0,2,4])])
#b = y>20    # b에 결과가 아닌 y>20 자체가 들어간다.
#print(y[b])


data = np.arange(60).reshape(6,10)
print(data, '\n')

mask = np.array([0,1,2,3,4,5])
data = data[mask, 0:6]
print(data, '\n')

mask = np.array(np.array([1,0,1,0,0,1],dtype=bool))
print(data[mask, 2], '\n')

mask1 = np.array([0,1,2,3,4])
mask2 = np.array([1,2,3,4,5])
print(data[mask1,mask2], '\n')

mask3 = np.array([0,2,5])
print(data[3:6, mask3], '\n')