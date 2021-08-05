# 从本节开始介绍`python`中`pandas`的一些主要的用法。
## 13 `pandas`的`series`了解
### 相关介绍：`pandas`处理的是非数值类型的数据，像文字，字母信息等等，`numpy`只能处理数值型的数据。在处理数据上`pandas`比`numpy`更为强大。
### 相关操作：
#### 1.导入`pandas`相关的包
        import pandas as pd
#### 2.`Serier`介绍：表示的是带标签的数组，输出的第一列为索引，第二列为输入的数字
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
## 14 `pandas`读取外部数据。
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
        # t1.dropna(axis=0, how="any", inplace=True)
        # 已经把原来的t1替换完成
#### 5.使用相关的值进行填充`nan`
## 18 `pandas`处理电影的直方图
### 数据集：IMDB_Movie_Data
### 目标需求：对于这一组的电影数据，如果我们像`rating`，`runtime`的分布情况，应该如何呈现数据？
### 相关操作：
### `runtime`的分布情况
#### 1.选择图形，直方图
#### 2.计算组数
        num_bin = (max_runtime - min_runtime) // 5
## 2.`rating`分布情况 0-10 打分
### 相关操作：
#### 计算组数：
        print(max_Rating, min_Rating)
        num_bin_list = [1.6]
        num_bin_list = [1.6]+[0.5]*11
## 19 `pandas`常用的统计方法
### 数据集：IMDB-Movie-Data
### 本节主要讲解常用的一些统计方法
#### 1.显示完成列信息
        pd.set_option('display.max_columns', None)
#### 2.获取电影导演的人数（因为有的导演拍摄不止一部影片，所以会有重合的，目标是进行去重，取唯一）
        print(len(IMDB_Movie_Data["Director"].unique()))
#### 3.获取演员的信息，按照`,`进行分割，并且将数组转换成列表
        DB_Movie_Data["Actors"].str.split(",").tolist()
## 20 `pandas`字符串离散化
### 项目需求：对于一组电影的数据，希望统计出电影分类(Genre)的情况，如何进行出路数据？
### 思路：重新构造一个全为0的数组，列名为分类，如果某一条数据中分类出现过，就让0变为1先将所有的电影的分类找到，然后某一个电影属于这个分类的话就将0改为1即可
### 相关重要操作：
#### 1.# 统计分类的列表，以,号进行分割
        temp_list = IMDB_Movie_Data["Genre"].str.split(",").tolist()
        # print(temp_list)  # 输出后为一个大链表，里面嵌套着一个一个的小链表，如 [[],[],[]....]
#### 2.展开链表:链表嵌套链表使用双重循环，进行输出（一般都要进行以下操作）
        genre_list = list(set([i for j in temp_list for i in j]))
#### 3.给每个电影出现的位置继续赋值1
#### 4.统计每个分类的电影的数量和
        genre_count = zero_IMDB_Movie_Data.sum(axis=0)
#### 5.画图
## 21 `panads`数组的合并
### 相关操作：
#### 1.join合并：主要是看以哪一个为主
#### 2.merge合并：默认情况下取的是并集
## 22 `pandas`数组的分组和聚合
### 目标需求：有一组全球星巴克店铺的统计数据，如果想知道美国星巴克的数量和中国的哪个多，或者我们想知道中国每个省份星巴克的数量的情况，那么我们应该怎么办？
### 数据集：directory.csv
### 相关操作：
#### 1.分类：按照列索引为国家进行分组
        rouped = directory.groupby(by="Country")
#### 2.统计中国每个省的店铺的数量
        china_data = directory[directory["Country"] == "CN"] # 先提取出来国家为中国的所有的信息
        grouped = china_data.groupby(by="State/Province").count()["Brand"] # 对提取出来的国家为中国在进行对省市进行分类，并且统计数量
#### 3.使用`matplotlib`进行绘图即可
## 23 `panads`数据的索引
### 数据集：directory.csv
### 相关介绍：
#### 1.更改原来的索引
        df1.index = ["a", "b"] # 要保证索引的数量必须要跟之前一样子才可以
#### 2.`unique`唯一的操作
        print(df1["a"].unique()) # 取唯一的操作，因为有些输出之后会有重复，重复的只会输出一次
#### 3.交换两列的索引值
        d.swaplevel()
## 24 `panads`数据的索引项目练习
### 目标需求:
#### 1.使用matplotlib呈现出店铺总数排名前10的国家
#### 2.使用matplotlib呈现出中国每个城市店铺的数量
#### 数据集：directory.csv
### 相关操作：
#### 1. 数据的处理：按照城市进行分组：默认情况下是升序，改成降序即可
        .sort_values(ascending=False) # 降序排列
#### 2.添加相关的描述信息
#### 3.绘图
## 25 `panads`数据的索引项目练习
### 项目需求:现在我们有全球排名前10000本书的数据，统计一下：
#### 1.不同年份书的数量
#### 2.不同年份书的平均评分情况
#### 数据集：books.csv
### 相关操作：
#### 1.数据预处理：数据里面有缺失不能直接进行使用dropnan，会把其他为nan都给删除
        books_data_notnull = books_data[pd.notnull(books_data["original_publication_year"])] # 使用notnull进行数据的提取
#### 2.绘图，强制转换成整数，不要小数，并且按照10进行取步长
        plt.xticks(list(range(len(average_x)))[::10], average_x[::10].astype(int), rotation=45)
## 26 `panads`时间序列练习
### 项目需求：
#### 1.统计出数据不同类型的紧急情况的次数
#### 2.统计出不同月份不同类型紧急电话的次数的变化情况
### 相关操作：
#### 1.对不同类型的紧急情况进行分组，然后转化成一个列表。
        temp_list = nine11_data["title"].str.split(":").tolist()
#### 2.进行降重，因为有很多重复的，重复的只需要去一次即可。
#### 3.时间序列的学习：
#### 3.1 虽然可以使用切割来获取年月的数据，有更为简单的处理方法：时间序列：
        t1 = pd.date_range(start="20210624", end="20210731", freq="D") # 按一天或者10天都可进行输出
##### 3.2 控制输出数据的个数：
        t3 = pd.date_range(start="20210624", freq="D", periods=10) # 不能与end进行连用
## 27 `panads`时间序列练习
### 目标需求：
#### 1.统计出911数据中不同月份电话的次数
#### 2.统计出911数据中心不同月份不同类型的电话的次数的变化情况
### 数据集：911.csv
### 相关操作：
#### 1.重采样的学习：
        t1 = pd.to_datetime(nine11_data["timeStamp"]) # to_datetime对timeStamp这一列进行获取时间序列
#### 2.统计出911数据中不同月份电话的次数
        count_by_month = nine11_data.resample("M").count()["title"]
#### 3.tolist()转换成一个列表
        temp_list = nine11_data["title"].str.split(":").tolist()  # 进行转化成一个列表
## 28 PM 2.5案列
### 项目需求：我们有北上广，深圳，和沈阳5个城市的空气质量数据源，请绘制出5个城市的PM2.5随时间的变化情况。
### 数据集：PM2.5文件夹（包含北京，广州等城市PM2.5的数据）
### 相关操作：
#### 1.按照天进行采样
        data_1 = Beijing["PM_US Post"].dropna() # 处理缺失的数据,删除缺失的数据,以 PM_US Post为基准
#### 2.数据量特别大的时候可以按照月进行重采样
#### 3.画图
