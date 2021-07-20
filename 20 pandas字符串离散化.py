"""
目标分析：对于一组电影的数据，希望统计出电影分类(Genre)的情况，如何进行出路数据？
思路：重新构造一个全为0的数组，列名为分类，如果某一条数据中分类出现过，就让0变为1
    先将所有的电影的分类找到，然后某一个电影属于这个分类的话就将0改为1即可
"""
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import matplotlib

IMDB_Movie_Data = pd.read_csv("./IMDB-Movie-Data.csv")
# print(IMDB_Movie_Data.info())

# 显示所有的行和列的详细信息，不会有省略号
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
# print(IMDB_Movie_Data["Genre"])

# 统计分类的列表
# 以,号进行分割
temp_list = IMDB_Movie_Data["Genre"].str.split(",").tolist()
# print(temp_list)  # 输出后为一个大链表，里面嵌套着一个一个的小链表
# [[],[],[]....]

# 展开链表:链表嵌套链表使用双重循环，进行输出
genre_list = list(set([i for j in temp_list for i in j]))
print(genre_list)

# 构造全为0的数组
zero_IMDB_Movie_Data = pd.DataFrame(np.zeros((IMDB_Movie_Data.shape[0], len(genre_list))), columns=genre_list)
# columns=genre_list 表示列的名字
print(zero_IMDB_Movie_Data)

# 给每个电影出现的位置继续赋值1
# 进行遍历所有的行
for i in range(IMDB_Movie_Data.shape[0]):
    # temp_list[i] 首先输出的是每一行的数据
    # 进行赋值为1，loc[行数,列数] temp_list[i] 出现的分类的列数
    # zero_IMDB_Movie_Data.loc[i, ['Mystery', 'Animation']] 下面的跟这个是一样子的
    zero_IMDB_Movie_Data.loc[i, temp_list[i]] = 1

# 输出进行比较
print(IMDB_Movie_Data["Genre"].head(3))
print(zero_IMDB_Movie_Data.head(3))

# 统计每个分类的电影的数量和
genre_count = zero_IMDB_Movie_Data.sum(axis=0)
print(genre_count)

# 对统计出来的电影进行排序
genre_count = genre_count.sort_values()
print(genre_count)

# 进行画图
# 设置图片的大小
plt.figure(figsize=(20, 8), dpi=80)

# 画条形图
_x = genre_count.index
_y = genre_count.values

# 添加描述信息
matplotlib.rc("font", family=' DengXian')  # 设置一下中文字体
plt.xlabel("电影分类")
plt.ylabel("电影的数量")
plt.title("电影分类与数量的情况分析")
plt.grid()

# 画图
plt.bar(_x, _y)
plt.show()
