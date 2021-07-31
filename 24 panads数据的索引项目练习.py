"""
1.使用matplotlib呈现出店铺总数排名前10的国家
"""
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib

matplotlib.rc("font", family=' DengXian')

directory = pd.read_csv("./directory.csv")

# 显示所有的行和列的详细信息，不会有省略号
pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)

# 使用matplotlib呈现出店铺总数排名前10的国家
# 准备数据
# 按照城市进行分组 默认情况为升序，改成降序即可
Country_data = directory.groupby(by="Country").count()["Brand"].sort_values(ascending=False)[:10]

_x = Country_data.index
_y = Country_data.values

# 进行画图
plt.figure(figsize=(20, 8), dpi=80)

# plt.bar(range(len(_x)),_y)
plt.bar(_x, _y)
plt.show()

"""
2.使用matplotlib呈现出中国每个城市店铺的数量
"""
directory_CN = directory[directory["Country"] == "CN"]
print(directory_CN, type(directory_CN))

# 按照城市进行分组 默认情况为升序，改成降序即可
city_data = directory_CN.groupby(by="City").count()["Brand"].sort_values(ascending=False)[:50]
print(type(city_data))

_x_1 = city_data.index
_y_1 = city_data.values

# 进行画图
plt.figure(figsize=(20, 8), dpi=80)

plt.xticks(rotation=90)
plt.bar(_x_1, _y_1, width=0.3, color="orange")

plt.grid()

plt.show()

# 也可以进行画出横的条形图
plt.figure(figsize=(20, 11), dpi=80)

plt.barh(_x_1, _y_1, height=0.5, color="orange")
plt.grid()

# 添加描述信息
plt.xlabel("城市Starbucks的数量")
plt.ylabel("城市名称")
plt.title("每个城市Starbucks的数量对比图")

plt.show()
