#program exam 1
#class movie :
#    title = ''
#    director = ''

#    def __init__(self, title, director) :
#        self.title = title
#        self.director = director

#    def showInfo(self) :
#        print('Title : ', self.title, 'Director : ', self.director)

#m = movie('암살', '아몰랑')
#m.actor = '???'
#m2 = movie('사도', '아몰랑')

#m.showInfo()
#print(m.actor)
#m2.showInfo()
#print(m2.actor) #error

#program exam 2
#class movie :
#    title = '암살'
#    director = '최동훈'

#    def __init__(self, title, director) :
#        self.title = title
#        self.director = director

#    def showInfo(self) :
#        print('Title : ', self.title, 'Director : ', self.director)

#m1 = movie('베테랑', '류승환')
#print(m1.title)
#print(m1.__class__.title)   #class templet에 접근하는 속성 __class__

#program exam 3
#class movie :
#    '''영화 클래스입니다.'''   #doc에 쓰여짐.
#    title = '암살'
#    director = '최동훈'

#    def __init__(self, title, director) :
#        self.title = title
#        self.director = director

#    def showInfo(self) :
#        print('Title : ', self.title, 'Director : ', self.director)
        
#m1 = movie('베테랑', '류승환')
#print(m1.__doc__)

#program exam 4
#class movie :
#    title = '암살'
#    director = '최동훈'

#    def __init__(self, title, director) :
#        self.title = title
#        self.director = director
#        print(self.title, ' 생성자 호출')

#    def __del__(self) :
#        print(self.title, ' 소멸자 호출')

#    def showInfo(self) :
#        print('Title : ', self.title, 'Director : ', self.director)
        
#m1 = movie('베테랑1', '류승환')
#m2 = movie('베테랑2', '류승환')
#m3 = movie('베테랑3', '류승환')
#m4 = movie('베테랑4', '류승환')
#print(type(m4))
#m4 = m3                 #m4의 인스턴스 객체가 끊어짐(소멸자 호출)
#m4.showInfo()
#print(id(m3), id(m4))

#program exam 5
class movie :
    count = 0
    title = '암살'
    director = '최동훈'

    def __init__(self, title, director) :
        movie.count += 1
        self.title = title
        self.director = director
        print(self.title, ' 생성자 호출')

    def __del__(self) :
        print(self.title, ' 소멸자 호출')

    def showInfo(self) :
        print('Title : ', self.title, 'Director : ', self.director)

    @staticmethod
    def showCount1() :
        print(movie.count)
        
    @classmethod
    def showCount2(cls) :
        print(cls.count)

m1 = movie('a', 'b')
m2 = movie('c', 'd')
m3 = movie('a', 'b')
m4 = movie('a', 'b')
m5 = movie('a', 'b')

movie.showCount1()
movie.showCount2()