"""
numpy读取本地文件的数据：
    我们一般不会使用numpy这个方法进行数据的读取，因为在后续的pandas里面会有更好的方法进行文件数据的读取
    我们一般会进行csv文件数据的读取
    相关的格式：
    np.loadtxt(frame.dtype = np.load,delimiter =None,skiprows = 0,uncols = None,unpack = False)
    frame:文件，字符串产生器
    dtype: 数据的类型
    delimiter:分割字符串，默认是任何空格，改为逗号
    skiprows：跳过x行，一般跳过第一行表头
    uncols：读取指定的列，索引，元祖类型
    unpack：Ture :转置的效果，行变成列，列变成行
"""
import numpy as np

# 传入文件的路径即可
GB_file_path = "./archive/GBvideos.csv"
us_file_path = "./archive/USvideos.csv"

# 加载本地的数据
# delimiter以逗号进行分割
t1 = np.loadtxt(GB_file_path, delimiter=",", dtype="int", unpack=True)
t2 = np.loadtxt(GB_file_path, delimiter=",", dtype="int")
print(t1)  # 出现的科学计数法,数据的类型
# 打印出来进行对照检查,转置的效果：行变成列，列变成行。
print("**" * 100)
print(t2)
print("/" * 20)

# 2.在程序中进行转置的方式很多：
t3 = np.arange(24).reshape(4, 6)
print(t3)
# 01.使用transpose进行转置,transpose在中文里面就是转置的意思
print(t3.transpose())
print("." * 10)
# 02.使用T就可以，在数学中T就是转置的符号
print(t3.T)
print("," * 10)
# 03.对数轴进行交换的操作,swapaxes交换数轴的意思，默认情况下是swapaxes(0,1)
print(t3.swapaxes(1, 0))
