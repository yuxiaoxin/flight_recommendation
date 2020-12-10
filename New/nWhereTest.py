from selenium import webdriver
from selenium.webdriver import ActionChains
import time
import pymysql
#python里面不是没有局部变量而是if，while里定义的不是局部变量，函数里定义的还是局部变量
db = pymysql.connect(host = "localhost",port = 3306, user = "root", passwd = "123456",database = "airport", charset="utf8")
# 使用cursor()方法获取操作游标
cursor = db.cursor()
# sql = "delete from wheretest"
# cursor.execute(sql)

driver = webdriver.Chrome()
#browser.implicitly_wait(10) # 等待时间为10seconds

# 追加数据到hdfs文件
def append_to_hdfs(client, hdfs_path, data):
    client.write(hdfs_path, data, overwrite=False, append=True)

#driver.get("https://www.qunar.com/?ex_track=auto_4e0d874a")
driver.get("https://flight.qunar.com/")

driver.maximize_window()
city = ['','北京','广州','上海','成都','深圳','杭州','武汉','西安','重庆','青岛','长沙','南京','厦门','昆明','大连','天津','郑州','三亚','济南','福州','哈尔滨','长春','海口','贵阳','兰州','南宁']
#data = ['','2019-03-10','2019-03-11','2019-03-12','2019-03-13','2019-03-14']

def explicitInfo(n):
    i = 1
    time.sleep(3)
    while i <= n:
        #防止这个字段没有导致程序崩溃,第一个用break是为了防止没有那么多航班
        try:
            company = driver.find_element_by_xpath(
                "//div[@class='m-airfly-lst']/div[%d]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]" % (i)).text
        except:
            break

        try:
            model = driver.find_element_by_xpath("//div[@class='m-airfly-lst']/div[%d]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/span[2]"%(i)).text
        except:
            continue

        try:
            discount = driver.find_element_by_xpath(
                "//div[@class='m-airfly-lst']/div[%d]/div[1]/div[2]/div[1]/span[1]" % (i)).text
        except:
            continue

        number = driver.find_element_by_xpath("//div[@class='m-airfly-lst']/div[%d]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/span[1]"%(i)).text
        startTime = driver.find_element_by_xpath("//div[@class='m-airfly-lst']/div[%d]/div[1]/div[1]/div[1]/div[2]/div[1]/h2[1]"%(i)).text
        startAirport = driver.find_element_by_xpath("//div[@class='m-airfly-lst']/div[%d]/div[1]/div[1]/div[1]/div[2]/div[1]/p[1]/span[1]"%(i)).text
        allTime = driver.find_element_by_xpath("//div[@class='m-airfly-lst']/div[%d]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]"%(i)).text
        arriveTime = driver.find_element_by_xpath("//div[@class='m-airfly-lst']/div[%d]/div[1]/div[1]/div[1]/div[2]/div[3]/h2[1]"%(i)).text
        arriveAirport = driver.find_element_by_xpath("//div[@class='m-airfly-lst']/div[%d]/div[1]/div[1]/div[1]/div[2]/div[3]/p[1]/span[1]"%(i)).text
        print("航空公司：%s 航班号：%s  飞机型号：%s 出发时间：%s 出发机场：%s 到达时间：%s 到达机场：%s 飞行时长：%s 折扣率：%s" % (company, number, model, startTime, startAirport, arriveTime, arriveAirport, allTime, discount))

        #判断并计算正确价格
        price = 0
        #falPrice是存储假价格的i标签下的数字
        falPrice = driver.find_elements_by_xpath(
            "//div[@class='m-airfly-lst']/div[%d]/div[1]/div[2]/p[1]/span[1]/span[1]/span[1]/em[1]/b[1]/i"%(i))
        #realPrice是存储真正的价格的b标签，其中realPrice[0]存储的b[1]是存储价格i标签用的，计算真正价格时不使用
        realPrice = driver.find_elements_by_xpath(
            "//div[@class='m-airfly-lst']/div[%d]/div[1]/div[2]/p[1]/span[1]/span[1]/span[1]/em[1]/b"%(i))
        i = i + 1

        if len(falPrice) == 3:
            price2 = int(falPrice[0].text) * 100
            # print(falPrice[0].text)
            price3 = int(falPrice[1].text) * 10
            # print(falPrice[1].text)
            price4 = int(falPrice[2].text)
            # print(falPrice[2].text)
            # realPrice[1]对应b[2]
            #realPrice[1]是除了假价格的第一个b标签（b[2]）
            if realPrice[1].get_attribute('style') == "width: 16px; left: -48px;":
                # print(realPrice[1].text)
                price2 = int(realPrice[1].text) * 100
            elif realPrice[1].get_attribute('style') == "width: 16px; left: -32px;":
                # print(realPrice[1].text)
                price3 = int(realPrice[1].text) * 10
            elif realPrice[1].get_attribute('style') == "width: 16px; left: -16px;":
                # print(realPrice[1].text)
                price4 = int(realPrice[1].text)
            # print(str(realPrice[1].get_attribute('style')) == "width: 16px; left: -48px;")
            # print(str(realPrice[1].get_attribute('style')) == "width: 16px; left: -32px;")
            # print(str(realPrice[1].get_attribute('style')) == "width: 16px; left: -16px;")

            try:
                if realPrice[2].get_attribute('style') == 'width: 16px; left: -48px;':
                    price2 = int(realPrice[2].text) * 100
                elif realPrice[2].get_attribute('style') == 'width: 16px; left: -32px;':
                    price3 = int(realPrice[2].text) * 10
                elif realPrice[2].get_attribute('style') == 'width: 16px; left: -16px;':
                    price4 = int(realPrice[2].text)
            except:
                pass

            try:
                if realPrice[3].get_attribute('style') == 'width: 16px; left: -48px;':
                    price2 = int(realPrice[3].text) * 100
                elif realPrice[3].get_attribute('style') == 'width: 16px; left: -32px;':
                    price3 = int(realPrice[3].text) * 10
                elif realPrice[3].get_attribute('style') == 'width: 16px; left: -16px;':
                    price4 = int(realPrice[3].text)
            except:
                pass
            price = price2 + price3 + price4
            print(price)

        elif len(falPrice) == 4:
            price1 = int(falPrice[0].text) * 1000
            # print(falPrice[0].text)
            price2 = int(falPrice[1].text) * 100
            # print(falPrice[1].text)
            price3 = int(falPrice[2].text) * 10
            # print(falPrice[2].text)
            price4 = int(falPrice[3].text)

            # realPrice[1]对应b[2]
            if realPrice[1].get_attribute('style') == "width: 16px; left: -48px;":
                # print(realPrice[1].text)
                price2 = int(realPrice[1].text) * 100
            elif realPrice[1].get_attribute('style') == "width: 16px; left: -32px;":
                # print(realPrice[1].text)
                price3 = int(realPrice[1].text) * 10
            elif realPrice[1].get_attribute('style') == "width: 16px; left: -16px;":
                # print(realPrice[1].text)
                price4 = int(realPrice[1].text)
            elif realPrice[1].get_attribute('style') == "width: 16px; left: -64px;":
                price1 = int(realPrice[1].text) * 1000
            # print(str(realPrice[1].get_attribute('style')) == "width: 16px; left: -48px;")
            # print(str(realPrice[1].get_attribute('style')) == "width: 16px; left: -32px;")
            # print(str(realPrice[1].get_attribute('style')) == "width: 16px; left: -16px;")

            try:
                if realPrice[2].get_attribute('style') == 'width: 16px; left: -48px;':
                    price2 = int(realPrice[2].text) * 100
                elif realPrice[2].get_attribute('style') == 'width: 16px; left: -32px;':
                    price3 = int(realPrice[2].text) * 10
                elif realPrice[2].get_attribute('style') == 'width: 16px; left: -16px;':
                    price4 = int(realPrice[2].text)
                elif realPrice[2].get_attribute('style') == "width: 16px; left: -64px;":
                    price1 = int(realPrice[2].text) * 1000
            except:
                pass

            try:
                if realPrice[3].get_attribute('style') == 'width: 16px; left: -48px;':
                    price2 = int(realPrice[3].text) * 100
                elif realPrice[3].get_attribute('style') == 'width: 16px; left: -32px;':
                    price3 = int(realPrice[3].text) * 10
                elif realPrice[3].get_attribute('style') == 'width: 16px; left: -16px;':
                    price4 = int(realPrice[3].text)
                elif realPrice[3].get_attribute('style') == "width: 16px; left: -64px;":
                    price1 = int(realPrice[3].text) * 1000
            except:
                pass
            try:
                if realPrice[4].get_attribute('style') == 'width: 16px; left: -48px;':
                    price2 = int(realPrice[4].text) * 100
                elif realPrice[4].get_attribute('style') == 'width: 16px; left: -32px;':
                    price3 = int(realPrice[4].text) * 10
                elif realPrice[4].get_attribute('style') == 'width: 16px; left: -16px;':
                    price4 = int(realPrice[4].text)
                elif realPrice[4].get_attribute('style') == "width: 16px; left: -64px;":
                    price1 = int(realPrice[4].text) * 1000
            except:
                pass
            price = price1 + price2 + price3 + price4
            print("票价： %d"%(price))

        priceWeight = 0
        timeWeight = 0
        departureTimeWeight = 0
        if price<=800 :
            priceWeight = 5
        elif 800<price&price<1000:
            priceWeight =4
        elif 1000<price&price<1500:
            priceWeight =3
        elif 1500<price&price<2000:
            priceWeight =2
        elif 2000<price&price:
            priceWeight =1

        if startTime[:1] == '0':
            sTime = int(startTime[1:2])
        else:
            sTime = int(startTime[0:2])

        if arriveTime[:1] == '0':
            aTime = int(startTime[1:2])
        else:
            aTime = int(startTime[0:2])


        if aTime > sTime:
            travelTime = aTime - sTime
        else:
            travelTime = aTime - sTime + 24

        if travelTime<=4 :
            timeWeight  = 4
        elif 4<price&price<=5:
            timeWeight  =3
        elif 5<price&price<=6:
            timeWeight  =2
        elif 6<price:
            timeWeight  =1

        if 0<aTime<=5 :
            departureTimeWeight   = 1
        elif 5<aTime&aTime<=8:
            departureTimeWeight   =2
        elif 8<aTime&aTime<=16:
            departureTimeWeight   =3
        elif 16<aTime&aTime<=20:
            departureTimeWeight   =2
        elif 20<aTime&aTime<=23:
            departureTimeWeight   =1

        companyWeight = 1
        typeWeight  = 1
        punctualWeight   = 1
        ageWeight  = 1


        sql = "insert into wheretest(company, number, price, puncualRate, model, startTime, startAirport , arriveTime , arriveAirport, discount, data, startPlace, startProvince, arriveProvince, arrivePlace, priceWeight, timeWeight ,  departureTimeWeight , companyWeight ,  typeWeight , ageWeight ,  punctualWeight )values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql,(company, number, price, discount, model, startTime, startAirport, arriveTime, arriveAirport, data, startPlace, arrivePlace, priceWeight, timeWeight ,  departureTimeWeight , companyWeight ,  typeWeight , ageWeight ,  punctualWeight))
        db.commit()
def chooseCity(stime, atime, n):
    #绝对不能用id作为标签寻找路径，很多网站id都会变动，但是class不会
    print("start: %d  arrive: %d"%(stime,atime))

    time.sleep(1)
    # 清空出发城市输入框内容
    ac = driver.find_element_by_xpath("//div[@class='crl_sp_city']/div[1]/div[1]/input[1]").clear()

    # 像出发城市框输入城市名
    ac = driver.find_element_by_xpath("//div[@class='crl_sp_city']/div[1]/div[1]/input[1]").send_keys(u"%s" % (city[stime]))
    global startPlace
    startPlace = city[stime]

    # 点击一下单程按钮
    ac = driver.find_element_by_xpath("//div[@class='crl_sp_sel']/label[1]/input[1]")
    ActionChains(driver).move_to_element(ac).click(ac).perform()

    # 清空输入框内容
    ac = driver.find_element_by_xpath("//div[@class='crl_sp_city']/div[2]/div[1]/input[1]").clear()

    # 向到达城市框输入城市名
    ac = driver.find_element_by_xpath("//div[@class='crl_sp_city']/div[2]/div[1]/input[1]").send_keys(u"%s" % (city[atime]))
    time.sleep(1)

    global arrivePlace
    arrivePlace = city[atime]

    # 点击一下单程按钮
    ac = driver.find_element_by_xpath("//div[@class='crl_sp_sel']/label[1]/input[1]")
    ActionChains(driver).move_to_element(ac).click(ac).perform()

    # print("出发地： %s 目的地： %s"%(city[stime],city[atime]))

    # 输入日期
    dataChose(stime, atime, n)
    time.sleep(1)

def dataChose(stime, atime, n):
    j= 2
    while j < 8:
        #去哪网浏览器后退时可以保存上次的输入，所有这里可以不用注释里的内容来重新输入出发地，目的地
        time.sleep(1)
        # ac = driver.find_element_by_xpath("//div[@class='crl_sp_city']/div[1]/div[1]/input[1]").clear()
        #
        # # 像出发城市框输入城市名
        # ac = driver.find_element_by_xpath("//div[@class='crl_sp_city']/div[1]/div[1]/input[1]").send_keys(
        #     u"%s" % (city[stime]))
        #
        # # 点击一下单程按钮
        # ac = driver.find_element_by_xpath("//div[@class='crl_sp_sel']/label[1]/input[1]")
        # ActionChains(driver).move_to_element(ac).click(ac).perform()
        #
        # # 清空输入框内容
        # ac = driver.find_element_by_xpath("//div[@class='crl_sp_city']/div[2]/div[1]/input[1]").clear()
        #
        # # 向到达城市框输入城市名
        # ac = driver.find_element_by_xpath("//div[@class='crl_sp_city']/div[2]/div[1]/input[1]").send_keys(
        #     u"%s" % (city[atime]))
        # time.sleep(1)
        #
        # # 点击一下单程按钮
        # ac = driver.find_element_by_xpath("//div[@class='crl_sp_sel']/label[1]/input[1]")
        # ActionChains(driver).move_to_element(ac).click(ac).perform()

        ac = driver.find_element_by_xpath("//div[@class='crl_sp_sel']/label[2]/input[1]")
        # 点击往返按钮
        ActionChains(driver).move_to_element(ac).click(ac).perform()

        #点击返程日期输入框
        try:
            ac = driver.find_element_by_xpath("//div[@class='crl_sp_date']/div[3]/div[1]/input")
            ActionChains(driver).move_to_element(ac).click(ac).perform()
        except:
            break

        # #点击出发日期输入框
        # ac = driver.find_element_by_xpath("//div[@class='crl_sp_date']/div[1]/div[1]/input")
        # ActionChains(driver).move_to_element(ac).click(ac).perform()

        time.sleep(1)
        #选择日期
        try:
            ac = driver.find_element_by_xpath("//div[@class='c-wp']/div[1]/div[3]/table[1]/tbody[1]/tr[4]/td[%d]" % (j))
            ActionChains(driver).move_to_element(ac).click(ac).perform()
        except:
            break


        global data
        data = driver.find_element_by_xpath("//div[@class='crl_sp_date']/div[3]/div[1]/input").get_attribute('value')
        print("日期： %s"%(data))

        # 点击往返按钮
        # ac = driver.find_element_by_xpath("//div[@class='crl_sp_sel']/label[2]/input[1]")
        # ActionChains(driver).move_to_element(ac).click(ac).perform()

        # 点击单程按钮
        # ac = driver.find_element_by_xpath("//div[@class='crl_sp_sel']/label[1]/input[1]")
        # ActionChains(driver).move_to_element(ac).click(ac).perform()

        # 点击搜索
        ac = driver.find_element_by_class_name("btn_search")
        ActionChains(driver).move_to_element(ac).click(ac).perform()

        #爬取详细信息
        explicitInfo(n)
        j = j + 1
        driver.back()
    driver.get("https://flight.qunar.com/")


def flyTime(stime, atime, n):
    p=1
    q=0
    while p <= stime :
        while q <= atime :
            q = q + 1
            if p>21:
                if p == q:
                    continue
                else:
                    chooseCity(p, q, n)
        q = 0
        p = p + 1

flyTime(25,25,40)
db.close()
cursor.close()
driver.close()
