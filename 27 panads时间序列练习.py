import pandas as pd
from matplotlib import pyplot as plt
import matplotlib
import numpy as np

matplotlib.rc("font", family=' DengXian')

nine11_data = pd.read_csv("./911.csv")

# 显示所有的行和列的详细信息，不会有省略号
pd.set_option('display.max_columns', None)

# 重采样的学习：
# to_datetime对timeStamp这一列进行获取时间序列
t1 = pd.to_datetime(nine11_data["timeStamp"])
# print(t1)

nine11_data["timeStamp"] = pd.to_datetime(nine11_data["timeStamp"])
nine11_data.set_index("timeStamp", inplace=True)
# 检查数据
# print(nine11_data.head(5))

# 统计出911数据中不同月份电话的次数
count_by_month = nine11_data.resample("M").count()["title"]
print(count_by_month)

# 画图
_x_nine11 = count_by_month.index
_y_nine11 = count_by_month.values

# 调整画布的大小
plt.figure(figsize=(20, 8), dpi=80)

plt.grid()
plt.plot(_x_nine11, _y_nine11)
plt.xticks(list(_x_nine11)[::1], rotation=45)
plt.show()

# 2. 统计出911数据中心不同月份不同类型的电话的次数的变化情况
nine11_data = pd.read_csv("./911.csv")
nine11_data["timeStamp"] = pd.to_datetime(nine11_data["timeStamp"])

# 添加类，表示分类:
temp_list = nine11_data["title"].str.split(":").tolist()  # 进行转化成一个列表
cate_list = [i[0] for i in temp_list]
nine11_data["cate"] = pd.DataFrame(np.array(cate_list).reshape((nine11_data.shape[0], 1)))
# 使其变成一个具有cate的数组，变成一列
nine11_data.set_index("timeStamp", inplace=True)

# 调整画布的大小
plt.figure(figsize=(20, 8), dpi=80)

# 进行分组
for group_name, group_data in nine11_data.groupby(by="cate"):
    # 对不同的分类进行绘图即可
    count_by_month = group_data.resample("M").count()["title"]

    # 画图
    _x_nine11_2 = count_by_month.index
    _y_nine11_2 = count_by_month.values

    plt.grid()
    plt.plot(_x_nine11_2, _y_nine11_2, label=group_name)

plt.xticks(list(_x_nine11_2)[::1], rotation=45)
plt.legend(loc="best")
plt.show()
