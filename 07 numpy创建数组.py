"""
什么是numpy
一个在Python中做科学计算的基础库，重在数值计算，也是大部分Python科学计算的基础库，多用于在大型，多维数组上执行数值运算
"""
import numpy as np
import random

# 使用numpy生成数组，得到ndarray类型
t1 = np.array([1, 2, 3])
print(t1)
print(type(t1))
# 输出的是 ndarray类型 以后会经常见到这个

t2 = np.array(range(10))
print(t2)
t3 = np.arange(10)
print(t3)
# 这两个的输出形式是一致的，其实都是生成0-9的一个数组
# 其中最快的还是aragne 这个方法

t4 = np.arange(0, 11, 2)
t5 = np.arange(-10, 0)
print(t4)
# 输出的结果为[ 0  2  4  6  8 10]，在0-10之间每隔2个步长进行取一个值
print(t4.dtype)  # 存放数据的类型是什么意思
# 输出为：int32 32位的电脑输出的 64位电脑输出的是 int64
# 其他类型：
# int8,uint8 有符号无符号的8位整形
# float16 小数或者是半精度的浮点数
# complex64 分别用两个32位的浮点数的复数
print(t5.dtype)
print(t5)

# 也可以进行如下的定义：
t6 = np.array(range(1, 4), dtype=float)
print(t6)
print(t6.dtype)

# numpy的bool类型
t7 = np.array([1, 1, 1, 0, 0], dtype=bool)
print(t7)
print(t7.dtype)
# 调整数据的类型
t8 = t7.astype("int8")  # 对上面的数组类型进行调整为int8
print(t8)
print(t8.dtype)
print("*" * 10)
t9 = t7.astype("float")  # 对上面的数组类型进行调整为int8
print(t9)
print(t9.dtype)

# numpy 中的小数
t10 = np.array([random.random() for i in range(10)])
print(t10)
print(t10.dtype)
t11 = np.array([random.random() for i in range(1, 10)])
print(t11)
print(t11.dtype)

# 取小数的操作
t12 = np.round(t10, 2)  # 2代表的是进行2位小数
print(t12)
print("_" * 100)
# 不是在np里面取小数的操作
t13 = round(random.random(), 4)
print(t13)
print(round(random.random(), 4))

