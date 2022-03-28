import random
from pyecharts import options as opts
from pyecharts.charts import Page, Pie

pie = (
    Pie()
    .add('鼠标选中分区后的tip',
         [list(z) for z in zip(['20{}年第{}季'.format(year,season)
                                        for year in [20]  # count 2
                                                for season in range(1,5)] # count 2
                ,[random.randint(2, 10) for _ in range(8)])]) # count 8
    .set_series_opts(label_opts=opts.LabelOpts(formatter='{b}: {c}万套'))
    .set_global_opts(title_opts=opts.TitleOpts(title='饼图实例-近两年季度销售'),
                         legend_opts=opts.LegendOpts(is_show=False))
)
pie.render('饼图.html')
