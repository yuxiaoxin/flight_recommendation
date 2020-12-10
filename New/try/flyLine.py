from pyecharts import GeoLines, Style

style = Style(
    title_top="#fff",
    title_pos="left",
    width=1000,
    height=800,
    background_color="#404a59"

)
fromCity = '北京'
toCity = '上海'
# s = "('%s', '%s')"%(fromCity,toCity)
data = [[fromCity,toCity]]

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

geolines.render()
