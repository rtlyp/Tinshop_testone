from selenium import webdriver



class setup:
    def get_driver(self,url):
        wd = webdriver.Firefox()
        wd.get(url)
        wd.implicitly_wait(4)
        return wd


# executable_path = 'C:\Program Files\Mozilla Firefox\geckodriver.exe'

# wd = webdriver.Firefox()
# wd.get('http://192.168.10.147/TinyShop_v1.7/index.php?con=simple&act=login')