from pyecharts import Bar, Line, Overlap
import pymysql


bar =Bar("区间分布")
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

# //由于雷达图传入的数据得为多维数据，所以这里需要做一下处理
radar_data1 = [priceThis]
radar_data2 = [priceNum]
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
overlap.render()