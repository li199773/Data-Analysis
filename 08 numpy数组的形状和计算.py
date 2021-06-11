import numpy as np

t1 = np.arange(12)
print(t1)
print(t1.shape)  # 输出后是一个元祖，比较特殊，只有一个数字在里面

t2 = np.array([[1, 2, 3], [4, 5, 6]])
print(t2)
print(t2.shape)
# shape 代表的是(列数，行数)
# t1代表的是一维数组，t2代表的是二维数组
# 有几个数字代表的是几维数组

t3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(t3)
print(t3.shape)
# t3是一个三维的数组
print("*" * 20)

# 进行数组的修改
t4 = np.arange(12)
print(t4)
print(t4.reshape(3, 4))  # 修改成3行4列的数组
# print(t4.reshape(3, 5))  # 会进行报错，因为不可能将12个数字变成3*5的数组的
print("." * 20)

t5 = np.arange(24).reshape(2, 3, 4)  # 2代表的是块，3行4列的意思
print(t5)

# 一般情况下转换成2维的即可
t6 = t5.reshape(4, 6)  # t5本身是不会进行改变的，会有一个 reture 的操作的
print(t6)
print(t6.shape)
# 进行转换成1维数组
print(t5.reshape(24, ))
print(t5.reshape(24, 1))  # 这样子的话就是24行1列的意思,与上面进行区分
print(t5.reshape(1, 24))  # 这个是2维的数组 因为里面有2个数字为2维的数组

# 一般的情况下不知道数据的个数时候如何进行取数组
t7 = t6.reshape((t6.shape[0] * t6.shape[1],))  # shape[0]行数,shape[1]列数
print(t7)
print("***" * 20)

# 对数组进行展开的处理
print(t6)
t8 = t6.flatten()  # flatten 有展开的意思 不需要传入行数和列数
print(t8)  # 转成了一维的数组

# 广播机制：加减乘除都可以
# 数组全部加2，在原有的基础上进行自加2
print(t6 + 2)
# print(t6 / 0)  # 会进行警告的操作：但是并不会报错，一样子进行计算，nan和inf
# nan：no a number 找不到一个数字，因为分子为0
# inf：无穷的意思 因为分母为0
t9 = np.arange(100, 124).reshape(4, 6)
print(t9)
print(t6 + t9)
print(t6 * t9)  # 道理是一样子的 都是对应位置进行加减乘除的运算即可

t10 = np.arange(0, 6)
print(t10)
print(t6 - t10)
t11 = np.arange(0, 4).reshape(4, 1)
print(t6 - t11)
# 必须要行或者是列要一致才可以，不然会进行报错。

"""
广播原则：
如果两个数组的后缘维度，即从末尾开始算起的维度的轴长度相符或者其中一方的长度为1，即认为他们是广播兼容的。
广播会在缺失和（或）长度为1的维度上进行计算。 
"""
