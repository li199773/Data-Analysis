"""
项目需求：
查看哪一种的名字被使用的次数最多？
"""
import pandas as pd

dog_names = pd.read_csv("./archive/dogNames2.csv")
# 查看相关的描述信息
# print(dog_names.head())
# print(dog_names.info())

# 对数据进行排序
# sort_values 对其中的一列进行排序，by= 指定其中的一列排序，ascending=False降序排序
dog_names = dog_names.sort_values(by="Count_AnimalName", ascending=False)
print(dog_names.head(5))
# 只能看到前5行的信息，想查看5-10行的信息必须要进行切片和索引的操作

# 取前20个：
print(dog_names[:20])
print(type(dog_names))  # 是一个DataFrame类型的数据
print("*" * 100)

# 取Row_Labels这一列
print(dog_names["Row_Labels"])
print(dog_names[:10]["Row_Labels"])  # 取前10行取Row_Labels这一列
print("*" * 100)

# print(dog_names[800 < dog_names["Count_AnimalName"] < 1000])
# 在DataFrame中不可以进行直接的编写，要分开进行编写
print(dog_names[(800 < dog_names["Count_AnimalName"]) & (1000 > dog_names["Count_AnimalName"])])

# 取使用次数大于700并且名字的字符串长度大于4的狗的名字
print(dog_names[(dog_names["Row_Labels"].str.len() > 4) & (dog_names["Count_AnimalName"] > 700)])

# 不同条件之前需要使用括号括起来即可
# 使用次数比较多的：
# 分割split：().str.split("/") 对其/进行分割
