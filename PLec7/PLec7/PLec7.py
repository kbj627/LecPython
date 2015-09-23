#program exam 1
#from abc import ABCMeta, abstractmethod

#class terran(metaclass = ABCMeta) :
#    def __init__(self, name) :
#        self.name = name
#    @abstractmethod
#    def attack(self) :
#        pass

#class tank (terran) :
#    def __init__(self, name, damage):
#        super().__init__(name)
#        self.damage = damage
#    def attack(self):
#        print(self.name + '\'s attack')

#class marine(terran) :
#    def __init__(self, name, hp):
#        super().__init__(name)
#        self.hp = hp
#    def attack(self):
#        print(self.name + '\'s attack')

#def Attack(terran) :
#    terran.attack()

#t1 = tank('tank', 0)
#t2 = marine('marine', 100)

#tlist = [tank('tank1', 0), tank('tank2', 0), marine('marine1', 100)]
#for item in tlist :
#    Attack(item)
#Attack(t1)
#Attack(t2)


#program exam 2
class MyList(list) :
    name = ''
    def __init__(self, name) :
        super().__init__([])
        self.name = name

    def __str__(self, **kwargs):
        return self.name + ' : ' + super().__str__(**kwargs)

list1 = MyList('greenjoa')
list1.append(10)
list1.append(50)
list1.append(60)
list1.append(70)
list1.append(80)
list1.append(100)

print(list1)