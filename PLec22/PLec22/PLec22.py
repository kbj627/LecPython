import numpy as np
from matplotlib import pyplot as plt

#Lec1
#mileposts = np.array([0, 198, 303, 736, 871, 1175, 1475, 1544, 1913, 2448])
#distance_array = np.abs(mileposts - mileposts[:, np.newaxis])   # mileposts[:, np.newaxis] newaxis는 가로, 세로 행렬을 변경한다.
#print(distance_array)

#x,y = np.arange(5), np.arange(5)[:, np.newaxis]
#distance = np.sqrt(x**2 + y**2)
#print(distance)

#plt.pcolor(distance)
#plt.colorbar()
#plt.show()


#Lec2
# grid에 대한 계산을 다루기 유용

##x : (5,1), y : (1,5) shape을 가짐
#x, y = np.ogrid[0:5, 0:5]
#print(x)
#print(y)

##x,y : (5,5) shape을 가짐
#x, y = np.mgrid[0:5, 0:5]
#print(x)
#print(y)


#Lec3
#a = np.array([[1, 2, 3], [4, 5, 6]])
#print(a.ravel()) #[1,2,3,4,5,6] 1차원으로 쭉 뽑아줌
#print(a.T)
#print(a.T.ravel())

#a.shape
#b = a.ravel()
#print(b)
#b = b.reshape((2, 3))
#print(b)
#b.reshape((2, -1))
#print(b)


#Lec4
#z = np.array([1, 2, 3])
#print(z)
#print(z[:, np.newaxis])
#print(z[np.newaxis, :])


#Lec5
#a = np.arange(4)
#a.resize((8,))
#print(a)


#Lec6
#a = np.array([[4, 3, 5], [1, 2, 1]])
#b = np.sort(a, axis=1) #Sorts each row separately!
#print(a)
#a.sort(axis=0)
#print(a)    # axis=0은 세로 기준
#print(b)    # axis=1은 가로 기준

#a = np.array([4, 3, 1, 2])
#j = np.argsort(a)   # sorting with index
#j_max = np.argmax(a)    # finding maxima
#j_min = np.argmin(a)    # finding minima


#Lec7
#p = np.poly1d([3, 2, -1])
#print(p(0))
#print(p.roots)
#print(p.order)
#p = np.polynomial.Polynomial([-1, 2, 3])
#print(p)


#Lec8
#x = np.linspace(0, 1, 20)
#y = np.cos(x) + 0.3*np.random.rand(20)
#p = np.poly1d(np.polyfit(x, y, 3))
#t = np.linspace(0, 1, 200)
#plt.plot(x, y, 'o', t, p(t), '-')
#plt.show()


#Lec9
#x = np.linspace(-1, 1, 2000)
#y = np.cos(x) + 0.3*np.random.rand(2000)
#p = np.polynomial.Chebyshev.fit(x, y, 90)
#t = np.linspace(-1, 1, 200)
#plt.plot(x, y, 'r.')
#plt.plot(t, p(t), 'k-', lw=3)
#plt.show()


#Lec10
img = plt.imread('image.png')
print(img.shape, img.dtype) #shape는 높이 너비 RGBA(Alpha가없으면 3)
i = np.array(img[0:500] [0:200])
plt.imshow(i)
plt.show()