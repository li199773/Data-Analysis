# 从本节开始介绍`python`中`numpy`的一些主要的用法
## 07 `numpy`创建数组
### `numpy`:一个在`Python`中做科学计算的基础库，重在数值计算，也是大部分`Python`科学计算的基础库，多用于在大型，多维数组上执行数值运算。
### 相关操作：
#### 1.使用`numpy`生成数组的几种方法
        t1 = np.array([1, 2, 3])
        t2 = np.array(range(10))
        t3 = np.arange(10) # 速度是最快的
#### 2.`numpy`数组的类型：`int` `float` `bool`等类型
## 08 `numpy`数组的形状和计算
### 相关介绍：本节主要介绍了数组的创建，数组的修改`reshape`操作，数组的简单计算`+-*/`的操作，广播原则。
### 相关操作：
#### 1.修改数组：reshape
        t5 = np.arange(24).reshape(2, 3, 4)  # 2代表的是块，3行4列的意思
        print(t5)
#### 2.广播机制：如果两个数组的后缘维度，即从末尾开始算起的维度的轴长度相符或者其中一方的长度为1，即认为他们是广播兼容的。广播会在缺失和（或）长度为1的维度上进行计算。
        print(t6 + 2)  #数组全部加2，在原有的基础上进行自加2
        print(t6 + t9)
        print(t6 * t9)  # 道理是一样子的 都是对应位置进行加减乘除的运算即可
        # 必须要行或者是列要一致才可以，不然会进行报错。
## 09 `numpy`读取本地数据
### 相关介绍：我们一般不会使用`numpy`这个方法进行数据的读取，因为在后续的`pandas`里面会有更好的方法进行文件数据的读取。
### 相关操作：
#### 1.格式介绍：
        np.loadtxt(frame.dtype = np.load,delimiter =None,skiprows = 0,uncols = None,unpack = False)
           # frame:文件，字符串产生器
           # dtype: 数据的类型
           # delimiter:分割字符串，默认是任何空格，改为逗号
           # skiprows：跳过x行，一般跳过第一行表头
           # uncols：读取指定的列，索引，元祖类型
           # unpack：Ture :转置的效果，行变成列，列变成行
#### 传入文件路径：
        GB_file_path = "./archive/GBvideos.csv"
#### 2.加载本地的数据：一般情况下使用下面的参数即可。
        t1 = np.loadtxt(GB_file_path, delimiter=",", dtype="int", unpack=True)
#### 3.转置方法的介绍：`transpose`，`T` 等等
        print(t3.transpose())
        print(t3.T)
## 10 `numpy`切片和索引
### 相关介绍：本节主要介绍了使用`loadtxt`加载本地的数据，取数组行列的操作，检索数组的操作，剪枝`clip`的操作，`nan`的操作。
### 相关操作：
#### 1.加载本地数据：
        # 传入文件的路径
        us_file_path = "./archive/USvideos.csv"
        # 加载本地的数据
        t1 = np.loadtxt(us_file_path, delimiter=",", dtype="int")
#### 2.数组取行列的操作：
        # 取连续多行的操作：: 即可
        print(t1[1:])
        # 取不行连续的多行的操作:[[]] 里面两个[]才可以
        print(t1[[0, 1, 2]])
        print(t1[:, 1:])  # 取连续的多列
#### 3.剪枝`clip`的操作：
        print(t2.clip(10, 15))
        # 在t2里面把小于10的替换成10,大于15的替换成15
#### 4.`nan`的操作：
        t2[3, 3] = np.nan
        # 输出为：cannot convert float NaN to integer
## 11 `numpy`数组的拼接
### 相关介绍：本节主要介绍数组的拼接，数组的交换，创建一个全为0，1的数组，`random`随机取数的操作
### 相关操作：
#### 1.数组的拼接：`vstack`竖直拼接，`hstack`水平拼接
        np.vstack # 竖直拼接
        np.hstack # 水平拼接
#### 2.创建数组:
        np.zeros() # 创建全为0的数组
        np.ones() # 创建全为1的数组
        np.eye() # 创建对角线全为1的数组
#### 3.`random`随机取数的一些用法：用的最多的是`randint`的用法：在一定的数字的范围之内进行取整数。
        np.random.randint(10, 20, (4, 4)) # 在10-20之间随机进行取数字，成为4行4列的数组
        但是每次出现的数字都是随机的，并不是一样子，可以使用seed的操作：
        # 随机种子:跟上次的数字是一样子的。
        np.random.seed(10)
## 11 `numpy`中youtub练习
### 相关介绍：寻找重要的相关数据点即可，少数的点可以进行删除或者省略。
### 相关操作：
#### 1.直方图：设置组距，寻找最大值，最小值，公式计算得到组数。
        d = 50
        # 最大值-最小值，再去除以组距然后取整
        bin_nums = (t_us_comment.max() - t_us_comment.min()) // d
#### 2.二者之间的关系使用散点图即可`scatter`。
#### 3.取x,y轴的数据：
        t_uk_like = t_uk[:, 1]
        t_uk_comment = t_uk[:, -1]
#### 4.绘制图形：
        plt.scatter(t_uk_like, t_uk_comment)
