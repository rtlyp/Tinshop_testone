# coding=UTF-8
import sys

# from common.login import Login
from common.setup import setup
from common.util import commonHelp
from data.readexcel import read


class mainMethod:
    #打开浏览武器
    def __init__(self,path,index,url):
        self.path=path
        self.index=index
        self.url=url
        st=setup()
        self.wd=st.get_driver(self.url)
    #登录
    # def exeLogin(self):
    #     ty=Login()
    #     ty.login_in(self.wd)
    def ex_Exit(self):
        self.wd.close()
        # self.wd.Dispose()
    #表格
    def exeCheck(self):
        re=read()
        sheet=re.getExcelsheet(self.path,self.index)
        coh=commonHelp()

        for i in range(1,sheet.nrows):
            li = sheet.row_values(i)
            # print(li, 'test00')

            #导入模块
            __import__(li[0])
            mod=sys.modules[li[0]]
            # 引入模块下的类
            obj=getattr(mod,li[1])

            #引入方法
            mtd=getattr(obj(self.wd),li[2])
            # print('test3')
            newli=li[4:20]
            flag=mtd(newli)

            #程序执行的结果
            coh.compare(li[3],flag)
            #
            coh.writeLog(i,flag,li[3])

if __name__=="__main__":
    path=r'C:\Users\Administrator\Desktop\tinyshop.xls'
    index=2
    url='http://192.168.1.200/TinyShop_v1.7/index.php?con=index&act=index'
    M=mainMethod(path,index,url)
    # M.exeLogin()
    M.exeCheck()
    # M.ex_Exit()


