from pyecharts import Map, Geo, Line, Radar
import pymysql

#python中的数组长度是动态的,不用声明

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
        print(price)
        if price < 800:
            priceThis[0] = priceThis[0] + 1
        elif 800< price < 1000:
            priceThis[1] = priceThis[1] + 1
        elif 1000< price < 1500:
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
    ("0~800", 8000), ("800~1000",3000), ("1000~1500", 3000),
    ("1500~2000", 500), ("2000~2500", 200), ("2500~3000", 50),
    ("3000~", 50)
]
# //传入坐标
radar.config(schema)
radar.add("本趟航班",radar_data1)
# //一般默认为同一种颜色，这里为了便于区分，需要设置item的颜色
radar.add("所有航班",radar_data2,item_color="#1C86EE")
radar.render()

