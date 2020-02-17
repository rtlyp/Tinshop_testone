from common.setup import setup

from common.login import Login

class register:
    def __init__(self,wd):
        self.wd=wd
    def registerment(self,count,pwd,repwd):
        #免费注册
        # self.wd.find_element_by_xpath('//div[@class="login-note mt20"]//a[@class="red"]').click()
        #注册
        # self.wd.find_element_by_xpath('//ul[@class=" fr"]//a[@href="/TinyShop_v1.7/index.php?con=simple&act=reg"]').click()
        self.wd.find_element_by_xpath('/html/body/div[1]/div[1]/div/ul/li[2]/a').click()
        print('mianfeizhuce')
        self.wd.find_element_by_id('email').send_keys(count)
        self.wd.find_element_by_xpath('//dl[@class="clearfix"]//input[@ name="password"]').send_keys(int(pwd))
        self.wd.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[2]/form/dl[3]/dd/input').send_keys(int(repwd))
        self.wd.find_element_by_id('verifyCode').send_keys('aaaa')
        self.wd.find_element_by_id("readme").click()
        self.wd.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[2]/form/dl[6]/dd/input').click()

#
# if __name__=='__main__':
#
#     url='http://192.168.10.200/TinyShop_v1.7/index.php?con=simple&act=login'
#
#     wd=setup().get_driver(url)
#
#     register(wd).registerment('1@qq.com',123456,123456)
