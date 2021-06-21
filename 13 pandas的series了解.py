"""
pandas处理的是非数值类型的数据，像文字，字母信息等等，numpy只能处理数值型的数据。
"""
import pandas as pd

# 1.Serier 表示的是带标签的数组，输出的第一列为索引，第二列为输入的数字
t1 = pd.Series([1, 2, 2, 2, 2, 2, 2, 2, 9])
print(t1)
print(type(t1))  # 带标签的数组

# 我们也可以进行自定义数组：
t2 = pd.Series([1, 2, 2, 2], index=list("abcd"))
print(t2)  # 原先的数组前面的索引1234变为abcd
print(type(t2))  # 输出的格式为int格式类型

# 也可以使用字典进行更改索引
temp_dict = {
    "name": "xiaohong",
    "age": 20,
    "tel": 10086
}
t3 = pd.Series(temp_dict)
print(t3)
# 前面的索引全部更改为name,age,tel

print(type(t3))
# 格式为object的格式 对象的形式

print(t3["age"])
# 通过索引进行取值

print(t3[2])
# 通过行数进行取值

print(t3[:3])
# 取前3行

print(t3[[0, 2]])
# 取不连续的2行 取第一行和第三行的数据

print(t3[["name", "age"]])
# 同样子取索引值也是可以的

# index索引的一些操作：
t3.index
for i in t3.index:
    print(i)
# 可以进行遍历进行取值

type(t3.index)
# <class '03 pandas.core.indexes.base.Index'> 类型的数据

len(t3.index)
# 也可以进行获取相关的长度

list(t3.index)
# 可以进行转换成列表的形式

list(t3.index)[:2]
# 进行取前两个的索引

# value的一些操作：
t3.values  # 输出的是值
# array(['xiaohong', 20, 10086], dtype=object)
type(t3.values)  # 输出的是<class 'numpy.ndarray'>
