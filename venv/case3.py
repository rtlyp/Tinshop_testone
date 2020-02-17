# 后台上架商品前台有显示
from  selenium import  webdriver
import  time
wb=webdriver.Firefox() #搭建链接
wb.implicitly_wait(5) #隐式等待5秒
wb.get('http://192.168.10.154/TinyShop_v1.7/index.php?con=order&act=order_list')
wb.find_element_by_xpath('/html/body/div/div/form/ul/li[1]/input').send_keys('admin')
wb.find_element_by_xpath('/html/body/div/div/form/ul/li[2]/input').send_keys('123456')
wb.find_element_by_xpath('/html/body/div/div/form/ul/li[3]/input').send_keys('aaaa')
wb.find_element_by_xpath('/html/body/div/div/form/ul/li[4]/input[1]').click()
time.sleep(2)
wb.find_element_by_link_text('商品中心').click()
# wb.find_element_by_xpath('/html/body/div[2]/ul/li[1]/a').click()   #点击商品中心
wb.find_element_by_xpath('/html/body/div[3]/div[2]/form/div/a[4]').click()  #点击上架
wb.find_element_by_xpath('/html/body/div[3]/div[2]/form/table/tbody/tr[3]/td[1]/input').click() #勾选商品
wb.find_element_by_xpath('/html/body/div[3]/div[2]/form/div/a[4]').click() #点击上架
wb.refresh()
msg=wb.find_element_by_xpath('/html/body/div[3]/div[2]/form/table/tbody/tr[3]/td[11]/b').text
if '在售' == msg:
    print('商品上架成功！')
else:
    print('上架失败')
