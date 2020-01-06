* 网站一共三个URL  第一个页面是总的，其他两个页面是分的
###  html档描述
一类是包含合作项目可视化HTML文件example.html系列，另一类则是放置flask对应页面的HTML，在文件夹templates中。

其中result.html属于第一个页面对应“/”主页面，其中我通过设置了可以链接跳转的按钮（通过button和a实现）将两个按钮分别对应第二页面和第三页面，并使用了div对按钮内容进行包裹，使其在同一行呈现；在区别内容程度，我分别用了p,h1,h3进行包裹。

鉴于第二页面和第三页面呈现模式相同，因此使用base.html作为基础模板，body部分由page1.html和page2.html两者进行数据传递。

在page2.html中，通过form标签包裹select在第三个页面使用for循环设置下拉菜单以此选择内容的呈现；然后使用作为数据的提交按钮，完成页面数据的转换。

在所有HTML中都使用了{{ the_title }}此类（jinjia2语法的动态数据绑定，在py文件中有对应的可视化函数传输数据）分别对标题，内容，HTML表格和可视化图表进行数据传递。

###  python档描述
主要导入使用flask，pandas，plotly三个模块

通过pd.pd.read_csv()来读取csv当中的内容，并通过x.to_html()的形式将csv中的内容以HTML表格的形式呈现。

"/"为主页面，通过按钮可以跳转至第二页面"/second"和第三页面"/third"，其中HTML和可视图的数据传递和交互完成；前三个url皆是使用"get"的方式接收数据。
data_str = dict[the_region].to_html()，text = texts[the_region]，ending = endings[the_region]，链接通过接收到下拉框中的选项，以字典的方式获得对应的HTML表格（data_str）及小标题文字（text）和看图总结（ending)

###  webapp描述
第一页为首页面介绍分析“乌托邦式”下冰岛女性婚姻观的形成下数据故事的背景，引入接下来的分析内容，内容接近结尾处将通过两种情况对内容深入分析，因此设置了两个分页面的按钮（冰岛高生育率和高离婚率）和（冰岛女性社会地位），点击可分别进入第二页面和第三页面。

其中冰岛高生育率和高离婚率和冰岛女性社会地位顶部设置了返回的按钮,点击即可回到首页面。

在“冰岛女性社会地位”这个页面下还设有下拉菜单，分别就“冰岛国家会议中妇女参与的比例”，“全球各国女性就业率”和“全球女性的就业比率”可以看到三种分析的选择呈现。


###  交互页面
![第一页](https://images.gitee.com/uploads/images/2020/0106/000859_2544560a_2229424.png)
![第二页](https://images.gitee.com/uploads/images/2020/0106/001028_d87ec5c8_2229424.png)
![第二页](https://images.gitee.com/uploads/images/2020/0106/004819_75784f07_2229424.png)

* pythonanywhere链接：http://aylinwasson.pythonanywhere.com/
