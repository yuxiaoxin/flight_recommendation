from pyecharts import Pie
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

# //设置行名
city = ['北京','上海','广东','天津','云南','四川','浙江','湖北', '陕西','重庆', '山东','湖南','福建','辽宁','河南']

columns = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# //设置主标题与副标题，标题设置居中，设置宽度为900
pie = Pie("饼状图", "各省机场数量",title_pos='center',width=900)
# //加入数据，设置坐标位置为【25，50】，上方的colums选项取消显示
pie.add("机场数", city, provice_flight ,center=[25,50],is_legend_show=False,is_label_show=True)


pie.render()