"""
假设知道了三天不同电影的票房记录，绘制一个更加直观的条形图来表示数据
实则是在一个条形图里面绘制不同的数据信息即可
a = ["猩球崛起3：终结之战", "敦刻尔克", "蜘蛛线：英雄归来", "战狼2"]
b_16 = [15746, 312, 4497, 319]
b_15 = [12357, 156, 2045, 168]
b_14 = [2358, 399, 2358, 362]

条形图的更多应用场景：
1.数量的统计
2.频率的统计（市场的饱和度）
"""
from matplotlib import pyplot as plt
import matplotlib

matplotlib.rc("font", family=' DengXian')

plt.figure(figsize=(20, 8), dpi=80)

a = ["猩球崛起3：终结之战", "敦刻尔克", "蜘蛛线：英雄归来", "战狼2"]
b_16 = [15746, 312, 4497, 319]
b_15 = [12357, 156, 2045, 168]
b_14 = [2358, 399, 2358, 362]

bar_width = 0.2

# 将每个第二个第三个条形图都往右移动0.2个单位即可
x_14 = list(range(len(a)))
x_15 = [i + bar_width for i in x_14]
x_16 = [i + bar_width * 2 for i in x_14]

plt.bar(range(len(a)), b_14, width=bar_width, color="red", label="9月14日")
plt.bar(x_15, b_15, width=bar_width, color="blue", label="9月15日")
plt.bar(x_16, b_16, width=bar_width, color="green", label="9月16日")
# 添加一个图例
plt.legend()

# 设置x轴的刻度
plt.xticks(x_15, a)

# 添加描述信息
plt.xlabel("电影名称")
plt.ylabel("票房记录")
plt.title("标题")

# 添加一个网格
plt.grid(alpha=0.4)

plt.show()
