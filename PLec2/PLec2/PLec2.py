#program exam 1
#data = ['a', 'b', 'c', ['abcd', 'efg', '한글']]
#data2 = ['test', data]
#print(data[0])
#print(data[-1])
#print(data[-1][0])
#print(data[-1][1])
#print(data2)
#print(data2[-1][-1][-1])

#program exam 2
#b = [1,2,3]
#c = ['life', 'is', 'too', 'short']
#f = b + c
#print(b + c)
#print(c * 3)

#program exam 3
#guest = ['a','b','c','d']
#guest[0] = 'greenjoa'
#guest[1] = ['greenjoa1','greenjoa2']
#guest[2:3] = ['greenjoa1','greenjoa2']
#print(guest)

#guest = ['a','b','c','d']
#guest.insert(2,'e')
#print(guest)

#guest = ['a','b','c','d']
#guest.append('greenjoa2')
#print(guest)

#guest = ['a','b','c','d']
#guest.remove('c')
#print(guest)

#guest = ['a','b','c','d']
#guest[1:2] = []
#print(guest)

#guest = ['a','b','c','d']
#del guest[0]
#print(guest)

#guest = ['a','b','c','d']
#print(guest.index('c'))

#program exam 4
#id = ['greenjoa1', 'greenjoa2', 'greenjoa3']
#pw = ['12345', '7890', 'abcd']
#phone = ['000-1111-2222', '333-4444-5555', '777-8888-9999']

#id.insert(id.index('greenjoa1')+1, pw[0])
#id.insert(id.index('greenjoa2')+1, pw[1])
#id.insert(id.index('greenjoa3')+1, pw[2])
#print(id)

#id.insert(id.index('greenjoa1')+2, phone[0])
#id.insert(id.index('greenjoa2')+2, phone[1])
#id.insert(id.index('greenjoa3')+2, phone[2])
#print(id)

#program exam 5
#guests = ['a','b','c','d']
#for steps in range(4) :
#    print(guests[steps])
#nEntries = len(guests)
#for steps in range(nEntries) :
#    print(guests[steps])
#print(nEntries)
#for guest in guests :
#    print(guest)
#print(guest)

#program exam 6
#score = [85, 62, 63, 45, 90, 15, 30, 25, 60, 50]
#score.sort();
#print(score)
#score.reverse();
#print(score)
#print('top5 = ', score[0:5])

#program exam 7
#data = ['a', 'b', 'c', ['abcd', 'efg', '한글']]
#for steps in data :
#    if isinstance(steps, list) :
#        for step in steps :
#            print(step)
#    else :
#        print(steps)

#program exam 8
score = [85, 62, 63, 45, 90]
score.extend([50,60])
print(score)
score = [85, 62, 63, 45, 90]
score.append([50,60])
print(score)
# append와 다른점 : append는 리스트 형태로 붙이고, extend는 병합한다.