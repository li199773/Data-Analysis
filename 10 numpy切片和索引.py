"""
在对应的数据集中进行取相应的行和列的操作，为下面做准备。
"""
import numpy as np

# 传入文件的路径即可
us_file_path = "./archive/USvideos.csv"

# 加载本地的数据
t1 = np.loadtxt(us_file_path, delimiter=",", dtype="int")
print(t1)
print("*" * 20)

# 取1行的操作：[]就是取行的意思
print(t1[1])
print("*" * 20)

# 取连续多行的操作：: 即可
print(t1[1:])
print("*" * 20)

# 取不行连续的多行的操作:[[]] 里面两个[]才可以
print(t1[[0, 1, 2]])
print("*" * 20)

# 取列的操作：不管行列通用的方法,[行,列]即可
# 假如是取行的话
print(t1[1, :])
print(t1[[0, 2], :])
# 假如是取列的话
print(t1[:, 1])
print(t1[:, [0, 2]])
print(t1[:, 1:])  # 取连续的多列
print("*" * 20)

# 取多行和多列，取第三行，第四列的值
print(t1[2, 3])
print(type(t1[2, 3]))  # <class 'numpy.int32'> 并不是我们常见到的int等等的类型

# 取第3行到第5行，第2列到第4列的数据:不需要再加入括号
# 要与,进行区分，[,]是取第x个的意思
# 因为要取第x行到第x行的话，最后数字要自加一，因为取不到。
print(t1[2:5, 1:4])
print("*" * 20)

# 了解一下不常使用
# 取多个不相邻的点
# 这里取到的是 [0,0],[2,1] 分别是第1行的第1列，第3行的第2列
print(t1[[0, 2], [0, 1]])
print("*" * 20)

# 更多的索引操作
# 检索所有小于10的数字
t2 = np.arange(24).reshape(4, 6)
print(t2)
print(t2 < 10)  # 会变成布尔类型的值

t2[t2 < 10] = 3
print(t2)
# 相比较
print(t2 > 20)
print(t2[t2 > 20])
print("*" * 20)

# where的用法
# 要是使用普通的话就要写2行,where的话直接去写就可以
print(t2)
print(np.where(t2 > 10, 100, 300))  # 在t2中，要是大于10情况下为100，否则为300

# 剪枝的操作:clip(裁剪)
print(t2.clip(10, 15))
# 在t2里面把小于10的替换成10,大于15的替换成15
print("*" * 20)

# nan的操作
print(t2)
# t2[3, 3] = np.nan
# 输出为：cannot convert float NaN to integer
# 因为之前为int的类型,不能将nan赋值给他,nan为浮点的类型
t2 = t2.astype(float)  # 转换成浮点的类型
t2[3, 3] = np.nan
print(t2)
