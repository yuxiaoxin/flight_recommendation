from pyecharts import Map, Geo, Line
import pymysql

#python中的数组长度是动态的,不用声明
provice_flight = []
for i in range(15):
    provice_flight.append(0)


city = ['北京','上海','广东','天津','云南','四川','浙江','湖北', '陕西','重庆', '山东','湖南','福建','辽宁','河南']
#机场信息放在airport这个数据库里
db = pymysql.connect(host = 'localhost' ,port = 3306, user = 'root', passwd = '123456',database = 'airport', charset='utf8')
cursor = db.cursor()
sql = "select * from ctrip"
cursor.execute(sql)
results = cursor.fetchall()
for row in results:
    if row[13] == '北京':
        provice_flight[0] = provice_flight[0]+1
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
province_distribution = {'深圳':provice_flight[3], '河南': provice_flight[1], '北京': provice_flight[0], '河北': 21, '辽宁': 12, '江西': 6, '上海': provice_flight[1], '安徽': 10, '江苏': provice_flight[5], '湖南': 9, '浙江': 13, '海南': 2, '广东': provice_flight[2], '湖北': provice_flight[6], '黑龙江': 11, '澳门': 1, '陕西': provice_flight[7], '四川': provice_flight[4], '内蒙古': 3, '重庆': 3, '云南': 6, '贵州': 2, '吉林': 3, '山西': 12, '山东': provice_flight[9], '福建': 4, '青海': 1, '舵主科技，质量保证': 1, '天津': provice_flight[10], '其他': 1}
provice=list(province_distribution.keys())
values=list(province_distribution.values())


map = Map("中国地图",'中国地图', width=1200, height=600)
map.add("", provice, values, visual_range=[0, 50],  maptype='china', is_visualmap=True,
    visual_text_color='#000')
map.show_config()
map.render(path="./中国地图.html")


#折线图
line = Line()
print(provice_flight)
line.add("成交量", city, provice_flight, mark_point=['average', 'max', 'min'], mark_point_symbol='diamond',
          mark_point_textcolor='#40ff27')
line.render()
