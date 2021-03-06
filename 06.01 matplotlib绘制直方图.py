"""
假设你获取到了250部电影的时长在列表 a 中,希望统计出来电影的时长分布状况（比如时长为100分钟到120分钟的电影的数量，出现的频率等等信息，如何进行呈现）
一般遇到这种数据量比较大的时候，尽量采用直方图进行呈现。
a = [105, 130, 134, 137, 115, 130, 114, 140, 96, 125, 150, 136, 97, 128, 129, 147, 148, 135, 138, 114, 141, 92, 126, 101, 148, 118, 92, 107, 132, 141, 131, 112, 122, 126, 126, 95, 127,
 145, 111, 123, 98, 123, 142, 112, 134, 129, 111, 96, 110, 112, 131, 130, 133, 150, 138, 112, 136, 112, 91, 126, 96, 113, 147, 122, 143, 140, 136, 116, 149, 114, 97, 143, 137, 115,
  103, 120, 133, 105, 124, 108, 140, 105, 119, 146, 139, 128, 96, 130, 147, 94, 138, 129, 135, 106, 147, 113, 127, 137, 123, 135, 116, 105, 143, 144, 146, 95, 148, 147, 100, 135,
  115, 98, 137, 136, 125, 135, 106, 144, 99, 125, 105, 100, 105, 114, 123, 137, 108, 127, 108, 122, 106, 122, 91, 104, 125, 107, 123, 120, 112, 137, 128, 116, 101, 120, 96, 142,
  128, 103, 96, 144, 135, 135, 144, 105, 110, 122, 119, 128, 131, 94, 142, 146, 129, 105, 93, 138, 131, 114, 142, 110, 121, 122, 102, 146, 140, 127, 108, 134, 90, 122, 115, 115, 109,
   113, 142, 136, 110, 95, 129, 94, 116, 128, 145, 147, 148, 101, 97, 134, 97, 101, 113, 150, 105, 98, 110, 123, 139, 94, 149, 119, 95, 108, 141, 103, 116, 140, 108, 106, 97, 146,
    134, 110, 91, 105, 110, 143, 135, 123, 128, 146, 131, 118, 148, 139, 117, 138, 141, 130, 129, 129, 90, 143, 132, 149, 124, 121, 146, 106, 140, 108]

plt.hist方法是那些没有统计过的数据,没有办法绘制直方图。
"""

# 可以使用以下代码进行随机获取90-150之间的250个数据
# import random
#
# y = [random.randint(90, 150) for i in range(250)]
# print(y)

from matplotlib import pyplot as plt
import matplotlib

matplotlib.rc("font", family=' DengXian')

plt.figure(figsize=(20, 8), dpi=80)

a = [105, 130, 134, 137, 115, 130, 114, 140, 96, 125, 150, 136, 97, 128, 129, 147, 148, 135, 138, 114, 141, 92, 126, 101, 148, 118, 92, 107, 132, 141, 131, 112, 122, 126, 126, 95,
     127, 145, 111, 123, 98, 123, 142, 112, 134, 129, 111, 96, 110, 112, 131, 130, 133, 150, 138, 112, 136, 112, 91, 126, 96, 113, 147, 122, 143, 140, 136, 116, 149, 114, 97, 143,
     137, 115, 103, 120, 133, 105, 124, 108, 140, 105, 119, 146, 139, 128, 96, 130, 147, 94, 138, 129, 135, 106, 147, 113, 127, 137, 123, 135, 116, 105, 143, 144, 146, 95, 148,
     147, 100, 135, 115, 98, 137, 136, 125, 135, 106, 144, 99, 125, 105, 100, 105, 114, 123, 137, 108, 127, 108, 122, 106, 122, 91, 104, 125, 107, 123, 120, 112, 137, 128, 116,
     101, 120, 96, 142, 128, 103, 96, 144, 135, 135, 144, 105, 110, 122, 119, 128, 131, 94, 142, 146, 129, 105, 93, 138, 131, 114, 142, 110, 121, 122, 102, 146, 140, 127, 108, 134,
     90, 122, 115, 115, 109, 113, 142, 136, 110, 95, 129, 94, 116, 128, 145, 147, 148, 101, 97, 134, 97, 101, 113, 150, 105, 98, 110, 123, 139, 94, 150, 119, 95, 108, 141, 103,
     116, 140, 108, 106, 97, 146, 134, 110, 91, 105, 110, 143, 135, 123, 128, 146, 131, 118, 148, 139, 117, 138, 141, 130, 129, 129, 90, 143, 132, 149, 124, 121, 146, 106, 140,
     108]

# 计算组距
d = 3  # 组距
num_bins = (max(a) - min(a)) // d  # 进行整除然后取整
print(max(a))
print(min(a))
print(num_bins)
plt.hist(a, num_bins, density=True)  # density=True 为计频数意思

# 这里进行设置x y轴的刻度值
plt.xticks(range(min(a), max(a) + d, d))
# plt.yticks(range(0, 20))

# 添加描述信息
plt.xlabel("电影时长")
plt.ylabel("数量")
plt.title("标题")

# 添加一个网格
plt.grid(alpha=0.4)

plt.show()
