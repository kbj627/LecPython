import os
import xlsxwriter


def readText(fileName) :
    check = []
    flag = True

    try :
        with open(fileName, 'r') as file :
            for part in file :
                (feild1, feild2, feild3, feild4) = part.split('|', 3)
                for val in check :
                    if val == feild3 :
                        flag = False
                        break;
                if flag == True :
                    check.append(feild3)
                    print(feild3)
                else :
                    flag = True
        file.close()
    except :
        print('File not found')

def createXlsx(t_fileName, str) :
    row = 0
    col = 0
    workbook = xlsxwriter.Workbook(str+'.xlsx')
    worksheet = workbook.add_worksheet()

    with open(t_fileName, 'r') as file :
        for part in file :
            (feild1, feild2, feild3, feild4) = part.split('|', 3)
            if (feild3 == str.upper()) :
                worksheet.write(row, col,     feild1)
                worksheet.write(row, col + 1, feild2)
                worksheet.write(row, col + 2, feild3)
                worksheet.write(row, col + 3, feild4)
                row += 1
    file.close()
    workbook.close()



readText('201401.txt')
str = input('찾을 값을 입력해주세요.')
createXlsx('201401.txt', str)
print(str+'.xlsx 파일이 생성되었습니다.')