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
## 15 pandas的DataFrame的创建
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
