from service.login import Login_service


class case:
    def __init__(self,wd):
        self.wd=wd
        self.lg=Login_service(wd)
    def caseLoginone(self,params):
        self.lg.login_in(params[0],params[1])
        flag=''
        try:

            text=self.wd.find_element_by_link_text('安全退出').text
            print(text,'========================')
            if '安全退出'in text:
                flag = '登录成功'
            else:
                flag="登录失败"

        except Exception as e:
            print(e,'firsterror')
            flag = "登录失败"

        return flag
                                       