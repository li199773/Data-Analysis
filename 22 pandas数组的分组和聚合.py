"""
目标分析：有一组全球星巴克店铺的统计数据，如果想知道美国星巴克的数量狂和中国的哪个多，或者我们想知道
中国每个省份星巴克的数量的情况，那么我们应该怎么办？
"""
import pandas as pd
import numpy as np

directory = pd.read_csv("./directory.csv")

# 显示所有的行和列的详细信息，不会有省略号
pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)

print(directory.head(1))
print(directory.info())

# 进行分组:按照国家进行分组
grouped = directory.groupby(by="Country")
print(grouped)
# 输出为<pandas.core.groupby.generic.DataFrameGroupBy object at 0x00000205FEDF65E0>

# 进行遍历
# for i, j in grouped:
#     print(i)
#     print("*" * 100)
#     print(j, type(j))
#     print("-" * 100)

# 进行统计个数
print(grouped.count())
print("*" * 100)
# 也可以对一列进行统计个数
print(grouped["Brand"].count())
print("-" * 100)

# 求中国与美国的数量
country_Brand = grouped["Brand"].count()
print(country_Brand["US"])
print(country_Brand["CN"])
print("-" * 100)

# 统计中国每个省份店铺的数量
china_data = directory[directory["Country"] == "CN"]
print(china_data)
print("-" * 100)

grouped = china_data.groupby(by="State/Province").count()["Brand"]
print(grouped)
print("*" * 100)

# 数组按照多个条件进行分组,返回Series
grouped = directory["Brand"].groupby(by=[directory["Country"], directory["State/Province"]]).count()
print(grouped)
print(type(grouped))
# 输出为<class 'pandas.core.series.Series'>
# 是一个Series类型的数据 只有最后一列是数据，前两个为索引
# 因为按照了Country，State/Province这两列进行了分组，索引会有两列的索引值

# 数组按照多个条件进行分组,返回DataFrame
# 加上[]即可，就换成了DataFrame
grouped1 = directory[["Brand"]].groupby(by=[directory["Country"], directory["State/Province"]]).count()
grouped2 = directory.groupby(by=[directory["Country"], directory["State/Province"]]).count()
grouped3 = directory.groupby(by=[directory["Country"], directory["State/Province"]]).count()[["Brand"]]

print(grouped1, type(grouped1))
print("*" * 100)
print(grouped2, type(grouped2))
print("*" * 100)
print(grouped3, type(grouped3))
# 全为DataFrame类型的数据
print("-" * 100)

# 练习
df1 = pd.DataFrame(np.arange(8).reshape(2, 4), index=["A", "B"], columns=list("abcd"), dtype="float")
print(df1)
df1.loc["A", "a"] = 100
df1.iloc[0, 1:] = 1
df1.iloc[1, :] = 1
print(df1, type(df1))
print("/" * 100)

print(df1["c"])
print(type(df1["c"]))
# 输出为<class 'pandas.core.series.Series'>
print(type(df1[["c"]]))
# 输出为<class 'pandas.core.frame.DataFrame'>
# 因为有2个的[[]]

print(df1[["c"]])  # 跟上一个其实是一个的样子的
