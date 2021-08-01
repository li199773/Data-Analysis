"""
项目需求：
现在我们有全球排名前10000本书的数据，统计一下：
    1.不同年份书的数量
    2.不同年份书的平均评分情况
"""
# 1.不同年份书的数量
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib

matplotlib.rc("font", family=' DengXian')

books_data = pd.read_csv("./books.csv")

# 显示所有的行和列的详细信息，不会有省略号
pd.set_option('display.max_columns', None)
# 检查数据
# print(books_data.head(1))
print(books_data.info())

# 对original_publication_year进行取值，里面有缺失要进行处理
# 对年份不为nan的书的年份进行提取
# dropnan在这里不太合适，会把其他的为nan的数据都给删掉了
books_data_notnull = books_data[pd.notnull(books_data["original_publication_year"])]
# books_data_notnull = books_data[books_data["original_publication_year"] != "nan"]
# print(books_data_notnull, type(books_data_notnull))

data = books_data_notnull.groupby(by="original_publication_year").count()["id"].sort_values(ascending=False)
print(type(data))
print(data)
# 输出类型为<class 'pandas.core.series.Series'>

# 设置x y 轴的相关的数据，取最近50年的即可
_x = data.index[:50]
_y = data.values[:50]

# 调整画布的大小
plt.figure(figsize=(20, 8), dpi=80)
plt.grid()
plt.bar(_x, _y)
plt.show()
print("/" * 100)

# 2.不同年份书的平均评分情况：二者之间的情况使用折线图，柱状图也可以
# 对年份不为nan的书的年份进行提取
grouped = books_data_notnull["average_rating"].groupby(by=books_data_notnull["original_publication_year"]).mean()
# print(grouped)

# 传入xy的数据
average_x = grouped.index
average_y = grouped.values

# 进行画图
plt.figure(figsize=(20, 8), dpi=80)

plt.plot(range(len(average_x)), average_y)
print(len(average_x))

# 强制转换成整数，不要小数
# 并且旋转45度
plt.xticks(list(range(len(average_x)))[::10], average_x[::10].astype(int), rotation=45)
plt.show()
