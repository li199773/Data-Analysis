import numpy as np

t1 = np.arange(0, 12).reshape(2, 6)
t2 = np.arange(12, 24).reshape(2, 6)
print(t1)
print(t2)

# 数组的拼接：
# 1.竖直拼接：
t3 = np.vstack((t1, t2))
print(t3)
# 2.水平切割：
t4 = np.hstack((t1, t2))
print(t4)
# 涉及到顺序的问题
print("*" * 100)

# 数组的交换：想把数组的第一行与第二行进行交换或者第一列与第二列进行交换
t5 = np.arange(24).reshape(4, 6)
print(t5)
t5[[1, 2], :] = t5[[2, 1], :]  # 第2行与第3行交换
print(t5)
t5[:, [1, 2]] = t5[:, [2, 1]]  # 第2行与第3行交换
print(t5)
print("-" * 100)

# 创建一个全为0 1 的数组：
t10 = np.zeros((5, 5))
print(t10)
t11 = np.ones((5, 5))
print(t11)
# 创建一个对角线全为1的数字:eye
t12 = np.eye(10)
print(t12)

# 练习：拼接两个国家的数据，然后在一起进行分析：

# 进行加载两个国家的数据：
GB_video_data = "./archive/GBvideos.csv"
US_video_data = "./archive/USvideos.csv"

t6 = np.loadtxt(GB_video_data, delimiter=",", dtype="int")
t7 = np.loadtxt(US_video_data, delimiter=",", dtype="int")

# 添加国家的信息：
# 构造一个根据t6的行数列数，1列的全为0的数组
zeros_data = np.zeros((t6.shape[0], 1)).astype(int)  # 后面的数字表示构造的列数 2代表构造2列
# 构造一个全为1的一列
ones_data = np.ones((t7.shape[0], 1)).astype(int)
# 一样子对其进行数组类型的转换，变成int类型的数据

print(zeros_data)
print(ones_data)

# 进行水平的拼接
t8 = np.hstack((zeros_data, t6))
t9 = np.hstack((ones_data, t7))
print(t8)
print(t9)

# 进行竖直的拼接：0代表的是GB国家，1代表的是UK
findly_data = np.vstack((t8, t9))
print(findly_data)

# 获取最大值的位置
t13 = np.eye(4)
print(t13)
t14 = np.argmax(t13, axis=0)
print(t14)  # 分别第一行第第一列，第二行第二列最大，依次往后进行输出最大的数字

t13[t13 == 1] = -1
print(t13)

t15 = np.argmin(t13, axis=1)
print(t15)

# random随机取数的一些用法
# 用的最多的是randint的用法：在一定的数字的范围之内进行取整数
t16 = np.random.randint(10, 20, (4, 4))
print(t16)
# 但是每次出现的数字都是随机的，并不是一样子，可以使用seed的操作：
# 随机种子:跟上次的数字是一样子的。
np.random.seed(10)
