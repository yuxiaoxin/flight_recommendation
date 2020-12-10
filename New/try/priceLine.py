from pyecharts import Map, Geo, Line, Radar
import pymysql

#python中的数组长度是动态的,不用声明

priceNum = []
y = []


db = pymysql.connect(host = 'localhost' ,port = 3306, user = 'root', passwd = '123456',database = 'airport', charset='utf8')
cursor = db.cursor()
sql = "select * from ctrip"
cursor.execute(sql)
results = cursor.fetchall()
i= 0
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


#折线图
line = Line()
line.add("成交量", y, priceNum, mark_point=[{"coord":[45,priceNum[45]]}], mark_point_symbol='diamond',
          mark_point_textcolor='#40ff27')
line.render()

