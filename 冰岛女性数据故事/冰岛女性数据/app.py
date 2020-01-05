
from flask import Flask, render_template, request
import pandas as pd
import cufflinks as cf
import plotly as py
import plotly.graph_objs as go


app = Flask(__name__)

# 准备工作
df = pd.read_csv('hurun.csv', encoding='utf-8', delimiter="\t")
regions_available = list(df.region.dropna().unique())
cf.set_config_file(offline=True, theme="ggplot")
py.offline.init_notebook_mode()



@app.route('/hhh',methods=['GET'])
def hu_run_2019():

    print('111')
    data_str = df.to_html()
    return render_template('index.html',
                           the_res = data_str,
                           the_select_region=regions_available)


@app.route('/hurun',methods=['POST'])
def hu_run_select() -> 'html':

    print('22')
    the_region = request.form["the_region_selected"]
    print(the_region) # 检查用户输入
    dfs = df.query("region=='{}'".format(the_region))
    df_summary = dfs.groupby("行业").agg({"企业名称":"count","估值（亿人民币）":"sum","成立年份":"mean"}).sort_values(by = "企业名称",ascending = False )
    print(df_summary.head(5)) # 在后台检查描述性统计
    ## user select
    # print(dfs)
    # 交互式可视化画图
    fig = dfs.iplot(kind="bar", x="行业", y="估值（亿人民币）", asFigure=True)
    py.offline.plot(fig, filename="example.html",auto_open=False)
    with open("example.html", encoding="utf8", mode="r") as f:
        plot_all = "".join(f.readlines())

    # plotly.offline.plot(data, filename='file.html')
    data_str = dfs.to_html()
    return render_template('results2.html',
                            the_plot_all = plot_all,
                            the_res = data_str,
                            the_select_region=regions_available,
                           )


@app.route('/',methods=['GET'])
def hu_page1() -> 'html':
    print('page111111111')
    import plotly as py
    import plotly.graph_objs as go
    pyplt = py.offline.plot
    labels = ["男性", "女性"]
    values = [50.17, 49.83]
    trace = [go.Pie(labels=labels, values=values)]
    layout = go.Layout(
        title="冰岛男女比例（%）",
    )
    fig = go.Figure(data=trace, layout=layout)
    # py.offline.iplot(fig)
    py.offline.plot(fig, filename="page1.html", auto_open=False)
    with open("page1.html", encoding="utf8", mode="r") as f:
        plot_all = "".join(f.readlines())

    # plotly.offline.plot(data, filename='file.html')
    data_str = pd.DataFrame(zip(labels,values)).to_html()

    import plotly as py
    import plotly.graph_objs as go
    pyplt = py.offline.plot
    labels = ["未婚父母", "已婚父母", "母亲", "父亲", "其他"]
    values = [67.61, 20.27, 10.61, 0.97, 0.54]
    trace = [go.Pie(labels=labels, values=values, hole=0.7, hoverinfo="label + percent")]
    layout = go.Layout(
        title="2017年冰岛0-5岁儿童的家庭成员组成情况",
    )
    fig = go.Figure(data=trace, layout=layout)
    py.offline.plot(fig, filename="page12.html", auto_open=False)
    with open("page12.html", encoding="utf8", mode="r") as f:
        plot_all2 = "".join(f.readlines())

    return render_template('index.html',
                            the_plot_all = plot_all,
                            the_plot_all2 = plot_all2,
                            the_res = data_str,
                            temp = '66'
                            # the_select_region=regions_available,
                           )


@app.route("/hello", methods=['GET', 'POST'])
def Hello():
    message = "hello"
    print(message)
    return render_template("page22.html", temp=message)



@app.route('/gopage2',methods=['GET', 'POST'])
def gopage2() -> 'html':
    print('page22222222')

    import plotly as py
    import plotly.graph_objs as go
    pyplt = py.offline.plot

    import pandas as pd
    import csv
    df = pd.read_csv('The divorce rate.csv', encoding='ANSI', index_col=['Name'])
    x轴 = [int(x) for x in df.columns.values]
    import plotly as py
    import plotly.graph_objs as go
    冰岛 = go.Scatter(
        x=[pd.to_datetime('01/01/{y}'.format(y=x), format="%m/%d/%Y") for x in df.columns.values],
        y=df.loc['Iceland', :].values, name='Iceland')
    瑞士 = go.Scatter(
        x=[pd.to_datetime('01/01/{y}'.format(y=x), format="%m/%d/%Y") for x in df.columns.values],
        y=df.loc['Switzerland', :].values, name='Switzerland')
    韩国 = go.Scatter(
        x=[pd.to_datetime('01/01/{y}'.format(y=x), format="%m/%d/%Y") for x in df.columns.values],
        y=df.loc['SouthKorea', :].values, name='SouthKorea')
    北欧国家 = go.Scatter(
        x=[pd.to_datetime('01/01/{y}'.format(y=x), format="%m/%d/%Y") for x in df.columns.values],
        y=df.loc['The Nordic countries', :].values, name='The Nordic countries')
    layout = dict(xaxis=dict(rangeselector=dict(buttons=list([
        dict(count=3,
             label="3年",
             step="year",
             stepmode="backward"),
        dict(count=5,
             label="5年",
             step="year",
             stepmode="backward"),
        dict(count=10,
             label="10年",
             step="year",
             stepmode="backward"),
        dict(count=20,
             label="20年",
             step="year",
             stepmode="backward"),
        dict(step="all")
    ])),
        rangeslider=dict(bgcolor="grey"),
        title='年份'
    ),
        yaxis=dict(title='不同地区总离婚率'),
        title="不同地区离婚情况"
    )
    fig = dict(data=[冰岛, 瑞士, 韩国, 北欧国家], layout=layout)

    # py.offline.iplot(fig)
    py.offline.plot(fig, filename="page21.html", auto_open=False)
    with open("page21.html", encoding="utf8", mode="r") as f:
        plot_all = "".join(f.readlines())

    # print(plot_all)
    print('wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww')

    df1 = pd.read_csv('The fertility rate.csv', encoding='ANSI', index_col=['Name'])
    import plotly as py
    import plotly.graph_objs as go
    pyplt = py.offline.plot

    trace_1 = go.Bar(
        x=[int(x) for x in df1.columns.values],
        y=df1.loc['冰岛', :].values, name='冰岛')

    trace_2 = go.Bar(
        x=[int(x) for x in df1.columns.values],
        y=df1.loc['世界水平', :].values, name='世界平均')

    trace_3 = go.Bar(
        x=[int(x) for x in df1.columns.values],
        y=df1.loc['欧洲联盟', :].values, name='欧盟')

    trace = [trace_1, trace_2, trace_3]

    layout = go.Layout(title="冰岛与欧盟国家、世界国家总生育率对比情况")

    figure = go.Figure(data=trace, layout=layout)

    # py.offline.iplot(figure, filename="page22.html")
    py.offline.plot(figure, filename="page22.html", auto_open=False)
    with open("page22.html", encoding="utf8", mode="r") as f:
        plot_all2 = "".join(f.readlines())

    return render_template('pages2.html',
                           the_plot_all=plot_all,
                           the_plot_all2=plot_all2,
                           # the_res=data_str,
                           temp='66'
                           # the_select_region=regions_available,
                           )



@app.route('/gopage3',methods=['GET', 'POST'])
def gopage3() -> 'html':
    print('page3333')
    import plotly as py
    import plotly.graph_objs as go
    pyplt = py.offline.plot

    import pandas as pd
    df = pd.read_csv("The proportion of women in the national parliament.csv", encoding='ANSI')
    x轴 = [1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016,
          2017, 2018]
    y轴 = [25.4, 25.4, 34.9, 34.9, 34.9, 34.9, 30.2, 30.2, 33.3, 33.3, 33.3, 33.3, 42.9, 42.9, 39.7, 39.7, 39.7, 39.7,
          41.3, 47.6, 47.6, 38.1, 38.1]
    import plotly as py
    import plotly.graph_objs as go

    冰岛 = go.Scatter(
        x=x轴,
        y=y轴,
    )

    layout = dict(xaxis=dict(rangeselector=dict(buttons=list([
        dict(count=3,
             label="3年",
             step="year",
             stepmode="backward"),
        dict(count=5,
             label="5年",
             step="year",
             stepmode="backward"),
        dict(count=10,
             label="10年",
             step="year",
             stepmode="backward"),
        dict(count=20,
             label="20年",
             step="year",
             stepmode="backward"),
        dict(step="all")
    ])),
        rangeslider=dict(bgcolor="grey"),
        title='年份'
    ),
        yaxis=dict(title='国家议会中女性参与的比例'),
        title="冰岛国家议会中女性参与的比例情况"
    )
    fig = dict(data=[冰岛], layout=layout)
    py.offline.plot(fig, filename="page3.html", auto_open=False)
    with open("page3.html", encoding="utf8", mode="r") as f:
        plot_all = "".join(f.readlines())

    # plotly.offline.plot(data, filename='file.html')
    data_str = pd.DataFrame(zip([1, 2], [2, 3])).to_html()

    df = pd.read_csv("country_female_ployment rate.csv", encoding='ANSI')
    print(df.columns)
    # print(df['YS2019'])
    from pyecharts.faker import Faker
    from pyecharts import options as opts
    from pyecharts.charts import Map
    from pyecharts.globals import ChartType, ThemeType

    def map_world(df) -> Map:
        # print(df.columns,'EEEEEEEEEEEEE')
        c = (
            Map()
                .add("2019年(%)", list(zip(list(df.country), list(df.YS2019))), 'world')
                .add("2018年(%)", list(zip(list(df.country), list(df.YS2018))), 'world')
                .add("2017年(%)", list(zip(list(df.country), list(df.YS2017))), 'world')
                .add("2016年(%)", list(zip(list(df.country), list(df.YS2016))), 'world')
                .add("2015年(%)", list(zip(list(df.country), list(df.YS2015))), 'world')
                .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
                .set_global_opts(
                visualmap_opts=opts.VisualMapOpts(max_=150, min_=5),
                title_opts=opts.TitleOpts(title="全球女性就业比率"),
            )
        )
        return c

    # map_world().render_notebook('page321.html')

    # map_world(df).render('page3211.html')
    print('ccccccccccccccccccc',map_world(df))
    # figure = go.Figure(data=map_world(df), layout=layout)
    # py.offline.plot(map_world(df), filename="page3211.html", auto_open=False)
    with open("全球女性就业比率.html", encoding="utf8", mode="r") as f:
        plot_all2 = "".join(f.readlines())



    df1 = pd.read_csv('country_female_ployment rate1.csv', encoding='ANSI')
    from pyecharts.faker import Faker
    from pyecharts import options as opts
    from pyecharts.charts import Bar

    def bar_vertical() -> Bar:
        bar = (
            Bar()
                .add_xaxis(
                ['冰岛', '尼泊尔', '老挝', '瑞士', '荷兰', '澳大利亚', '加拿大', '丹麦', '越南', '挪威', '新西兰', '英国', '瑞典', '北美', '美国', '德国',
                 '芬兰', '中国', '日本', '中国香港特别行政区', '马尔代夫', '爱尔兰', '新加坡', '巴西', '哥伦比亚', '泰国', '大韩民国', '不丹', '法国'])
                .add_yaxis("2017",
                           [76.71, 74.37, 63.56, 62.45, 61.61, 58.69, 56.96, 56.83, 52.24, 50.05, 51.29, 48.79, 45.85,
                            46.31, 44.77, 44.52, 41.81, 40.9, 41.4, 37.81, 37.96, 40.52, 35.95, 35.25, 34.42, 32.22,
                            31.03, 31.98, 25.53], gap="0%", color="#285171")
                .add_yaxis("2018",
                           [78.27, 74.35, 62.11, 62.58, 61.48, 58.61, 57.04, 56.72, 50.56, 49.97, 51.57, 49.02, 44.74,
                            46.4, 44.85, 44.22, 41.7, 40.53, 41.83, 37.18, 38.46, 41.61, 35.86, 35.69, 34.69, 32.32,
                            31.14, 30.7, 23.99], gap="0%", color="#82c0af")
                .add_yaxis("2019",
                           [76.36, 74.38, 63.28, 62.58, 61.63, 58.68, 57.19, 56.13, 53.21, 51.77, 51.04, 49.33, 46.17,
                            46.09, 44.94, 44.18, 43.14, 42.98, 40.79, 37.68, 37.55, 37.37, 36.19, 36.01, 35.27, 32.63,
                            30.93, 30.92, 26.14], gap="0%", color="#dad4b9")
                .set_global_opts(
                title_opts=opts.TitleOpts(title="各国女性就业率对比"),
                datazoom_opts=opts.DataZoomOpts(orient="vertical"))
                .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
                .reversal_axis()
        )

        return bar

    # bar_vertical().render_notebook()
    # bar_vertical().render('各国女性就业比率对比.html')
    # py.offline.plot(fig, filename="page32.html", auto_open=False)
    with open("各国女性就业比率对比.html", encoding="utf8", mode="r") as f:
        plot_all3 = "".join(f.readlines())
    # print(plot_all3)
    # py.offline.plot(fig, filename="page323.html", auto_open=False)
    # with open("page323.html", encoding="utf8", mode="r") as f:
    #     plot_all3 = "".join(f.readlines())


    return render_template('pages3.html',
                           the_plot_all=plot_all,
                           the_plot_all2=plot_all2,
                           # the_plot_all2=map_world(df1).render_embed(),
                           the_plot_all3=plot_all3,
                           the_res=data_str,
                           temp='66'
                           # the_select_region=regions_available,
                           )
    # return render_template('各国女性就业比率对比.html',
    #                        the_plot_all=plot_all,
    #                        the_plot_all2=plot_all2,
    #                        # the_plot_all2=map_world(df1).render_embed(),
    #                        the_plot_all3=bar_vertical().dump_options(),
    #                        the_res=data_str,
    #                        temp='66'
    #                        # the_select_region=regions_available,
    #                        )


if __name__ == '__main__':
    app.run(debug=True,port=8000)
