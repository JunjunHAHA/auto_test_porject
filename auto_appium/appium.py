#coding=utf-8
from appium import webdriver
import time

android = {
    'platformName':'android',
    'deviceName':'127.0.0.1:62001',
    'appPackage':'lawu.company.lawuapp',
    'appActivity':'lawu.company.lawuapp.MainActivity',
    'unicodeKeyboard':True, # 键盘事件
    'resetKeyboard':True # # 键盘事件
    }

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",android)
driver.implicitly_wait(10)

#判断是否以及处于登录状态
driver.find_element_by_id("lawu.company.lawuapp:id/ActivityMainTabMe").click()
try:
    ele = driver.find_element_by_id("lawu.company.lawuapp:id/MeSetting")
except Exception:
    #登录部分    
    driver.find_element_by_id("lawu.company.lawuapp:id/LoginUserED").clear()
    driver.find_element_by_id("lawu.company.lawuapp:id/LoginUserED").send_keys("13418685311")
    driver.find_element_by_id("lawu.company.lawuapp:id/LoginPwdED").send_keys("123456")
    driver.find_element_by_id("lawu.company.lawuapp:id/LoginBtn").click()
else:
    driver.find_element_by_id("lawu.company.lawuapp:id/ActivityMainTabShopping").click()

#在首页的搜索框中输入酸奶，点击搜索
driver.find_element_by_name("搜索你想要的").click()
driver.find_element_by_name("搜索你想要的宝贝").send_keys(u"酸奶")
#使用组合定位的方式
time.sleep(2)
driver.find_element_by_android_uiautomator('new UiSelector().text("酸奶").resourceId("lawu.company.lawuapp:id/itemHomeSearchTypeTv")').click()
driver.find_element_by_android_uiautomator('new UiSelector().textContains("安慕希")').click()

#购物车的操作
driver.find_element_by_id("lawu.company.lawuapp:id/GoodsDetailAddCartTv").click()
driver.find_element_by_id("lawu.company.lawuapp:id/GoodsDetailSelectTypeAddIv")

while True:
    ele = driver.find_element_by_id("lawu.company.lawuapp:id/GoodsDetailSelectTypeNumTv")
    if ele.text == "5":
        break
    else:
        driver.find_element_by_id("lawu.company.lawuapp:id/GoodsDetailSelectTypeAddIv").click()
driver.find_element_by_id("lawu.company.lawuapp:id/GoodsDetailSelectTypeNowBuyTv").click()

driver.find_element_by_id("lawu.company.lawuapp:id/GoodsDetailCartIv").click()

driver.find_element_by_id("lawu.company.lawuapp:id/CartSelectGoodsIv").click()

while True:
    ele = driver.find_element_by_id("lawu.company.lawuapp:id/CartGoodsNumIv")
    if int(ele.text) > 5:
        driver.find_element_by_id("lawu.company.lawuapp:id/CartGoodsJianIv").click()
    elif int(ele.text) < 5:
        driver.find_element_by_id("lawu.company.lawuapp:id/CartGoodsAddIv").click()
    else:
        break

driver.find_element_by_name("结算").click()
ele = driver.find_element_by_id("lawu.company.lawuapp:id/SureOrderMoneyTv")
if ele.text == u"实付款：¥325.0":
    print "pass"
else:
    print "fail"

    

