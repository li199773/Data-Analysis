# 从本节开始介绍`python`中`pandas`的一些主要的用法
## 13 `pandas`的`series`了解
### 相关介绍：`pandas`处理的是非数值类型的数据，像文字，字母信息等等，`numpy`只能处理数值型的数据。在处理数据上`pandas`比`numpy`更为强大。
### 相关操作：
#### 1.导入`pandas`相关的包
        import pandas as pd
#### 2.`Serier`介绍：表示的是带标签的数组，输出的第一列为索引，第二列为输入的数字。
        t1 = pd.Series([1, 2, 2, 2, 2, 2, 2, 2, 9])
