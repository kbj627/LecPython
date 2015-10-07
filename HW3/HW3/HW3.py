import os
try :
    import xlsxwriter
except ImportError:
    if 'Y' == input('xlsxwriter가 없습니다. 설치 하시겠습니까?(y/n)').upper() :
        os.system('pip install xlsxwriter')
        import xlsxwriter
    else :
        os.sys.exit()

class xlsxUser :
    list = []
    
    
    def __readText(self, fileName) :
        check = []
        flag = True

        try :
            with open(fileName, 'r') as file :
                for part in file :
                    (feild1, feild2, feild3, feild4, trash) = part.split('|', 4)
                    self.list.append([feild1, feild2, feild3, feild4])
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
        except FileNotFoundError:
            print('File not found error')
            return False

        return True


    def __writeXlsx(self, str) :
        row = 0
        col = 0
        workbook = xlsxwriter.Workbook(str+'.xlsx')
        worksheet = workbook.add_worksheet()

        for part in self.list :
            (feild1, feild2, feild3, feild4) = part
            if (feild3 == str.upper()) :
                worksheet.write(row, col,     feild1)
                worksheet.write(row, col + 1, feild2)
                worksheet.write(row, col + 2, feild3)
                worksheet.write(row, col + 3, feild4)
                row += 1
        workbook.close()

    
    def createXlsx(self, FIlename) :
        if self.__readText(FIlename) == True :
            str = input('찾을 값을 입력해주세요.')
            self.__writeXlsx(str)
            print(str + '.xlsx 파일이 생성되었습니다.')


xlsxUser().createXlsx('201401.txt')