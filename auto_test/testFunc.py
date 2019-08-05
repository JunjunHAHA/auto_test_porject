#coding=utf-8

from selenium import webdriver
import datetime
import time

driver = webdriver.Chrome()
 
def testFindElement(find,position):
    global ele
    try:
        position = position.encode("utf8")
        if find == "id":
            ele = driver.find_element_by_id(position)
        elif find == "name":
            ele = driver.find_element_by_name(position)
        elif find == "xpath":
            ele = driver.find_element_by_xpath(position)
        elif find == "a":
            ele = driver.find_element_by_link_text(position)
    except Exception:
        t = datetime.datetime.today().strftime("%Y%m%d%H%M%S")
        driver.get_screenshot_as_file("E:/autotest/screenshot/%s.png"%t)
        return None
    else:    
        return ele
 
def testOpen(url):    
    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(10)
 
def testInput(find,position,data):
    time.sleep(1)
    ele = testFindElement(find,position)
    if ele == None:
        print ("输入框没有找到")
    else:        
        ele.clear()
        ele.send_keys(data)
    
def testClick(find,position):
    time.sleep(1)
    ele = testFindElement(find,position)
    if ele == None:
        print ("点击的元素没有找到")
    else:
        ele.click()

def testFrame(find,position,status):
    time.sleep(1)
    #状态码为1的时候，切换到子页面
    if status == "1":
        if find == "id" or find == "name":
            driver.switch_to.frame(position)
        else:
            ele = testFindElement(find,position)
            driver.switch_to.frame(ele)
    #状态码为2的时候，跳出到最外层的html       
    elif status == "2":
        driver.switch_to.default_content()
    #状态码为3的时候，切换到父级页面
    elif status == "3":
        driver.switch_to.parent_frame()
        
def testSelect(find,position,data):
    data = data.encode("utf8")
    time.sleep(1)
    from selenium.webdriver.support.select import Select
    ele = testFindElement(find,position)
    if ele == None:
        print("下拉框没有找到")
    else:        
        s = Select(ele)
        s.select_by_visible_text(data)

def testJs(data):
    time.sleep(1)
    driver.execute_script(data)
    
def testWinInput(data):
    data = data.encode("utf8")
    time.sleep(1)
    import SendKeys
    
    SendKeys.SendKeys(data)
    
    
    
    
    
    
    
    
    
    