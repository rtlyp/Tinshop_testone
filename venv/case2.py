# 新增会员成功后台显示人数+1
from  selenium import  webdriver
import  time
wb=webdriver.Firefox() #搭建链接
wb.implicitly_wait(5) #隐式等待5秒
wb.get('http://192.168.10.147/TinyShop_v1.7/index.php?con=admin&act=index')
wb.find_element_by_xpath('/html/body/div/div/form/ul/li[1]/input').send_keys('admin')
wb.find_element_by_xpath('/html/body/div/div/form/ul/li[2]/input').send_keys('123456')
wb.find_element_by_xpath('/html/body/div/div/form/ul/li[3]/input').send_keys('aaaa')
wb.find_element_by_xpath('/html/body/div/div/form/ul/li[4]/input[1]').click()
content=wb.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[3]/table/tbody/tr[1]/td[1]').text #会员人数
print('当前会员人数：'+content)
time.sleep(2)


wb.get('http://192.168.10.147/TinyShop_v1.7/')
wb.find_element_by_xpath('/html/body/div[1]/div[1]/div/ul/li[2]/a').click()
wb.find_element_by_id('email').send_keys('11@qq.com')
wb.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[2]/form/dl[2]/dd/input').send_keys('123456')
wb.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[2]/form/dl[3]/dd/input').send_keys('123456')
wb.find_element_by_id('verifyCode').send_keys('aaaa')
wb.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[2]/form/dl[5]/dd/input').click()
wb.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[2]/form/dl[6]/dd/input').click()
meg=wb.find_element_by_xpath('/html/body/div[2]/div/div/div[1]').text
if '恭喜您，注册成功！' == meg:
    print('注册账号成功')
else:
    print('注册失败！')
wb.close()
time.sleep(2)

wb1=webdriver.Firefox() #搭建链接
wb1.get('http://192.168.10.147/TinyShop_v1.7/index.php?con=admin&act=index')
wb1.find_element_by_xpath('/html/body/div/div/form/ul/li[1]/input').send_keys('admin')
wb1.find_element_by_xpath('/html/body/div/div/form/ul/li[2]/input').send_keys('123456')
wb1.find_element_by_xpath('/html/body/div/div/form/ul/li[3]/input').send_keys('aaaa')
wb1.find_element_by_xpath('/html/body/div/div/form/ul/li[4]/input[1]').click()
wb1.refresh()
content1=wb1.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[3]/table/tbody/tr[1]/td[1]').text #会员人数
print('当前会员人数：'+content1)
if content1>content:
    print('successful')
else:
    print('fail')


