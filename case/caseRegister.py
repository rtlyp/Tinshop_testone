from service.register import register


class case:
    def __init__(self,wd):
        self.re=register(wd)
        self.wd=wd

    def caseRegisterone(self,params):
        self.wd.get('http://192.168.10.200/TinyShop_v1.7/index.php?con=index&act=index')
        self.re.registerment(params[0],params[1],params[2])
        text=''
        try:
            text = self.wd.find_element_by_xpath('/html/body/div[2]/div/div/div[1]').text

        except Exception as e:
            print(e,'firstexception')
           #返回首页
        # self.wd.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/a[1]').click()
        #
        # self.wd.find_element_by_xpath('//a[@href="/TinyShop_v1.7/index.php?con=simple&act=logout"]').click()
        return text



    def caseRegistertwo(self, params):
        self.wd.get('http://192.168.10.200/TinyShop_v1.7/index.php?con=index&act=index')
        self.re.registerment(params[0], params[1], params[2])

        text = ''
        try:
            text = self.wd.find_element_by_xpath('//dd//label[@class="invalid-msg"]').text
        except Exception as e:
            print(e, 'firstexception')
        return text

    def caseRegisterthree(self, params):
        self.wd.get('http://192.168.10.200/TinyShop_v1.7/index.php?con=index&act=index')
        self.re.registerment(params[0], params[1], params[2])
        text = ''

        try:
            text = self.wd.find_element_by_xpath('//div[@ class="mt20 login box clearfix"]//div[@class="fl login-form mt20"]//label[@class="invalid-msg"]').text

        except Exception as e:
            print(e, 'firstexception')

        return text

    def caseRegisterfour(self, params):
        self.wd.get('http://192.168.10.200/TinyShop_v1.7/index.php?con=index&act=index')
        self.re.registerment(params[0], params[1], params[2])
        text = ''

        try:
            text = self.wd.find_element_by_xpath('//form[@callback="checkReadme"]//dd//label[class="invalid-msg"]').text

        except Exception as e:
            print(e, 'firstexception')

        return text
