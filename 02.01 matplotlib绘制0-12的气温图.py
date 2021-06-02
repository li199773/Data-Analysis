"""
目标分析：
构建一个2个小时的气温图
"""
from matplotlib import pyplot as plt
import random  # 随机在一定的范围内产生一个随机数字

# 5.进行中文的转换，不用死记硬背，去理解就好，去寻找函数的定义即可
# 5.1 第一种方法
import matplotlib

matplotlib.rc("font", family=' DengXian')
# 也可以写下面这种的方式，首选上面的这个形式
# font = {'family': 'MicroSoft YaHei',
#         'weight': 'bold',
#         'size': 'larger'}
# matplotlib.re("font", **font)
# 5.2
# from matplotlib import font_manager
# my_font = font_manager.FontProperties(fname=字体的路径 在路径下面去查询)

x = range(0, 120)
y = [random.randint(20, 35) for i in range(120)]
print(y)
# 设置图片的大小
plt.figure(figsize=(20, 8), dpi=80)

# plt.plot(x, y)
# plt.show()
# 这里发现x轴不是按照分钟进行的，而是按照数字从0到120开始的

# 2.进行改进
# 调整x轴的刻度
# _x = x  # 首先将x的值传递给_x 其实就是1-119
# _xtick_label = ["hello,{}".format(i) for i in _x]  # 这里打印出来的是从1-119的hello,{}
# plt.xticks(_x, _xtick_label) # 将 x 与 _xtick_label 一一进行对应
# plt.plot(x, y)
# plt.show()
# 这里发现 太密集，要进行取步长的操作，让其变得稍微稀疏一些。

# 3.进行稀疏操作，取步长
# _x = list(x)[::10]
# # 取步长的操作，首先强制转换成一个列表，然后在取10这个步长
# # 注意：这个_x 要与前后相互对应
# _xtick_label = ["hello,{}".format(i) for i in _x]
# plt.xticks(_x, _xtick_label)
# plt.plot(x, y)
# plt.show()

# 4.开始进行10-11点的编写（根据上面的例子）
# 取步长的操作，首先强制转换成一个列表，然后在取10这个步长
# 注意：这个_x 要与前后相互对应
_xtick_label = ["10点{}分".format(i) for i in range(1, 60)]
_xtick_label += ["11点{}分".format(i) for i in range(1, 60)]
plt.xticks(list(x)[::3], _xtick_label[::3], rotation=45)
# plt.xticks(list(x)[::3], _xtick_label[::3], rotation=270)  # 如果是270的话那么是逆时针旋转90度，此时10会转到最上面去
# 一步到位，取步长为3，数字和字符串一一对应，数据的长度一样子
"""
x = range(0, 120,3)
这是另一种表示步长的方法，直接在定义里面进行表示。其中3表示的步长
"""
# rotation 是旋转的角度 为90度。可以将文字立起来
plt.plot(x, y)
# plt.show()
# 这里发现：上述操作之后，xx点xx分 文字这里并不会显示，下一步的操作是将文字添加上去

# 5.紧接上文，解决中文不显示的问题
"""
注意：这里就是不显示中文的，因为 matplotlib 就是不显示中文的
"""
# 详细的信息参见上文

# 6.添加描述信息
plt.xlabel("时间")
plt.ylabel("温度 单位(℃)")
plt.title("10点到12点每分钟的温度变化情况")

plt.show()
