from matplotlib import pyplot as plt
import matplotlib

matplotlib.rc("font", family=' DengXian')

plt.figure(figsize=(20, 8), dpi=80)

y_3 = [11, 17, 16, 11, 12, 11, 12, 6, 6, 7, 8, 9, 12, 15, 14, 17, 18, 21, 16, 17, 20, 14, 15, 15, 15, 19, 21, 22, 22, 22, 23]
y_10 = [26, 26, 28, 19, 21, 17, 16, 19, 18, 20, 20, 19, 22, 23, 17, 20, 21, 20, 22, 15, 11, 15, 5, 13, 17, 10, 11, 13, 12, 13, 6]

x_3 = range(1, 32)
x_10 = range(51, 82)

# 设置x轴的刻度
_x = list(x_3) + list(x_10)
_xtick_label = ["3月{}日".format(i) for i in x_3]
_xtick_label += ["10月{}日".format(i - 50) for i in x_10]
plt.xticks(list(_x)[::3], list(_xtick_label)[::3], rotation=45)

# 设置x y轴标题
plt.xlabel("日期")
plt.ylabel("温度(℃)")
plt.title("标题")

# 使用 scatter 来绘制散点图
plt.scatter(x_3, y_3, label="3月份")
plt.scatter(x_10, y_10, label="10月份")

plt.legend()

plt.show()
