from matplotlib import pyplot as plt

x = range(2, 26, 2)
y = [15, 13, 14.5, 17, 20, 25, 26, 26, 27, 22, 18, 15]

# 在绘画之前要设置图片的大小
"""
figsize 是调节图片尺寸大小的,dpi是表示的图片的质量大小的，dpi越高说明质量越高。
"""
plt.figure(figsize=(20, 8), dpi=80)
# 开始绘图
plt.plot(x, y)

"""
设置x轴的刻度
"""
# plt.xticks(x)
# 也可以这样子进行编写 画图从2 开始然后画到25结束（其实是从2到24这个值）每隔1一个值进行划分
# plt.xticks(range(2, 25, 1))

# 想要传入0.5的话 会显示报错 可以写一个列表进行传递
_xtick_label = [i / 2 for i in range(4, 49)]
# 代表的是 从4到48 然后 在除以2 就是2 2.5 3 一直往后开始传递
plt.xticks(_xtick_label)

# 如果是下面的样子，代表的是 在25到50 才会有刻度，你传给这个函数才会有值，在之前都没有刻度
# plt.xticks(range(25, 50))

"""
y轴也是这样子，跟x轴样子差不多
"""
plt.yticks(range(min(y), max(y) + 1))  # 因为max(y)取不到，所以进行自加一即可

# plt.xticks(range(2, 25, 0.5))


# 进行保存绘制的图片
# 也可以进行不显示，直接进行文件的保存
# plt.savefig("./text1.svg")

# 展示图形
plt.show()
