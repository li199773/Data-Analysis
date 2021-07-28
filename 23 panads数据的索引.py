"""
复合索引的介绍:
"""
import pandas as pd
import numpy as np

directory = pd.read_csv("./directory.csv")
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

grouped1 = directory[["Brand"]].groupby(by=[directory["Country"], directory["State/Province"]]).count()
print(grouped1)
print("*" * 100)

# 复合索引
# 索引的方法和属性
print(grouped1.index)

df1 = pd.DataFrame(np.arange(8).reshape(2, 4), index=["A", "B"], columns=list("abcd"), dtype="float")
print(df1)
df1.loc["A", "a"] = 100
df1.iloc[0, 1:] = 1
df1.iloc[1, :] = 1
print(df1, type(df1))
print("/" * 100)

print(df1.index)
# 输出Index(['A', 'B'], dtype='object')
# 更改原来的索引
df1.index = ["a", "b"]
print(df1)
# 索引的数量必须要跟之前的数量一样子才可以
print(df1.index)

# reindex操作：
print(df1)
print(df1.reindex(["a", "f"]))
# a那一行全部为原来的数值，f那一行原来的数组没有，现在输出为nan

# unique唯一的操作
print(df1["a"].unique())
# 输出为100 1 两个值 因为这两个值不一样子
print(df1["b"].unique())
# 输出为1个值，因为这两个的值都是一样子的

# 复合索引
a = pd.DataFrame({'a': range(7), 'b': range(7, 0, -1), 'c': ['one', 'one', 'one', 'two', 'two', 'two', 'two'], 'd': list("hjklmno")})
print(a)
print("/" * 100)
b = a.set_index(["c", "d"])
print(b)

c = b["a"]
print(c, type(c))  # 是一个<class 'pandas.core.series.Series'>
# 复合索引下进行取索引下面的值
# 取one j 的值：
print("0" * 100)
print(c["one"]["k"])

d = a.set_index(["d", "c"])["a"]
print(d)
# 对d取a这一列
print("/" * 100)

# 取one对应的数据
d1 = a.set_index(["c", "d"])["a"]
print(d1["one"]["h"])
print(d1["one"]["j"])
print("/" * 100)

# 太繁琐
# 进行交换2者的索引值
print(d.swaplevel())  # 交换索引之后cd位置变换
# 在进行取one即可
e = d.swaplevel()["one"]
print(e)
print("*" * 100)

# 有两个值怎么进行取值
# 对b来说的话取one j的值的话：
print(b)
print(b.loc["one"].loc["k"])
# 输出为a 2 b 5
# 类型为DataFrame进行取值的话要加上loc进行取值
# 方法二：交换索引
f = b.swaplevel()
print(f)
print(f.loc["k"])
