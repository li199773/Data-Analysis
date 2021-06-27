# 从本节开始介绍`python`中`pandas`的一些主要的用法
## 13 `pandas`的`series`了解
### 相关介绍：`pandas`处理的是非数值类型的数据，像文字，字母信息等等，`numpy`只能处理数值型的数据。在处理数据上`pandas`比`numpy`更为强大。
### 相关操作：
#### 1.导入`pandas`相关的包
        import pandas as pd
#### 2.`Serier`介绍：表示的是带标签的数组，输出的第一列为索引，第二列为输入的数字。
        t1 = pd.Series([1, 2, 2, 2, 2, 2, 2, 2, 9])
#### 3.索引的一些操作：
        len(t3.index)
        # 进行获取相关的长度
        print(t3["age"])
        # 通过索引进行取值
        print(t3[2])
        # 通过行数进行取值
        print(t3[:3])
        # 取前3行
#### 4.`value`的一些操作：
        t3.values  # 输出的是值
        # array(['xiaohong', 20, 10086], dtype=object)
        type(t3.values)
## 14 `pandas`读取外部数据
### 相关介绍：跟`numpy`差不多，传入相关的类型即可。
        dog_names = pd.read_csv("./archive/dogNames2.csv") # 文件所在的路径
        print(dog_names)
## 15 `pandas`的`DataFrame`的创建
### 相关操作：
#### 1.改变索引的编号：
        t2 = pd.DataFrame(np.arange(12).reshape(3, 4), index=list("abc"), columns=list("zxcv"))
#### 2.缺失数据的编写：
        t5 = [{"name": "xiaogang", "age": 20, "tel": 10086}, {"name": "xiaohong", "tel": 10010}, {"name": "xiaoli", "age": 30}]
#### 3.显示文件数据的前几行：`head`
        print(dog_names.head()) # 默认显示数据的前5行
#### 4.显示数据的详细信息：`info`
        print(dog_names.info())  # 会把列和行的信息更详细的展示出来。
## 16 `pandas`的`DataFrame`练习
### 练习需求：查看哪一种的名字被使用的次数最多？
### 数据集：dogNames2.csv
### 相关操作：
#### 1.对数据进行排序：
        # sort_values 对其中的一列进行排序，by= 指定其中的一列排序，ascending=False降序排序
        dog_names = dog_names.sort_values(by="Count_AnimalName", ascending=False)
#### 2.取某一列：
        print(dog_names["Row_Labels"]) 取Row_Labels这一列
#### 3.双重判断：
        print(dog_names[800 < dog_names["Count_AnimalName"] < 1000]) # 不能这么写
        # 分开进行以下的编写，使用 & 进行连接
        print(dog_names[(800 < dog_names["Count_AnimalName"]) & (1000 > dog_names["Count_AnimalName"])])
## 17 `pandas`的`DataFrame`索引
### 相关操作：
#### 1.取很多行也想取很多列：主要有2种方法`loc`与`iloc`
        # loc:通过 标签 索引行数据
        # iloc：通过 位置 获取行数据
        print(t1.loc["a"])  # 取整行
        print(t1.loc["a":])  # 取整行
#### 2.缺失数据的处理：
        t1.iloc[1:, :2] = np.nan
        t2 = pd.isnull(t1)
        print(t2)  # 可以找到是不是为nan的
#### 3.`nan`操作：删除
        # any 操作:只要这一行含有nan的话就会把它进行删除、
        t5 = t1.dropna(axis=0, how="any")
        # all 操作:保证这一行全部要含有nan的话就会把它进行删除、
        t6 = t1.dropna(axis=0, how="all")
#### 4.`inpalce` 原地的替换
