from pyecharts import Gauge

gu = Gauge("航班折扣")
gu.add("全额", "折扣", 61)

gu.render("Guage-eg.html")