"""
目标分析：
1.结合之前的matplotlib绘制出各自的评论数量的直方图
2.了解视频的评论数和喜欢数的关系，如何进行绘制改图
"""
import numpy as np
from matplotlib import pyplot as plt

# 传入文件的路径即可
us_file_path = "./archive/USvideos.csv"

# 加载本地的数据
t_us = np.loadtxt(us_file_path, delimiter=",", dtype="int")

# 取评论的数据
t_us_comment = t_us[:, -1]
# print(t_us_comment)

# 发现很多的数据主要集中在5000以下的地方，只取到5000以下的即可
t_us_comment = t_us_comment[t_us_comment <= 5000]
print(t_us_comment.max(), t_us_comment.min())

# 设置组距
d = 50
# 最大值-最小值，再去除以组距然后取整
bin_nums = (t_us_comment.max() - t_us_comment.min()) // d

# 绘制图形
plt.figure(figsize=(20, 8), dpi=80)
plt.hist(t_us_comment, bin_nums)
plt.show()

# 表示2者之间的关系的话使用散点图进行绘制
GB_file_path = "./archive/GBvideos.csv"
t_uk = np.loadtxt(GB_file_path, delimiter=",", dtype="int")

# 绘制图形之后发现数据点基本都在1000000以下，取这些点即可
t_uk = t_uk[t_uk[:, 1] <= 1000000]

t_uk_like = t_uk[:, 1]
t_uk_comment = t_uk[:, -1]

# 绘制图形
plt.figure(figsize=(20, 8), dpi=80)
plt.scatter(t_uk_like, t_uk_comment)
plt.show()
