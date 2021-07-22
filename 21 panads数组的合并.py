import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.ones((2, 4)), columns=list("abcd"), index=["A", "B"])
df2 = pd.DataFrame(np.zeros((3, 3)), columns=list("xyz"), index=["A", "B", "C"])
print(df1)
print(df2)
print("*" * 50)

# join合并
print(df1.join(df2))  # 以df1为基准
print(df2.join(df1))  # 以df2为基准，df1没有第三行,输出为nan

# merge合并
df3 = pd.DataFrame(np.zeros((3, 3)), columns=list("fax"))
print(df3)
print(df1.merge(df3, on="a"))  # 输出Empty DataFrame
# 默认情况下取得是并集
df3.loc[1, "a"] = 2
df3.loc[0, "a"] = 1
df3.loc[2, "a"] = -1
print(df3)
print(df1.merge(df3, on="a"))
print("*" * 100)

df4 = pd.DataFrame(np.arange(9).reshape(3, 3), columns=list("fax"))
print(df4)
print(df1)
print(df1.merge(df4, on="a"))
# 对其进行重新的赋值
df1.loc["A", "a"] = 100
print(df1.merge(df4, on="a"))
print("*" * 100)

# 外连接
print(df1.merge(df4, how="outer"))

# 总结：
# join是按照行索引进行合并在一起
# merge是按照列索引进行合并在一起
