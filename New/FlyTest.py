from selenium import webdriver
from selenium.webdriver import ActionChains
import time
import pytesseract
from PIL import Image
import pymysql
#这个网站driver.back以后不能保存上次输入的信息，所有信息需要重新输入


# 另一种二值化。自定义灰度，将灰度值在 190 以上的设置 1（白色），其它设为 0（黑色），相当于将阈值设置成了 115
threshold = 140

table = []

#灰度值一共256，190以下设置为0（黑色），以上为白色不显示
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)

# 我们常用的爬虫IP是高匿名动态IP，是通过拨号动态产生的，时效性很短，一般在1~3分钟。对于scrapy这种并发度很高，又不需要登录的爬虫来说，非常合适，但是在浏览器渲染类爬虫中并不适用。
# 使用代理IP会降低爬虫效率
driver = webdriver.Chrome()
# browser.implicitly_wait(10) # 等待时间为10seconds
# db = pymysql.connect(host="localhost", port=3306, user="root", passwd="123456", database="airport", charset="utf8")
# # 使用cursor()方法获取操作游标
# cursor = db.cursor()
# sql = "delete from fly"
# cursor.execute(sql)

driver.get("http://www.variflight.com/")
driver.maximize_window()


# print(browser.page_source)
# className不允许使用复合类名(类名中含有空格)做参数

# 选择出发城市和到达城市进行查询
# def choose_city(stime, atime, n):
#
#
#
#
#
#
#     # 进行查询，并查询完本天情况后，查询日后七天情况
#     clickdata(stime, atime,n)
#     driver.back()


# 点击查询结果中的第i个航班
def explicit_info(i):
    driver.implicitly_wait(5)
    # 从列表的第i行爬取各种信息/div[@class='li_com']/span[1]
    #从总体信息统计界面爬取这条的大略信息
    company = driver.find_element_by_xpath("//ul[@id='list']/li[%d]/div/span[1]/b[1]/a[1]" % (i)).text
    number = driver.find_element_by_xpath("//ul[@id='list']/li[%d]/div/span[1]/b[1]/a[2]" % (i)).text
    startTime = driver.find_element_by_xpath("//ul[@id='list']/li[%d]/div/span[2]" % (i)).text
    startAirport = driver.find_element_by_xpath("//ul[@id='list']/li[%d]/div/span[4]" % (i)).text
    arriveTime = driver.find_element_by_xpath("//ul[@id='list']/li[%d]/div/span[5]" % (i)).text
    arriveAirport = driver.find_element_by_xpath("//ul[@id='list']/li[%d]/div/span[7]" % (i)).text
    # punctualRate = driver.find_element_by_xpath("//ul[@id='list']/li[%d]/div/span[8]"%(i)).text
    state = driver.find_element_by_xpath("//ul[@id='list']/li[%d]/div/span[9]" % (i)).text
    print('''公司: %s 航班号：%s 出发时间：%s  出发机场：%s 到达时间：%s  到达机场：%s 飞机状态：%s'''
      % (company, number, startTime, startAirport, arriveTime, arriveAirport, state))

    # 点击这条航班信息进入具体页面
    driver.implicitly_wait(5)
    ac = driver.find_element_by_xpath("//ul[@id='list']/li[%d]" % (i))
    ActionChains(driver).move_to_element(ac).click(ac).perform()

    # 验证码识别
    verify()

    # 在具体页面爬取信息
    distance = driver.find_element_by_xpath("//div[@class='p_ti']/span[1]").text
    hour = driver.find_element_by_xpath("//div[@class='p_ti']/span[2]").text
    airport_model = driver.find_element_by_class_name("mileage").text
    age = driver.find_element_by_class_name("time").text
    departure_weather = driver.find_element_by_xpath("//ul[@class='f_common rand_ul_dep']/li[1]").text
    arrive_weather = driver.find_element_by_xpath("//ul[@class='f_common rand_ul_arr']/li[1]").text

    path = "//div[@class='p_info']/ul/li[3]/span"
    rate = knowPicture(path)

    print(distance, hour, airport_model, age)
    print("%s天气：%s \n%s天气：%s  准点率：%s" % (startAirport, departure_weather, arriveAirport, arrive_weather, rate))
    #现在数据库表格的参数和这个不一样，想用要修改
    # create table fly(company varchar(20), number varchar(20), startTime varchar(20), startAirport varchar(20), arriveTime varchar(20), arriveAirport varchar(20), data varchar(50), distance varchar(20), hour varchar(20), model varchar(20), age varchar(20), departure_weather varchar(40), arrive_weather varchar(40));
    # sql = "insert into fly(company, number, starttime, startairport, arrivetime, arriveairport, data, distance, hour, model, age, departure_weather, arrive_weather )values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    # cursor.execute(sql, (company, number, startTime, startAirport, arriveTime, arriveAirport, data, distance, hour, airport_model, age,
    # departure_weather, arrive_weather))
    # db.commit()
    #返回总体信息统计界面
    driver.back()
    # 验证码识别
    verify()


# 点击具体日期,查询未来7天的
def clickdata(stime, atime,n):
    print("start: %d  arrive: %d" % (stime, atime))

    j = 0
    while j <= 6:
        time.sleep(1)
        # 点击按起降地框
        ac = driver.find_element_by_id("myOrder")
        ActionChains(driver).move_to_element(ac).click(ac).perform()

        # 点击出发城市框
        ac = driver.find_element_by_id("dep_city")
        ActionChains(driver).move_to_element(ac).click(ac).perform()

        # 点击第i个热门出发城市
        ac = driver.find_element_by_xpath("//div[@class='cityByHot clearfix']/span[%d]" % (stime))
        ActionChains(driver).move_to_element(ac).click(ac).perform()

        # 点击到达城市框
        ac = driver.find_element_by_id("arr_city")
        ActionChains(driver).move_to_element(ac).click(ac).perform()

        # 点击第i个热门出发城市
        ac = driver.find_element_by_xpath("//div[@class='cityByHot clearfix']/span[%d]" % (atime))
        ActionChains(driver).move_to_element(ac).click(ac).perform()

        i = 1
        # 点击日期框
        ac = driver.find_element_by_id("cityDatepicker")
        ActionChains(driver).move_to_element(ac).click(ac).perform()

        # 查询今天之后的七天飞机情况,因为picked的位置会随着点击变化，所有不用设置为变量，只需每次加一就可以进入下一天
        #点击下一天的日期
        ac = driver.find_element_by_xpath("//li[@class='picked']/following-sibling::li[%s]"%(j+1))
        ActionChains(driver).move_to_element(ac).click(ac).perform()

        # 点击查询按钮，进入总体统计界面
        ac = driver.find_element_by_id("byCityBtn")
        ActionChains(driver).move_to_element(ac).click(ac).perform()

        # 验证码识别
        verify()

        # 已经进入总体航班信息统计
        global data
        data = driver.find_element_by_class_name('tit').text
        print("航班信息：", data)

        while i <= n:
            #查询当前日期的第i条信息的具体信息
            explicit_info(i)
            i = i + 1
        j = j + 1
        #从总体统计信息界面返回填写日期的界面
        driver.back()
    driver.get("http://www.variflight.com/")


# choose_city(1,2,1)
# explicit_info(1)
def flyTime(stime, atime, n):
    i = 1
    j = 0
    while i <= stime:
        while j <= atime:
            j = j + 1
            if i == j or (i == 3 and j == 4):
                continue
            else:
                clickdata(i, j, n)
        j = 0
        i = i + 1

#切割图片并识别
def knowPicture(xpath):
    pic = driver.find_element_by_xpath("%s"%(xpath))
    temp_img1 = 'F:\picture\w1.png'  # 图片存放位置，getImg.png是给截图的命名
    temp_img2 = 'F:\picture\w2.png'  # 图片存放位置，getImg.png是给截图的命名
    driver.save_screenshot(temp_img1)
    left = pic.location['x']
    top = pic.location['y']
    elementWidth = pic.location['x'] + pic.size['width']
    elementHeight = pic.location['y'] + pic.size['height']
    picture = Image.open(temp_img1)
    # 截图所使用的坐标却是需要根据电脑显示比例决定的
    # 图片的缩放比例和电脑不一样（现在电脑是125%），将比例调整成一样就可以了
    picture = picture.crop((1.25 * (left), 1.25 * (top), 1.25 * (elementWidth), 1.25 * (elementHeight)))
    # picture = picture.crop((1.25*(left), top, elementWidth, elementHeight))
    #存储切割出的验证码
    picture.save(temp_img2)
    #直接打开图片，不处理直接识别
    image = Image.open(temp_img2)
    # image.show() #打开图片1.jpg
    text = pytesseract.image_to_string(image,lang='chi_sim') #使用简体中文解析图片
    return text

#验证码识别
def verify():
    while 1==1:
        try:
            #点击一下更换验证码
            ac = driver.find_element_by_id("authCodeImg")
            ActionChains(driver).move_to_element(ac).click(ac).perform()

            #验证码的xpath
            path = "//div[@class='authCodeBox']/div[2]/div/img"
            #调用函数对验证码部分截图
            knowPicture(path)
            #将识别的验证码中的值赋给verification
            verification = getverify1('F:\picture\w2.png')
            print(verification)
            #将识别出的验证码写入框内
            driver.execute_script('document.getElementById("authCodeImgInput").value="%s"' % (verification))
            # driver.execute_script('document.getElementById("authCodeImgInput").value="123"')
            #点击提交验证码
            ac = driver.find_element_by_xpath("//div[@class='authCodeBox']/div[2]/div[2]/input")
            ActionChains(driver).move_to_element(ac).click(ac).perform()

            #等待1秒如果识别不成功，使验证码错误的提示消失
            time.sleep(3)
        except:
            break

def getverify1(name):
    # 打开切割出的验证码图片
    im = Image.open(name)
    # 转化到灰度图
    imgry = im.convert('L')
    # 保存图像
    imgry.save('F:\picture\w4.png')
    # 二值化，采用阈值分割法，threshold为分割点
    # 二值化，传入的是数字 1，默认阈值是 127，一般不推荐使用，改用table
    out = imgry.point(table, '1')
    out.save('F:\picture\w5.png')

    # 识别
    text = pytesseract.image_to_string('F:\picture\w5.png')  # 使用简体中文解析图片
    text = text.strip() #         返回一个去除开始空格和结尾空格的字符串副本。
    # 使用ImageEnhance可以增强图片的识别率
    # enhancer = ImageEnhance.Contrast(image)
    # enhancer = enhancer.enhance(4)

    # 去掉非法字符，只保留字母数字
    # ltext = re.sub("\W", "", ltext)
    # text = text.upper() #         返回一个被转换为全大写字母的字符串的副本。
    print("123 %s" % (text))
    return text

flyTime(18, 18, 30)

# 打印页面标题
# print (browser.title)
# 退出，清除浏览器缓存
# cursor.close()
# db.close()
driver.quit()

