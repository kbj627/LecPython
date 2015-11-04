import re

def password(p) :
    print(len(p))
    if re.match(r'[0-9, a-z, A-Z, !@#$%\^&*]{8,13}?', p) == None :
        print('1', re.match(r'[0-9, a-z, A-Z, !@#$%\^&*]{8,13}', p))
        return
    if re.match('[0-9]*', p) == None :
        print('2', re.match('[0-9]', p))
        return
    if re.match('[a-z,A-Z]*', p) == None :
        print('3', re.match('[a-z,A-Z]', p))
        return
    if re.match(r'[!@#$%\^&*]*', p) == None :
        print('4', re.match(r'[!@#$%\^&*]', p))
        return
    print('적합')

password('asdf1234!@#^a')