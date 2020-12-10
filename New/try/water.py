from pyecharts import Liquid, Polar, Radar
#
rate = 0.6
# 圆形水球
liquid2 =Liquid("水球图示例")
liquid2.add("Liquid", [rate, 0.5, 0.4, 0.3], is_liquid_outline_show=False)
# liquid2.add("Liquid", [0.6, 0.5, 0.4, 0.3], is_liquid_outline_show=False)
liquid2.show_config()
liquid2.render(path='圆形水球.html')

# # 菱形水球
# liquid3 =Liquid("水球图示例")
# liquid3.add("Liquid", [0.6, 0.5, 0.4, 0.3], is_liquid_animation=False, shape='diamond')
# liquid3.show_config()
# liquid3.render(path='./data/03-03菱形水球.html')
