from pyecharts import Map, Geo, Line
import pymysql

#python中的数组长度是动态的,不用声明
l=[0]
provice_flight = l*30
city = ['北京','上海','广东','深圳','成都','江苏','湖北','重庆','','']
#机场信息放在airport这个数据库里
db = pymysql.connect(host = 'localhost' ,port = 3306, user = 'root', passwd = '123456',database = 'airport', charset='utf8')
cursor = db.cursor()
sql = "select * from fly"
cursor.execute(sql)
results = cursor.fetchall()
for row in results:
    if row[3][0:2] == '北京':
        provice_flight[0] = provice_flight[0]+1
    elif row[3][0:2] == '上海':
        provice_flight[1] = provice_flight[1] + 1
    elif row[3][0:2] == '广州' or '广东':
        provice_flight[2] = provice_flight[2] + 1
    elif row[3][0:2] == '深圳':
        provice_flight[3] = provice_flight[3] + 1
    elif row[3][0:2] == '成都':
        provice_flight[4] = provice_flight[4] + 1
    elif row[3][0:2] == '杭州' or '江苏':
        provice_flight[5] = provice_flight[5] + 1
    elif row[3][0:2] == '武汉' or '湖北':
        provice_flight[6] = provice_flight[6] + 1
    elif row[3][0:2] == '西安' or '陕西':
        provice_flight[7] = provice_flight[7] + 1
    elif row[3][0:2] == '重庆':
        provice_flight[8] = provice_flight[8] + 1
    elif row[3][0:2] == '青岛' or '山东':
        provice_flight[9] = provice_flight[9] + 1
    elif row[3][0:2] == '天津':
        provice_flight[10] = provice_flight[10] + 1


# 省和直辖市
province_distribution = {'深圳':provice_flight[3], '河南': provice_flight[1], '北京': provice_flight[0], '河北': 21, '辽宁': 12, '江西': 6, '上海': provice_flight[1], '安徽': 10, '江苏': provice_flight[5], '湖南': 9, '浙江': 13, '海南': 2, '广东': provice_flight[2], '湖北': provice_flight[6], '黑龙江': 11, '澳门': 1, '陕西': provice_flight[7], '四川': provice_flight[4], '内蒙古': 3, '重庆': 3, '云南': 6, '贵州': 2, '吉林': 3, '山西': 12, '山东': provice_flight[9], '福建': 4, '青海': 1, '舵主科技，质量保证': 1, '天津': provice_flight[10], '其他': 1}
provice=list(province_distribution.keys())
values=list(province_distribution.values())




#折线图
line = Line()
line.add("成交量", city, provice_flight)
line.render()