class commonHelp:
    @staticmethod
    def compare(realReault,exptResult):
        if realReault==exptResult:
            return 'pass'
        else:
            return 'fail'

    def writeLog(self,num,Result,expResult):
        result = '第%d条数据执行结果：%s，结果:%s' % ( num,Result, commonHelp.compare(Result, expResult))
        print(result)
        print()