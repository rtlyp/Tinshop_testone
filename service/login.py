import time

from common.setup import setup


class Login_service:
    def __init__(self,wd):
        self.wd=wd

    def login_in(self,email,password):

        self.wd.find_element_by_xpath('//div[@class="wrap nav"]//b').click()
        print('==========================logintest=',str(password))
        self.wd.find_element_by_id("email").clear()
        self.wd.find_element_by_id("email").send_keys(email)
        self.wd.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/form/dl[2]/dd/input').clear()
        self.wd.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/form/dl[2]/dd/input').send_keys((password))
        time.sleep(2)
        self.wd.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/form/dl[4]/dd/input").click()
        self.wd.maximize_window()

# if __name__=="__main__":
#     wd=setup().get_driver('http://192.168.191.200/TinyShop_v1.7/index.php?con=simple&act=login')
#     Login_service().login_in(wd)