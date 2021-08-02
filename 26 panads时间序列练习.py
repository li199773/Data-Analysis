"""
1.统计出数据不同类型的紧急情况的次数
2.统计出不同月份不同类型紧急电话的次数的变化情况
"""
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import matplotlib

matplotlib.rc("font", family=' DengXian')

nine11_data = pd.read_csv("./911.csv")

# 显示所有的行和列的详细信息，不会有省略号
pd.set_option('display.max_columns', None)
# 检查数据
# print(nine11_data.head(10))
# print(nine11_data.info())

# 1.统计出数据不同类型的紧急情况的次数
# 不同类型的紧急情况分组，在title里面的第一个EMS，Fire，Traffic等情况，进行切割即可
# 获取分类的情况

# df = nine11_data["title"].str.split(":") # 不能直接进行取值为0
temp_list = nine11_data["title"].str.split(":").tolist()  # 进行转化成一个列表
cate_list = list(set([i[0] for i in temp_list]))  # 进行去重的操作

# print(cate_list)

# 构造全为0的数组
# 定义列索引为cate_list的值
zeros_nine11_data = pd.DataFrame(np.zeros((nine11_data.shape[0], len(cate_list))), columns=cate_list)
# print(zeros_nine11_data)

# 进行赋值
for cate in cate_list:
    zeros_nine11_data[cate][nine11_data["title"].str.contains(cate)] = 1
# print(zeros_nine11_data)

# 对每一个类型的数据进行求和即可
sum_ret = zeros_nine11_data.sum(axis=0)
# print(sum_ret)

# 进行画图
plt.figure(figsize=(20, 8), dpi=80)

# 传入xy的值
_x = sum_ret.index
_y = sum_ret.values

# 调整大小
plt.bar(_x, _y, width=0.3)
plt.xticks()
plt.grid()

# 添加描述信息
plt.xlabel("911紧急情况的类型")
plt.ylabel("数量")
plt.title("911紧急情况的次数")

# plt.show()

# 2.统计出不同月份不同类型紧急电话的次数的变化情况
# 变化的情况使用折线图
# print(temp_list)
print("*" * 100)
cate_list_2 = [i[0] for i in temp_list]
# print(cate_list_2)
# 添加其中的一列就好,在进行分组
nine11_data["cate"] = pd.DataFrame(np.array(cate_list_2).reshape((nine11_data.shape[0], 1)))
# print(cate_df)

print(nine11_data.groupby(by="cate").count()["title"])

# 时间序列的学习：
# 虽然可以使用切割来获取年月的数据，有更为简单的处理方法：时间序列：
t1 = pd.date_range(start="20210624", end="20210731", freq="D")
print(t1)
# 即从2021-06-24一直输出到2021-07-31

# 每隔10天进行取值
t2 = pd.date_range(start="20210624", end="20210731", freq="10D")
print(t2)

# 控制输出数据的个数：
# 注意：有periods,不能与end连用
t3 = pd.date_range(start="20210624", freq="D", periods=10)
print(t3)

# 按月进行输出：
t4 = pd.date_range(start="20210624", freq="M", periods=10)
print(t4)

index = pd.date_range("20210624", periods=10)
df1 = pd.DataFrame(np.random.rand(10), index=index)
print(df1)
print("*" * 100)
