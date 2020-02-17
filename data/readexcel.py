import xlrd
class read:
    def getExcelsheet(self,path,index):
        book=xlrd.open_workbook(path)
        sheet=book.sheets()[index]
        return sheet
