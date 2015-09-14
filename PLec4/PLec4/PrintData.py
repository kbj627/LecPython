def printData(data) :
    for item in data :
        if isinstance(item, list) :
            for item2 in item :
                print(item2)
        else :
            print(item)

def printData2(data, level = 0) :
    for item in data :
        if isinstance(item, list) :
            printData2(item, level+1)
        else :
            for i in range(level) :
                print('\t', end='')
            print(item)