import pandas as pd
import numpy as np

IMDB_Movie_Data = pd.read_csv("./IMDB-Movie-Data.csv")
print(IMDB_Movie_Data.info())

# 显示完整列的信息
pd.set_option('display.max_columns', None)
print(IMDB_Movie_Data.head(1))

# 获取电影的平均评分
print(IMDB_Movie_Data["Rating"].mean())
# 获取导演的人数
# 方法一
print(len(set(IMDB_Movie_Data["Director"].tolist())))
# 方法二 unique() 唯一的意思
print(len(IMDB_Movie_Data["Director"].unique()))

# 获取演员的信息
temp_actors_list = IMDB_Movie_Data["Actors"].str.split(",").tolist()
# print(temp_actors_list)

# 获取演员的人数
# 2次循序即可
actors_list = [i for j in temp_actors_list for i in j]
actors_num = len(set(actors_list))
print(actors_num)


