from selenium import webdriver
from selenium.webdriver import ActionChains
import time
import pymysql

driver = webdriver.Chrome()
#browser.implicitly_wait(10) # 等待时间为10seconds

db = pymysql.connect(host = "localhost",port = 3306, user = "root", passwd = "123456",database = "airport", charset="utf8")
# 使用cursor()方法获取操作游标
cursor = db.cursor()
# sql = "delete from ctrip"
# cursor.execute(sql)

j =1
#driver.get("https://flights.ctrip.com/itinerary/oneway/bjs-sha?date=2019-03-05")
driver.get("https://flights.ctrip.com/")

driver.maximize_window()
city = ['','北京','广州','上海','成都']
data = ['','2019-03-20','2019-03-21','2019-03-22','2019-03-17','2019-03-18','2019-03-19']
#price = driver.find_element_by_xpath("//div[@class='inb price child_price lowest_price']/div[1]/span[1]").text

def explicitInfo(n, j):
    i = 1
    #如果网速过慢，页面未加载出来就开始爬取则会找不到元素报错
    # time.sleep(2)
    # company = driver.find_element_by_xpath(
    #     "//div[@class='search_box search_box_tag search_box_light Label_Flight']/div[1]/div[1]/div[1]/div[1]/span[1]/span[1]/strong[1]").text
    # number = driver.find_element_by_xpath(
    #     "//div[@class='search_box search_box_tag search_box_light Label_Flight']/div[1]/div[1]/div[1]/div[1]/span[1]/span[1]/span[1]").text
    # price = driver.find_element_by_xpath(
    #     "//div[@class='search_box search_box_tag search_box_light Label_Flight']/div[1]/div[7]/div[1]/span[1]").text
    # punctualRate = driver.find_element_by_xpath(
    #     "//div[@class='search_box search_box_tag search_box_light Label_Flight']/div[1]/div[5]/div[1]/div[1]/div[1]/span[1]").text
    #
    # model = driver.find_element_by_xpath("//div[@class='search_box search_box_tag search_box_light Label_Flight']/div[1]/div[1]/div[2]/span[1]").text
    # startTime = driver.find_element_by_xpath("//div[@class='search_box search_box_tag search_box_light Label_Flight']/div[1]/div[2]/div[1]/strong[1]").text
    # startAirport = driver.find_element_by_xpath("//div[@class='search_box search_box_tag search_box_light Label_Flight']/div[1]/div[2]/div[2]").text
    # arriveTime = driver.find_element_by_xpath("//div[@class='search_box search_box_tag search_box_light Label_Flight']/div[1]/div[4]/div[1]/strong[1]").text
    # arriveAirport = driver.find_element_by_xpath("//div[@class='search_box search_box_tag search_box_light Label_Flight']/div[1]/div[4]/div[2]").text
    # discount = driver.find_element_by_xpath("//div[@class='search_box search_box_tag search_box_light Label_Flight']/div[1]/div[7]/div[1]/div[1]/div[1]/span[1]").text
    #
    # print("航空公司：%s  航班号: %s 机票价格：%s  准点率%s 飞机型号：%s 出发时间：%s 出发机场：%s 到达时间：%s 到达机场：%s 折扣率：%s" % (company, number, price, punctualRate, model, startTime, startAirport, arriveTime, arriveAirport, discount))
    # create table ctrip(company varchar(20), number varchar(20), price varchar(20), punctualRate varchar(20), model varchar(20), startTime varchar(20), startAirport varchar(20), arriveTime varchar(20), arriveAirport varchar(20), discount varchar(20), date varchar(20));
    # sql = "insert into ctrip(company, number, price, punctualrate, model, starttime, startairport, arrivetime, arriveairport, discount, startdata)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    # cursor.execute(sql,(company, number, price, punctualRate, model, startTime, startAirport, arriveTime, arriveAirport, discount,data[j]))


    while i <= n:
        #time.sleep(2)
        driver.implicitly_wait(5)
        #try的作用是防止航班数量不够导致程序崩溃
        try:
            company = driver.find_element_by_xpath(
                "//div[@class='search_box search_box_tag search_box_light Label_Flight']/following-sibling::div[%d]/div[1]/div[1]/div[1]/div[1]/span[1]/span[1]/strong[1]" % (
                    i)).text
        except:
            break

        number = driver.find_element_by_xpath(
            "//div[@class='search_box search_box_tag search_box_light Label_Flight']/following-sibling::div[%d]/div[1]/div[1]/div[1]/div[1]/span[1]/span[1]/span[1]" % (i)).text
        price = driver.find_element_by_xpath(
            "//div[@class='search_box search_box_tag search_box_light Label_Flight']/following-sibling::div[%d]/div[1]/div[7]/div[1]/span[1]" % (
                i)).text
        try:
            punctualRate = driver.find_element_by_xpath(
                "//div[@class='search_box search_box_tag search_box_light Label_Flight']/following-sibling::div[%d]/div[1]/div[5]/div[1]/div[1]/div[1]/span[1]" % (
                    i)).text
        except:
            break


        try:
            model = driver.find_element_by_xpath(
                "//div[@class='search_box search_box_tag search_box_light Label_Flight']/following-sibling::div[%d]/div[1]/div[1]/div[2]/span[1]" % (
                    i)).text
        except:
            break

        startTime = driver.find_element_by_xpath(
            "//div[@class='search_box search_box_tag search_box_light Label_Flight']/following-sibling::div[%d]/div[1]/div[2]/div[1]/strong[1]" % (i)).text
        startAirport = driver.find_element_by_xpath(
            "//div[@class='search_box search_box_tag search_box_light Label_Flight']/following-sibling::div[%d]/div[1]/div[2]/div[2]" % (i)).text
        arriveTime = driver.find_element_by_xpath(
            "//div[@class='search_box search_box_tag search_box_light Label_Flight']/following-sibling::div[%d]/div[1]/div[4]/div[1]/strong[1]" % (i)).text
        arriveAirport = driver.find_element_by_xpath(
            "//div[@class='search_box search_box_tag search_box_light Label_Flight']/following-sibling::div[%d]/div[1]/div[4]/div[2]" % (i)).text
        discount = driver.find_element_by_xpath(
            "//div[@class='search_box search_box_tag search_box_light Label_Flight']/following-sibling::div[%d]/div[1]/div[7]/div[1]/div[1]/div[1]/span[1]" % (i)).text

        print("航空公司：%s  航班号: %s  机票价格：%s  准点率%s 飞机型号：%s 出发时间：%s 出发机场：%s 到达时间：%s 到达机场：%s 折扣率：%s" % (company, number, price, punctualRate, model, startTime, startAirport, arriveTime, arriveAirport, discount))
        i = i + 1
        sql = "insert into ctrip(company, number, price, punctualrate, model, starttime, startairport, arrivetime, arriveairport, discount, startData)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql, (company, number, price, punctualRate, model, startTime, startAirport, arriveTime, arriveAirport, discount, data[j]))
        db.commit()
    driver.back()


def chooseCity(stime, atime, n):
    #清空输入框内容

    print("start: %d  arrive: %d"%(stime,atime))

    # print("出发地： %s 目的地： %s"%(city[stime],city[atime]))


    # 输入日期
    dataChose(stime, atime,n)
    #ac = driver.find_element_by_xpath("//ul[@class='search_baseform']/li[2]/input[1]").clear()
    # # 像出发城市框输入城市名
    # ac = driver.find_element_by_xpath("//ul[@class='search_baseform']/li[2]/input[1]").send_keys(u"%s" % (city[stime]))
    #
    # # 点击一下附近解决弹出对话框
    # ac = driver.find_element_by_xpath("//ul[@class='search_baseform']/li[2]/span[1]")
    # ActionChains(driver).move_to_element(ac).click(ac).perform()
    #
    # # 清空输入框内容
    # ac = driver.find_element_by_xpath("//ul[@class='search_baseform']/li[5]/input[1]").clear()
    #
    # # 向到达城市框输入城市名
    # ac = driver.find_element_by_xpath("//ul[@class='search_baseform']/li[5]/input[1]").send_keys(u"%s" % (city[atime]))
    #
    # # 点击一下附近解决弹出对话框
    # ac = driver.find_element_by_xpath("//ul[@class='search_baseform']/li[5]/span[1]")
    # ActionChains(driver).move_to_element(ac).click(ac).perform()
#如果浏览器后退不能保存上次输入的出发城市，目的地等数据，那dataChose函数就没有意义了，只能在函数里重新输入
def dataChose(stime, atime,n):
    j= 1
    while j < 7:
        # #原版输入内容
        # # 清空输入框内容
        # ac = driver.find_element_by_xpath("//ul[@class='search_baseform']/li[2]/input[1]").clear()
        #
        # # 像出发城市框输入城市名
        # ac = driver.find_element_by_xpath("//ul[@class='search_baseform']/li[2]/input[1]").send_keys(
        #     u"%s" % (city[stime]))
        #
        # # 点击一下附近解决弹出对话框
        # ac = driver.find_element_by_xpath("//ul[@class='search_baseform']/li[2]/span[1]")
        # ActionChains(driver).move_to_element(ac).click(ac).perform()
        #
        # # 清空输入框内容
        # ac = driver.find_element_by_xpath("//ul[@class='search_baseform']/li[5]/input[1]").clear()
        #
        # # 向到达城市框输入城市名
        # ac = driver.find_element_by_xpath("//ul[@class='search_baseform']/li[5]/input[1]").send_keys(
        #     u"%s" % (city[atime]))
        #
        # # 点击一下附近解决弹出对话框
        # ac = driver.find_element_by_xpath("//ul[@class='search_baseform']/li[5]/span[1]")
        # ActionChains(driver).move_to_element(ac).click(ac).perform()
        # time.sleep(1)
        #
        # #输入日期
        # ac = driver.find_element_by_xpath("//ul[@class='search_baseform']/li[6]/input[1]").clear()
        # ac = driver.find_element_by_xpath("//ul[@class='search_baseform']/li[6]/input[1]").send_keys(u"%s" % (data[i]))
        #
        # print("日期： %s"%(data[i]))
        #
        # # 点击一下附近解决弹出对话框
        # ac = driver.find_element_by_xpath("//ul[@class='search_baseform']/li[6]/span[1]")
        # ActionChains(driver).move_to_element(ac).click(ac).perform()

        #点击出发城市框
        ac = driver.find_element_by_xpath("//ul[@class='search_baseform']/li[2]/input[1]")
        ActionChains(driver).move_to_element(ac).click(ac).perform()

        ac = driver.find_element_by_xpath("//ul[@class='search_baseform']/li[2]/input[1]")
        ActionChains(driver).move_to_element(ac).click(ac).perform()

        #选择出发城市
        ac = driver.find_element_by_xpath("//div[@class='address_hotlist']/ul[1]/li[%d]"%(stime))
        ActionChains(driver).move_to_element(ac).click(ac).perform()

        # 点击到达城市框
        ac = driver.find_element_by_xpath("//ul[@class='search_baseform']/li[5]/input[1]")
        ActionChains(driver).move_to_element(ac).click(ac).perform()

        #选择到达城市
        ac = driver.find_element_by_xpath("//div[@class='address_hotlist']/ul[1]/li[%d]"%(atime))
        ActionChains(driver).move_to_element(ac).click(ac).perform()

        #输入日期
        ac = driver.find_element_by_xpath("//ul[@class='search_baseform']/li[6]/input[1]").clear()
        ac = driver.find_element_by_xpath("//ul[@class='search_baseform']/li[6]/input[1]").send_keys(u"%s" % (data[j]))

        print("日期： %s"%(data[j]))

        # 点击一下附近解决弹出对话框
        ac = driver.find_element_by_xpath("//ul[@class='search_baseform']/li[6]/span[1]")
        ActionChains(driver).move_to_element(ac).click(ac).perform()

        #向下滚动浏览器
        js = "var q=document.documentElement.scrollTop=50"
        driver.execute_script(js)

        # 点击搜索
        ac = driver.find_element_by_class_name("search")
        ActionChains(driver).move_to_element(ac).click(ac).perform()

        #爬取详细信息
        explicitInfo(n, j)
        j = j + 1
    driver.get("https://flights.ctrip.com/")
    # driver.get("https://flights.ctrip.com/itinerary/oneway/bjs-sha?date=2019-03-05")


def flyTime(stime, atime, n):
    i=1
    j=0
    while i <= stime :
        while j <= atime :
            j = j + 1
            if i > 19:
                if i == j:
                    continue
                else:
                    chooseCity(i, j, n)
        j = 0
        i = i + 1

#flyTime(2,3,4)
#20*20个城市
flyTime(20,19,30)


cursor.close()
db.close()
driver.close()
