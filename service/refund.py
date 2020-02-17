from common.setup import setup
from common.login import Login


class myRefund:
    def __init__(self,wd):
        self.wd=wd

    def refundment(self,number,reason):
        self.wd.find_element_by_xpath('//li//a[@href="/TinyShop_v1.7/index.php?con=ucenter&act=refund"]').click()
        self.wd.find_element_by_name('order_no').clear()
        self.wd.find_element_by_name('order_no').send_keys(number)
        self.wd.find_element_by_xpath('//td//textarea[@name="content"]').clear()
        self.wd.find_element_by_xpath('//td//textarea[@name="content"]').send_keys(reason)
        self.wd.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/div[1]/form/table/tbody/tr[7]/td[2]/input').click()
# if __name__=='__main__':
#     url='http://192.168.0.200/TinyShop_v1.7/index.php?con=simple&act=login'
#
#     wd=setup().get_driver(url)
#     Login().login_in(wd)
#
#     myRefund(wd).refundment(20180326024216779932,'dgahjrsfkidfl')






