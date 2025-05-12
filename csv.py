from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.globals import ThemeType

# 创建图表时指定主题
bar_chart = Bar(init_opts=opts.InitOpts(theme=ThemeType.DARK))
# 后续再进行其他配置
bar_chart.add_xaxis(["A", "B", "C", "D"])
bar_chart.add_yaxis("数据", [10, 20, 30, 40])
bar_chart.set_global_opts(title_opts=opts.TitleOpts(title="示例图表"))
bar_chart.render("f:/bar_chart.html")

import os
print(os.getcwd())
