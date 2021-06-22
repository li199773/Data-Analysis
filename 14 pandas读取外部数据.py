import pandas as pd

# 跟numpy差不多，传入相关的类型即可

dog_names = pd.read_csv("./archive/dogNames2.csv")
print(dog_names)
# 第一列还是索引的类型
