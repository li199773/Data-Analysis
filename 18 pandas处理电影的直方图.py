"""
目标需求：
对于这一组的电影数据，如果我们像rating，runtime的分布情况，应该如何呈现数据？
"""
# 1.runtime的分布情况
import pandas as pd
from matplotlib import pyplot as plt

IMDB_Movie_Data = pd.read_csv("./IMDB-Movie-Data.csv")

# 检测相关信息的输出
# print(IMDB_Movie_Data.head())
print(IMDB_Movie_Data.info())

# rating，runtime的分布情况
# 选择图形，直方图
# 准备数据
runtime_data = IMDB_Movie_Data["Runtime (Minutes)"].values
max_runtime = runtime_data.max()
min_runtime = runtime_data.min()

# 计算组数
num_bin = (max_runtime - min_runtime) // 5
print(max_runtime - min_runtime)

# 设置图片的大小
plt.figure(figsize=(20, 8), dpi=80)

# 绘制图片
plt.hist(runtime_data, num_bin)
# 设置x轴的刻度
plt.xticks(range(min_runtime, max_runtime + 5, 5))

# plt.show()
# print(IMDB_Movie_Data["Rating"].values)

# 2.rating 分布情况 0-10 打分
Rating_data = IMDB_Movie_Data["Rating"].values
max_Rating = Rating_data.max()
min_Rating = Rating_data.min()

# 计算组数
print(max_Rating, min_Rating)
num_bin_list = [1.6]
num_bin_list = [1.6]+[0.5]*11

# 设置图片的大小
plt.figure(figsize=(20, 8), dpi=80)
# 绘制图片
plt.hist(Rating_data, num_bin_list)

_x = [min_Rating]
i = min_Rating
while i <= max_Rating + 0.5:
    i = i + 0.5
    _x.append(i)

# 设置x轴的刻度
plt.xticks(_x)
plt.show()
