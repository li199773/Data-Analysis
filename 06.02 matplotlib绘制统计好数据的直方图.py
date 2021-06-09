"""
直方图更多的应用场景：
1.用户的年龄分布状态
2.一段时间内用户点击次数的分布状态
3.用户活跃时间的分布状态

相关参数：
时间段：interval = [0,5,10,15,20,25,30,35,40,45,60,90] 就是x的数据
组距：width = [5,5,5,5,5,5,5,5,5,15,30,60]
y轴的数据 quantity = [836,2737,3723,3926,3596,1438,3273,642,824,613,215,47]
"""
from matplotlib import pyplot as plt
import matplotlib

matplotlib.rc("font", family=' DengXian')

plt.figure(figsize=(20, 8), dpi=80)

interval = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 60, 90]  # x轴的数据
width = [5, 5, 5, 5, 5, 5, 5, 5, 5, 15, 30, 60]  # 组距
quantity = [836, 2737, 3723, 3926, 3596, 1438, 3273, 642, 824, 613, 215, 47]  # y轴的数据

print(len(width))
print(len(quantity))

# 设置x轴的刻度
_x = [i - 0.5 for i in range(13)]
_xtick_labels = interval + [150]
plt.xticks(_x, _xtick_labels)

# 条形图与直方图是有区别的，width=1的话就会连在一起
plt.bar(range(len(quantity)), quantity, width=1)

plt.grid(alpha=0.4)
plt.show()
