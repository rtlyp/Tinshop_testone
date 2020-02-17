from common.login import Login
from common.setup import setup
from service.refund import myRefund

class case:
    def __init__(self,wd):
        self.re=myRefund(wd)
        self.wd=wd

    def caseRefund_testone(self,params):
        self.re.refundment(params[0],params[1])
        text=''
        try:
            text=self.wd.find_element_by_xpath('//div[@class="content clearfix uc-content"]//div[@class="box p10"]//div[@class="message_warning ie6png"]').text

        except Exception as e:
            print(e,'firstexception')
        return text

    def caseRefund_testtwo(self,params):
        self.re.refundment(params[0], params[1])
        text=''
        try:
            text = self.wd.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/div[1]').text

        except Exception as e:
            print(e,'secondexception')

        return text

    def caseRefund_testthree(self, params):
        self.re.refundment(params[0], params[1])
        text = ''
        try:
            text = self.wd.find_element_by_xpath('//div[@class="content clearfix uc-content"]//div[@class="box p10"]//div[@ class="message_warning ie6png"]').text

        except Exception as e:
            print(e, 'secondexception')

        return text

    def caseRefund_testfour(self, params):
        self.re.refundment(params[0], params[1])
        text = ''
        try:
            text = self.wd.find_element_by_xpath('//table[@class="form"]//label[@ class="invalid-msg"]').text

        except Exception as e:
            print(e, 'secondexception')

        return text

    def caseRefund_testfive(self, params):
        self.re.refundment(params[0], params[1])
        text = ''
        try:
            text = self.wd.find_element_by_xpath('//table[@class="form"]//label[@ class="invalid-msg"]').text

        except Exception as e:
            print(e, 'secondexception')

        return text

    def caseRefund_testsix(self, params):
        self.re.refundment(params[0], params[1])
        text = ''
        try:
            text = self.wd.find_element_by_xpath('//table[@ class="form"]//td//label[@class="invalid-msg"]').text

        except Exception as e:
            print(e, 'secondexception')

        return text

    def caseRefund_testseven(self, params):
        self.re.refundment(params[0], params[1])
        text = ''
        try:
            text = self.wd.find_element_by_xpath('//div[@class="mt10 clearfix"]//div[@class="content clearfix uc-content"]//div[@class="message_warning ie6png"]').text

        except Exception as e:
            print(e, 'secondexception')

        return text

    def caseRefund_testeight(self, params):
        self.re.refundment(params[0], params[1])
        text = ''
        try:
            text = self.wd.find_element_by_xpath(
                '//div[@class="content clearfix uc-content"]//div[@class="box p10"]//div[@ class="message_warning ie6png"]').text

        except Exception as e:
            print(e, 'secondexception')

        return text

# if __name__=='__main__':
#     url='http://192.168.0.200/TinyShop_v1.7/index.php?con=simple&act=login'
#
#     wd=setup().get_driver(url)
#     Login().login_in(wd)
#
#     myRefund(wd).refundment(20180326024216779932,'dgahjrsfkidfl')
#     case(wd).caseRefund_test()