from django.shortcuts import render,redirect
from django.http import HttpResponse
import pymysql
import random
from pyecharts import Line,Bar,Map,GeoLines, Style, Radar, Liquid, Pie, Overlap



db = pymysql.connect(host = 'localhost' ,port = 3306, user = 'root', passwd = '123456',database = 'airport', charset='utf8')
cursor = db.cursor()
# from pyecharts.constants import DEFAULT_HOST #这句去掉
DEFAULT_HOST = "" #加上这句

# 记录用户最看重因素的一半
userHighWeight = ''
fromCity = ''
toCity = ''
# 用户最看重因素的位置
userHighPosition = ''
airportName = ''
airportPlace = ''
priceWeight = 0
timeWeight = 0
punctualWeight = 0
departureTimeWeight = 0
companyWeight = 0
typeWeight: int = 0
ageWeight = 0


def wrong(request):
    return render(request,'404.html')

def wrong2(request):
    return render(request,'quireFault.html')

def flightPie(request):
    l = p()  # 生成图像实例
    context = {}
    context['myechart'] = l.render_embed()
    return render(request, 'flightPie.html', context)


def airportRecommend(request):
    l = pan()  # 生成图像实例
    context = {}
    context['echart'] = l.render_embed()
    return render(request, 'airportRecommend.html', context)
def airportDiscount(request):
    l = bDiscount()  # 生成图像实例
    context = {}
    context['echart'] = l.render_embed()
    return render(request, 'airportDiscount.html', context)
def airportPunctual(request):
    l = water()  # 生成图像实例
    context = {}
    context['echart'] = l.render_embed()
    return render(request, 'airportPunctual.html', context)

def pan():
    bar = Bar("区间分布")
    priceNum = []
    for i in range(7):
        priceNum.append(0)
    priceThis = []
    for i in range(7):
        priceThis.append(0)
    priceThis[3] = 3
    priceThis[4] = 6
    priceThis[5] = 8
    priceThis[6] = 1

    db = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', database='airport', charset='utf8')
    cursor = db.cursor()
    sql = "select * from ctrip"
    cursor.execute(sql)
    results = cursor.fetchall()
    i = 0
    fromCity = '北京'
    toCity = '上海'

    for row in results:
        price = int(row[2][1:])
        print(price)
        if fromCity == row[12] and toCity == row[14]:
            price = int(row[2][1:])
            print(price)
            if price < 800:
                priceThis[0] = priceThis[0] + 1
            elif 800 < price < 1000:
                priceThis[1] = priceThis[1] + 1
            elif 1000 < price < 1500:
                priceThis[2] = priceThis[2] + 1
            elif 1500 < price < 2000:
                priceThis[3] = priceThis[3] + 1
            elif 2000 < price < 2500:
                priceThis[4] = priceThis[4] + 1
            elif 2500 < price < 3000:
                priceThis[5] = priceThis[5] + 1
            elif 3000 < price:
                priceThis[6] = priceThis[6] + 1

    # //设置column的最大值，为了雷达图更为直观，这里的月份最大值设置有所不同

    y = ["0~800", "800~1000", "1000~1500", "1500~2000", "2000~2500", "2500~3000", "3000~"]
    line = Line()
    line.add('航班范围', y, priceThis, mark_point=[{"coord": ["0~800", priceThis[0]]}], mark_point_symbol='diamond',
             mark_point_textcolor='#40ff27')
    bar.add("票价", y, priceThis)
    overlap = Overlap()
    overlap.add(bar)
    overlap.add(line)
    overlap.show_config()

    return overlap


def bDiscount():
    # python中的数组长度是动态的,不用声明

    priceNum = []
    y = []

    sql = "select * from ctrip"
    cursor.execute(sql)
    results = cursor.fetchall()
    i = 0
    fromCity = '北京'
    toCity = '上海'

    for row in results:
        price = int(row[2][1:])
        print(price)

        if fromCity == row[12] and toCity == row[14]:
            price = int(row[2][1:])
            priceNum.append(price)
            y.append(i)
            i = i + 1

    # 折线图
    line = Line()
    line.add("成交量", y, priceNum, mark_point=[{"coord": [45, priceNum[45]]}], mark_point_symbol='diamond',
             mark_point_textcolor='#40ff27')

    return line


def p():
    # python中的数组长度是动态的,不用声明
    provice_flight = []
    for i in range(15):
        provice_flight.append(0)

    city = ['北京', '上海', '广东', '天津', '云南', '四川', '浙江', '湖北', '陕西', '重庆', '山东', '湖南', '福建', '辽宁', '河南']
    sql = "select * from ctrip"
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        if row[13] == '北京':
            provice_flight[0] = provice_flight[0] + 1
        elif row[13] == '上海':
            provice_flight[1] = provice_flight[1] + 1
        elif row[13] == '广东':
            provice_flight[2] = provice_flight[2] + 1
        elif row[13] == '天津':
            provice_flight[3] = provice_flight[3] + 1
        elif row[13] == '云南':
            provice_flight[4] = provice_flight[4] + 1
        elif row[13] == '四川':
            provice_flight[5] = provice_flight[5] + 1
        elif row[13] == '浙江':
            provice_flight[6] = provice_flight[6] + 1
        elif row[13] == '湖北':
            provice_flight[7] = provice_flight[7] + 1
        elif row[13] == '陕西':
            provice_flight[8] = provice_flight[8] + 1
        elif row[13] == '重庆':
            provice_flight[9] = provice_flight[9] + 1
        elif row[13] == '山东':
            provice_flight[10] = provice_flight[10] + 1
        elif row[13] == '湖南':
            provice_flight[11] = provice_flight[11] + 1
        elif row[13] == '福建':
            provice_flight[12] = provice_flight[12] + 1
        elif row[13] == '辽宁':
            provice_flight[13] = provice_flight[13] + 1
        elif row[13] == '河南':
            provice_flight[14] = provice_flight[14] + 1

    # //设置行名
    city = ['北京', '上海', '广东', '天津', '云南', '四川', '浙江', '湖北', '陕西', '重庆', '山东', '湖南', '福建', '辽宁', '河南']

    columns = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    # //设置主标题与副标题，标题设置居中，设置宽度为900
    pie = Pie("饼状图", "各省机场数量", title_pos='center', width=900)
    # //加入数据，设置坐标位置为【25，50】，上方的colums选项取消显示
    pie.add("机场数", city, provice_flight, center=[25, 50], is_legend_show=False, is_label_show=True)
    return pie


def priceShow(request):
    l = priceRadar()  # 生成图像实例
    context = {}
    context['echart'] = l.render_embed()
    return render(request, 'priceShow.html', context)

def discount(request):
    l = water()  # 生成图像实例
    context = {}
    context['echart'] = l.render_embed()
    return render(request, 'discount.html', context)

def water():
    rate = 0.6
    # 圆形水球
    liquid2 = Liquid("准点率")
    liquid2.add("Liquid", [rate, 0.5, 0.4, 0.3], is_liquid_outline_show=False)
    # liquid2.add("Liquid", [0.6, 0.5, 0.4, 0.3], is_liquid_outline_show=False)
    liquid2.show_config()
    return  liquid2


def priceRadar():
    priceNum = []
    for i in range(7):
        priceNum.append(0)
    priceThis = []
    for i in range(7):
        priceThis.append(0)
    priceThis[3] = 3
    priceThis[4] = 6
    priceThis[5] = 8
    priceThis[6] = 1


    sql = "select * from ctrip"
    cursor.execute(sql)
    results = cursor.fetchall()
    i = 0
    fromCity = '北京'
    toCity = '上海'

    for row in results:
        price = int(row[2][1:])
        print(price)
        if price < 800:
            priceNum[0] = priceNum[0] + 1
        elif 800 < price < 1000:
            priceNum[1] = priceNum[1] + 1
        elif 1000 < price < 1500:
            priceNum[2] = priceNum[2] + 1
        elif 1500 < price < 2000:
            priceNum[3] = priceNum[3] + 1
        elif 2000 < price < 2500:
            priceNum[4] = priceNum[4] + 1
        elif 2500 < price < 3000:
            priceNum[5] = priceNum[5] + 1
        elif 3000 < price:
            priceNum[6] = priceNum[6] + 1

        if fromCity == row[12] and toCity == row[14]:
            price = int(row[2][1:])
            print(price)
            if price < 800:
                priceThis[0] = priceThis[0] + 1
            elif 800 < price < 1000:
                priceThis[1] = priceThis[1] + 1
            elif 1000 < price < 1500:
                priceThis[2] = priceThis[2] + 1
            elif 1500 < price < 2000:
                priceThis[3] = priceThis[3] + 1
            elif 2000 < price < 2500:
                priceThis[4] = priceThis[4] + 1
            elif 2500 < price < 3000:
                priceThis[5] = priceThis[5] + 1
            elif 3000 < price:
                priceThis[6] = priceThis[6] + 1

    print(priceThis)
    print(priceNum)

    radar = Radar("价格图", "各区间机票数量")
    # //由于雷达图传入的数据得为多维数据，所以这里需要做一下处理
    radar_data1 = [priceThis]
    radar_data2 = [priceNum]
    # //设置column的最大值，为了雷达图更为直观，这里的月份最大值设置有所不同
    schema = [
        ("0~800", 8000), ("800~1000", 3000), ("1000~1500", 3000),
        ("1500~2000", 500), ("2000~2500", 200), ("2500~3000", 50),
        ("3000~", 50)
    ]
    # //传入坐标
    radar.config(schema)
    radar.add("本趟航班", radar_data1)
    # //一般默认为同一种颜色，这里为了便于区分，需要设置item的颜色
    radar.add("所有航班", radar_data2, item_color="#1C86EE")
    return radar


def airportAccount(request):
    m = map()  # 生成图像实例
    context = {}
    context['echart'] = m.render_embed()
    return render(request, 'airportAccount.html', context)


def airportNumber(request):
    l = numberLine()  # 生成图像实例
    context = {}
    context['echart'] = l.render_embed()
    return render(request, 'airportNumber.html', context)


def geoLine(request):
    l = geo()  # 生成图像实例
    context = {}
    context['echart'] = l.render_embed()
    return render(request, 'geoLine.html', context)





def map():
    provice_flight = []
    for i in range(15):
        provice_flight.append(0)

    city = ['北京', '上海', '广东', '天津', '云南', '四川', '浙江', '湖北', '陕西', '重庆', '山东', '湖南', '福建', '辽宁', '河南']
    sql = "select * from ctrip"
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        if row[13] == '北京':
            provice_flight[0] = provice_flight[0] + 1
        elif row[13] == '上海':
            provice_flight[1] = provice_flight[1] + 1
        elif row[13] == '广东':
            provice_flight[2] = provice_flight[2] + 1
        elif row[13] == '天津':
            provice_flight[3] = provice_flight[3] + 1
        elif row[13] == '云南':
            provice_flight[4] = provice_flight[4] + 1
        elif row[13] == '四川':
            provice_flight[5] = provice_flight[5] + 1
        elif row[13] == '浙江':
            provice_flight[6] = provice_flight[6] + 1
        elif row[13] == '湖北':
            provice_flight[7] = provice_flight[7] + 1
        elif row[13] == '陕西':
            provice_flight[8] = provice_flight[8] + 1
        elif row[13] == '重庆':
            provice_flight[9] = provice_flight[9] + 1
        elif row[13] == '山东':
            provice_flight[10] = provice_flight[10] + 1
        elif row[13] == '湖南':
            provice_flight[11] = provice_flight[11] + 1
        elif row[13] == '福建':
            provice_flight[12] = provice_flight[12] + 1
        elif row[13] == '辽宁':
            provice_flight[13] = provice_flight[13] + 1
        elif row[13] == '河南':
            provice_flight[14] = provice_flight[14] + 1

    # 省和直辖市
    province_distribution = {'深圳': provice_flight[3], '河南': provice_flight[1], '北京': provice_flight[0], '河北': 21,
                             '辽宁': 12, '江西': 6, '上海': provice_flight[1], '安徽': 10, '江苏': provice_flight[5], '湖南': 9,
                             '浙江': 13, '海南': 2, '广东': provice_flight[2], '湖北': provice_flight[6], '黑龙江': 11, '澳门': 1,
                             '陕西': provice_flight[7], '四川': provice_flight[4], '内蒙古': 3, '重庆': 3, '云南': 6, '贵州': 2,
                             '吉林': 3, '山西': 12, '山东': provice_flight[9], '福建': 4, '青海': 1, '舵主科技，质量保证': 1,
                             '天津': provice_flight[10], '其他': 1}
    provice = list(province_distribution.keys())
    values = list(province_distribution.values())

    map = Map("中国地图", '中国地图', width=800, height=350)
    map.add("", provice, values, visual_range=[0, 50], maptype='china', is_visualmap=True,
            visual_text_color='#000')
    map.show_config()
    return map


def geo():
    style = Style(
        title_top="#fff",
        title_pos="left",
        width=600,
        height=400,
        background_color="#404a59"

    )
    fromCity = '北京'
    toCity = '上海'
    data = [[fromCity, toCity]]

    style_geo = style.add(
        is_label_show=True,  # 标签的有无
        line_curve=0.2,  # 曲线的弯曲度
        line_opacity=0.5,  # 航线的透明度
        legend_text_color="#eee",
        legend_pos="right",  # 示例的位置
        geo_effect_symbol="plane",
        geo_effect_symbolsize=10,  # 飞机大小
        label_color=['#ffa022', '#ffa022', '#46bee9'],
        label_pos="right",
        label_formatter="{b}",  # 地方标签的格式
        label_text_color="#eee",
    )

    geolines = GeoLines("航线展示", **style.init_style)  # 相当于设置背景
    geolines.add("航线展示", data,
                 tooltip_formatter="{a} : {c}", **style_geo  # 设置航线的一些东西

                 )
    return geolines


def numberLine():
    # python中的数组长度是动态的,不用声明
    provice_flight = []
    for i in range(15):
        provice_flight.append(0)

    city = ['北京', '上海', '广东', '天津', '云南', '四川', '浙江', '湖北', '陕西', '重庆', '山东', '湖南', '福建', '辽宁', '河南']
    # 机场信息放在airport这个数据库里
    db = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', database='airport', charset='utf8')
    cursor = db.cursor()
    sql = "select * from ctrip"
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        if row[13] == '北京':
            provice_flight[0] = provice_flight[0] + 1
        elif row[13] == '上海':
            provice_flight[1] = provice_flight[1] + 1
        elif row[13] == '广东':
            provice_flight[2] = provice_flight[2] + 1
        elif row[13] == '天津':
            provice_flight[3] = provice_flight[3] + 1
        elif row[13] == '云南':
            provice_flight[4] = provice_flight[4] + 1
        elif row[13] == '四川':
            provice_flight[5] = provice_flight[5] + 1
        elif row[13] == '浙江':
            provice_flight[6] = provice_flight[6] + 1
        elif row[13] == '湖北':
            provice_flight[7] = provice_flight[7] + 1
        elif row[13] == '陕西':
            provice_flight[8] = provice_flight[8] + 1
        elif row[13] == '重庆':
            provice_flight[9] = provice_flight[9] + 1
        elif row[13] == '山东':
            provice_flight[10] = provice_flight[10] + 1
        elif row[13] == '湖南':
            provice_flight[11] = provice_flight[11] + 1
        elif row[13] == '福建':
            provice_flight[12] = provice_flight[12] + 1
        elif row[13] == '辽宁':
            provice_flight[13] = provice_flight[13] + 1
        elif row[13] == '河南':
            provice_flight[14] = provice_flight[14] + 1

    # 省和直辖市
    province_distribution = {'深圳': provice_flight[3], '河南': provice_flight[1], '北京': provice_flight[0], '河北': 21,
                             '辽宁': 12, '江西': 6, '上海': provice_flight[1], '安徽': 10, '江苏': provice_flight[5], '湖南': 9,
                             '浙江': 13, '海南': 2, '广东': provice_flight[2], '湖北': provice_flight[6], '黑龙江': 11, '澳门': 1,
                             '陕西': provice_flight[7], '四川': provice_flight[4], '内蒙古': 3, '重庆': 3, '云南': 6, '贵州': 2,
                             '吉林': 3, '山西': 12, '山东': provice_flight[9], '福建': 4, '青海': 1, '舵主科技，质量保证': 1,
                             '天津': provice_flight[10], '其他': 1}
    provice = list(province_distribution.keys())
    values = list(province_distribution.values())


    # 折线图
    line = Line()
    line.add("机场数量", city, provice_flight, mark_point=['average', 'max', 'min'], mark_point_symbol='diamond',
             mark_point_textcolor='#40ff27')
    return line



#不能关闭数据库，不然其他功能就无法实现
# cursor.close()
# db.close()



# def newLogin(request):
#     flag = 0
#     if request.method == 'POST':
#         # 获取用户通过post 提交过来的数据
#         user = request.POST.get('user', None)
#         pwd = request.POST.get('pwd', None)
#         p1 = int(pwd)
#         print('p1:',user, p1)
#         #用户专属的用户表user_password
#         sql = "select * from user"
#         cursor.execute(sql)
#         results = cursor.fetchall()
#         for row in results:
#             p = int(row[1])
#             print('p:',row[0], p)
#             if user == row[0] and p1 == p:
#                 # 找出用户最看重的元素
#                 userHighWeight = row[2]
#                 priceWeight = row[2]
#                 timeWeight = row[3]
#                 departureTimeWeight = row[4]
#                 companyWeight = row[5]
#                 typeWeight = row[6]
#                 ageWeight = row[7]
#                 punctualWeight = row[8]
#                 flag = 1
#                 for i in range(3,8):
#                     if userHighWeight < row[i]:
#                         userHighWeight = row[i]
#                         userHighPosition = i
#                 userHighWeight = userHighWeight/2
#                 print('userHighWeight',userHighWeight)
#                 return render(request, 'flightLine.html')
#                 # return redirect('/flightLine')
#             else:
#                 # 用户名密码不匹配
#                 error_msg = "用户名密码不匹配"
#         if flag == 0:
#             return HttpResponse('404.html')
#     # 打开urls里注册的连接后，调用views里的函数，然后先调用return render里的网页，然后提交表单
#     return render(request, 'newLogin.html')
def newLogin(request):
    flag = 0

    global userHighWeight
    # 用户最看重因素的位置
    global userHighPosition
    global priceWeight
    global timeWeight
    global departureTimeWeight
    global companyWeight
    global typeWeight
    global ageWeight
    global punctualWeight
    if request.method == 'POST':
        # 获取用户通过post 提交过来的数据
        user = request.POST.get('user', None)
        pwd = request.POST.get('pwd', None)
        p1 = int(pwd)
        print('p1:',user, p1)
        #用户专属的用户表user_password
        sql = "select * from user"
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            p = int(row[1])
            print('p:',row[0], p)
            if user == row[0] and p1 == p:
                # 找出用户最看重的元素
                userHighWeight = row[2]
                priceWeight = row[2]
                timeWeight = row[3]
                departureTimeWeight = row[4]
                companyWeight = row[5]
                typeWeight = row[6]
                ageWeight = row[7]
                punctualWeight = row[8]
                flag = 1
                for i in range(3,8):
                    if userHighWeight < row[i]:
                        userHighWeight = row[i]
                        userHighPosition = i
                userHighWeight = userHighWeight/2
                print('userHighWeight',userHighWeight)
                # return render(request, 'flightLine.html')
                # 改变url
                return redirect('/flightLine')
            else:
                # 用户名密码不匹配
                error_msg = "用户名密码不匹配"
        if flag == 0:
            return redirect('/404')
    # 打开urls里注册的连接后，调用views里的函数，然后先调用return render里的网页，然后提交表单
    return render(request, 'newLogin.html')




# 用于注册
def register(request):
    if request.method == 'POST':
        # 获取用户通过post 提交过来的数据
        user = request.POST.get('user', None)
        psw = request.POST.get('psw', None)
        price = request.POST.get('price', None)
        departureTime = request.POST.get('departureTime', None)
        time = request.POST.get('time', None)
        company = request.POST.get('company', None)
        type = request.POST.get('type', None)
        age = request.POST.get('age', None)
        punctual = request.POST.get('punctual', None)
        # 用户专属的用户表user_password
        global user_password
        user_password = user + "password"
        # sql = "insert into user(name, password, price, time, departureTime, company, type)values('%s', '%s', '%s', '%s', '%s', '%s', '%s');"
        # sql = "insert into user(name, password, price, time, departureTime, company, type) values ('wer', 4 ,5,5,5, 4 ,6);"
        psw1 = int(psw)
        price1 = int(price)
        departureTime1 = int(departureTime)
        time1 = int(time)
        company1 = int(company)
        type1 = int(type)
        sql = "insert into user(name, password, price, time, departureTime, company, type, age, punctual)values('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');"%(user, psw1, price1, departureTime1, time1, company1, type1, age, punctual)
        # sql = "insert into user(name, password, price, time, departureTime, company, type)values('%s', %d, %d, %d, %d, %d, %d);"%(user, psw1, price1, departureTime1, time1, company1, type1)
        cursor.execute(sql)
        db.commit()


    return render(request, 'register.html')  # 将绑定的数据传入前台

# 查询航线，进行推荐
# def flightLine(request):
#     context = {}
#     context['numberExhibition'] = '密码位'
#     if request.method == 'POST':
#         depCity = request.POST.get('depCity', None)
#         arrCity = request.POST.get('arrCity', None)
#         data = request.POST.get('data', None)
#         sql = "select * from fly"
#         cursor.execute(sql)
#         results = cursor.fetchall()
#         # for row in results:
#         #     # 用户最看重因素评分超过一半才会对航班进行评分
#         #     if row[14+userHighPosition] > 5:
#         #         if depCity == row[12] and arrCity == row[14] and data == row[10]:
#                     # bestPrice =
#
#
#     return render(request, 'flightLine.html',context)  # 将绑定的数据传入前台


def flightLine(request):
    global fromCity
    global toCity
    global airportName
    global airportPlace
    context = {}
    # weight = 0
    # bestNumber = 0
    # bestCompany = 0
    # bestType = 0
    # bestDepAirport = 0
    # bestAriAirport = 0
    # bestDepTime = 0
    # bestArrTime = 0
    # bestPrice = 0
    weight = 0
    bestNumber = ''
    bestCompany = ''
    bestType = ''
    bestDepAirport = ''
    bestAriAirport = ''
    bestDepTime = ''
    bestArrTime = ''
    bestPrice = ''
    if request.method == 'POST':
        fromCity = request.POST.get('fromCity', None)
        toCity = request.POST.get('toCity', None)
        data = request.POST.get('date2', None)
        sql = "select * from tryfly"
        cursor.execute(sql)
        results = cursor.fetchall()
        print(fromCity, toCity, data)
        if userHighPosition == '':
            return redirect('/404')
        elif fromCity == toCity:
            return redirect('/quireFault')
        else:
            for row in results:
                # 用户最看重因素评分超过一半才会对航班进行评分
                # if row[userHighPosition] > 5:
                    print('row[12]',row[12],row[14],row[10])
                    if fromCity == row[12] and toCity == row[14]:
                    # if fromCity == row[12] and toCity == row[14] and data == row[10]:
                        # 权重乘以评分等于本趟航班总评分
                        thisWeight = priceWeight*row[15] + timeWeight*row[16] + departureTimeWeight*row[17] + companyWeight*row[18] + typeWeight*row[19] + ageWeight*row[20] + punctualWeight*row[21]
                        if thisWeight > weight:
                            bestNumber =  row[1]
                            bestCompany = row[0]
                            bestType = row[4]
                            bestDepAirport = row[6]
                            bestAriAirport = row[8]
                            bestDepTime = row[5]
                            bestArrTime = row[7]
                            bestPrice = row[2]
                            airportName = row[6]
                            airportPlace = row[11]

    context['numberExhibition'] = bestNumber
    context['companyExhibition'] = bestCompany
    context['typeExhibition'] = bestType
    context['depAirExhibition'] = bestDepAirport
    context['arrAirExhibition'] = bestAriAirport
    context['depTimeExhibition'] = bestDepTime
    context['arrTimeExhibition'] = bestArrTime
    context['priExhibition'] = bestPrice
    return render(request, 'flightLine.html',context)  # 将绑定的数据传入前台


def airport(request):
    global airportName
    global airportPlace
    # airportName = '北京'
    # airportPlace = '北京'
    context = {}
    if airportName == '':
        return redirect('/quireFault')
    else:
        context['airportName'] = airportName
        context['airportPlace'] = airportPlace
        context['airportAmount'] = 0
        context['airportSort'] = 4


    # python中的数组长度是动态的,不用声明
    l = [0]
    provice_flight = l * 11

    city = ['北京', '上海', '广东', '深圳', '成都', '江苏', '湖北', '重庆', '陕西', '山东', '天津']
    # 机场信息放在airport这个数据库里
    sql = "select * from ctrip"
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        if row[14] == '北京':
            provice_flight[0] = provice_flight[0] + 1
        elif row[14] == '上海':
            provice_flight[1] = provice_flight[1] + 1
        elif row[14] == '广州' or '广东':
            provice_flight[2] = provice_flight[2] + 1
        elif row[14] == '厦门':
            provice_flight[3] = provice_flight[3] + 1
        elif row[14] == '成都':
            provice_flight[4] = provice_flight[4] + 1
        elif row[14] == '杭州' or '江苏':
            provice_flight[5] = provice_flight[5] + 1
        elif row[14] == '武汉' or '湖北':
            provice_flight[6] = provice_flight[6] + 1
        elif row[14] == '西安' or '陕西':
            provice_flight[7] = provice_flight[7] + 1
        elif row[14] == '重庆':
            provice_flight[8] = provice_flight[8] + 1
        elif row[14] == '青岛' or '山东':
            provice_flight[9] = provice_flight[9] + 1
        elif row[14] == '天津':
            provice_flight[10] = provice_flight[10] + 1

        # 将机场数量排序
        for j in range(0, 10):
            for i in range(0, 10-j):
                if provice_flight[i] > provice_flight[i + 1]:
                    temp = provice_flight[i]
                    provice_flight[i] = provice_flight[i + 1]
                    provice_flight[i + 1] = temp

        for i in range(0, 10):
            if airportPlace == city[i]:
                context['airportAmount'] = provice_flight[i]


    return render(request, 'airport.html', context)
