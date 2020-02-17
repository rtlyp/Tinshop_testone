# 登录购物流程+后台订单显示
from  selenium import  webdriver
import  time
wb=webdriver.Firefox() #搭建链接
wb.implicitly_wait(5) #隐式等待5秒
wb.get('http://192.168.10.147/TinyShop_v1.7/') #获取链接
wb.find_element_by_xpath('/html/body/div[1]/div[1]/div/ul/li[1]/a/b').click() #点击登录
wb.find_element_by_id('email').send_keys('1@qq.com') #账号
wb.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/form/dl[2]/dd/input').send_keys('123456') #密码
wb.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/form/dl[4]/dd/input').click() #登录
wb.find_element_by_xpath('/html/body/div[2]/div/div[3]/dl[1]/dd/ul/li[1]/dl/dt/a/img').click() #点击图片购买商品
wb.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[1]/dl[1]/dd/ul/li[1]').click() #选择颜色
wb.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[1]/dl[2]/dd/ul/li[1]/span').click() #选择尺码
time.sleep(2)
wb.find_element_by_id('add-cart').click() #加入购物车
wb.find_element_by_id('settlement').click() #点击去结算
wb.find_element_by_xpath('/html/body/div[2]/div/div[3]/p/a[2]').click()  #结算
wb.find_element_by_xpath('/html/body/div[3]/div/div[2]/form/div[2]/ul/li/input').click()  #选择支付方式
wb.find_element_by_xpath('/html/body/div[3]/div/div[2]/form/div[6]/p/input').click() #提交订单
wb.find_element_by_xpath('/html/body/div[3]/div/div[2]/form/div[3]/p/input').click() #立即支付

def houtai(self):
        self.wb.get('http://192.168.10.147/TinyShop_v1.7/index.php?con=admin&act=login') #后台链接
        self.wb.find_element_by_xpath('/html/body/div/div/form/ul/li[1]/input').send_keys('admin') #输入账号
        self.wb.find_element_by_xpath('/html/body/div/div/form/ul/li[3]/input').send_keys('aaaa') #输入验证码
        self.wb.fiind_element_by_xpath('/html/body/div/div/form/ul/li[2]/input').send_keys('123456') #输入密码
        self.wb.fnd_element_by_xpath('/html/body/div/div/form/ul/li[4]/input[1]').click() #登录
        self.wb.find_element_by_xpath('/html/body/div[1]/ul/li[2]/a').click() #点击订单中心
        msg=self.wb.find_element_by_xpath('/html/body/div[3]/div[2]/form/table/tbody/tr[2]/td[4]').text
        if '处理' in msg:
            print('后台数据已生成！')
        else:
            print('未找到订单！')
houtai()

