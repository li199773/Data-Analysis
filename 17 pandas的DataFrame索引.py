import pandas as pd
import numpy as np

# 即想取很多行也想取很多列：主要有2种方法loc与iloc
# loc:通过 标签 索引行数据
# iloc：通过 位置 获取行数据

t1 = pd.DataFrame(np.arange(12).reshape(3, 4), index=list("abc"), columns=list("wxyz"))
print(t1)

# 通过标签进行定位数组中的元素
print(t1.loc["a", "y"])
print(t1.loc["a"])  # 取整行
print(t1.loc["a":])  # 取整行

# 查看数据的类型
print(type(t1.loc["a", "y"]))  # <class 'numpy.int32'>
print("*" * 100)

# 查看多行：
print(t1.loc[["a", "b"], :])  # 整体的格式跟之前numpy的格式差不多
# 都是进行取行跟列 [[行],[列]]
print("-" * 100)

# iloc的操作
# 取行
print(t1.iloc[2])
# 取列
print(t1.iloc[:, 2])
# 取多列
print(t1.iloc[:, [2, 1]])  # 这样子第3列就在第2列的前面了
print("/" * 100)

print(t1.iloc[1:, :2])
t1.iloc[1:, :2] = 30  # 可以进行赋值的操作
print(t1)
print("*" * 100)

# 缺失数据的处理：
t1.iloc[1:, :2] = np.nan
print(t1)
t2 = pd.isnull(t1)
print(t2)  # 可以找到是不是为nan的
print("*" * 100)

t3 = t1[pd.notnull(t1["w"])]
print(t3)

# nan操作：删除
t4 = t1.dropna(axis=0)
print(t4)  # 删除含有nan的行 也包含很多的参数
# any 操作:只要这一行含有nan的话就会把它进行删除、
t5 = t1.dropna(axis=0, how="any")
print(t5)
# all 操作:保证这一行全部要含有nan的话就会把它进行删除、
t6 = t1.dropna(axis=0, how="all")
print(t6)  # 输出并没有变化，跟原来的数组是一样子的.
print("*" * 100)

# inpalce 原地的替换
# 2种的表达意思：
t7 = t1.dropna(axis=0, how="any")
print(t7)
# 原地的替换
# t1.dropna(axis=0, how="any", inplace=True)
# print(t1)  # 已经把原来的t1替换完成
print(t1)
print("*" * 100)

# 使用相关的值进行填充nan
t8 = t1.fillna(0)  # 把原来的nan进行填充成0
print(t8)  # 一般情况下不会这样子进行传参数
# 一般情况使用均值进行填充即可
print(t1.mean())
print(t1.fillna(t1.mean()))
print("*" * 100)
# 对指定的一列进行填充:
print(t1["w"].fillna(t1["w"].mean()))  # 只对w这一列进行更改均值
t1["w"] = t1["w"].fillna(t1["w"].mean())
print(t1)  # 让t1的w这一列进行改变

# panads求均值的操作：
t1.iloc[1, 1] = 21
print(t1)
t8 = t1["x"].mean()
print(t8)  # pandas在求均值方面要比numpy要好,有nan求均值不会变成nan，会正常的求知
