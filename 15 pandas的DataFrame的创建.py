import pandas as pd
import numpy as np

t1 = pd.DataFrame(np.arange(12).reshape(3, 4))
print(t1)
# 会分别出现行索引和列索引
# 行索引：不同行，横向索引，叫index 0轴，axis=0
# 列索引：不同列，纵向索引，叫columns 1轴，axis=1

# 为其改变索引的编号
t2 = pd.DataFrame(np.arange(12).reshape(3, 4), index=list("abc"), columns=list("zxcv"))
print(t2)

# 取第二行到最后行 索引也会变化
t3 = t1[1:]
print(t3)

# DataFrame是series的一个容器
# 传入字典,使用DataFrame
t4 = {"name": ["xiaohong", "xiaogang"], "age": ["20", "30"], "tel": ["10086", "10010"]}
print(pd.DataFrame(t4))
print(type(pd.DataFrame(t4)))
# 输出为 <class 'pandas.core.frame.DataFrame'>
print("*" * 50)

# t5 = {"name": ["xiaohong"], "age": ["20", "30"], "tel": ["10086", "10010"]}
# print(pd.DataFrame(t5))
# 报错 缺失一个数据
# 可以进行以下编写
t5 = [{"name": "xiaogang", "age": 20, "tel": 10086}, {"name": "xiaohong", "tel": 10010}, {"name": "xiaoli", "age": 30}]
print(t5)
print(pd.DataFrame(t5))
# 缺失的数据会用nan进行填充
# print(t5.index())

# 数据的维度ndim
# t6 = t5.ndim

dog_names = pd.read_csv("./archive/dogNames2.csv")
print(dog_names)

# head显示前几行的意思
# 不写的话默认为前5行的意思
print(dog_names.head())
# 显示前一行
print(dog_names.head(1))
# tail显示的后几行
print(dog_names.tail(3))
print("-" * 100)

# 显示数据的详细信息
print(dog_names.info())  # 会把列和行的信息更详细的展示出来。
print(dog_names.describe()) # 只会显示出来int类型的相关值，均值，中位数，最小值等等
# 以后可能会经常使用来查看数据是否有缺失，进行查看.

