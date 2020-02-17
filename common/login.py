# coding=UTF-8
import time

from common.setup import setup

class Login:
    def login_in(self,wd):
        wd.find_element_by_id("email").clear()
        wd.find_element_by_id("email").send_keys("12345@qq.com")
        wd.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/form/dl[2]/dd/input').clear()
        wd.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/form/dl[2]/dd/input').send_keys("123456")
        time.sleep(2)
        wd.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/form/dl[4]/dd/input").click()
        wd.maximize_window()


if __name__ == "__main__":
    st = setup()
    url = 'http://192.168.191.200/TinyShop_v1.7/index.php?con=simple&act=login'
    wd=st.get_driver(url)
    Login().login_in(wd)