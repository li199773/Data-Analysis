"""
我们有北上广，深圳，和沈阳5个城市的空气质量数据源，请绘制出5个城市的PM2.5随时间的变化情况
"""
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib

matplotlib.rc("font", family=' DengXian')

Beijing = pd.read_csv("./PM2.5/BeijingPM20100101_20151231.csv")

# 显示所有的行和列的详细信息，不会有省略号
pd.set_option('display.max_columns', None)
print(Beijing.head())
print(Beijing.info())

# 读出信息数据发现年月日小时都是分开的
# 不是字符串，要进行处理：
period = pd.PeriodIndex(year=Beijing["year"], month=Beijing["month"], day=Beijing["day"], hour=Beijing["hour"], freq="H")
# print(period, type(period))
# 在原来的数据集上在添加一列
Beijing["datatime"] = period

# 把datatime设置成索引
Beijing.set_index("datatime", inplace=True)

# 按照天进行采样
# 1.处理缺失的数据,删除缺失的数据,以 PM_US Post为基准
data_1 = Beijing["PM_US Post"].dropna()
# 画图
plt.figure(figsize=(20, 8), dpi=80)
_x = data_1.index
_y = data_1.values
plt.grid()
plt.plot(range(len(_x)), _y)  # 变化使用折线图就好
plt.xticks(range(0, len(_x), 20), list(_x)[::20])
plt.show()
# print("**" * 100)

# 可以按照月进行分析，因为数据量太大了，所以可以进行重采样
# 进行重采样
Beijing = pd.read_csv("./PM2.5/BeijingPM20100101_20151231.csv")
period = pd.PeriodIndex(year=Beijing["year"], month=Beijing["month"], day=Beijing["day"], hour=Beijing["hour"], freq="H")
Beijing["datatime"] = period
Beijing.set_index("datatime", inplace=True)

Beijing = Beijing.resample("M").mean()
print(Beijing)
data_2 = Beijing["PM_US Post"].dropna()
# 画图
plt.figure(figsize=(20, 8), dpi=80)
_x_2 = data_2.index
_y_2 = data_2.values
plt.grid()
plt.plot(range(len(_x_2)), _y_2)  # 变化使用折线图就好
plt.xticks(range(0, len(_x_2), 3), list(_x_2)[::3])
plt.show()
