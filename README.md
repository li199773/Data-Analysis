# Data-Analysis
## 本章节开始开始进行数据的分析。其中包括`matplotlib`
## 01 matplotlib基础绘图和调整x轴
### 相关介绍：
#### 1.导入 `matplotlib` 模块
        from matplotlib import pyplot as plt
#### 2.通常要通过`figsize` 设置图片的大小
#### 3.开始绘图
        plt.plot(x, y)
#### 注：1.我们可以使用 `_xtick_label` `_ytick_label` 对x轴和y轴进行设置，如果不进行设置的话，通过默认输出的值达不到我们的需求。
        _xtick_label =
        _ytick_label = 
        plt.xticks(_xtick_label)
        plt.yticks(_ytick_label)
## 02.01 `matplotlib` 绘制 0-12 的气温图
### 目标分析：构建一个2小时的气温图。
### 相关介绍：
#### 1.`matplotlib` 不显示中文的问题：需要导入包即可，相关的字体见下一节介绍，中文字体不是很多。
        import matplotlib
        matplotlib.rc("font", family=' DengXian')
#### 2.画出来的图片需要一步一步的去细致的调节。
#### 3.x轴的调节（y轴也是同理）
        _xtick_label = ["10点{}分".format(i) for i in range(1, 60)]
#### 4.进行稀疏操作，取步长
        plt.xticks(list(x)[::3], _xtick_label[::3], rotation=45) # 注意前后要一致，因为要将_xtick_label传递给x,rotation是旋转角度的意思
#### 5.添加描述信息
        plt.xlabel("时间") # x轴的描述信息
        plt.ylabel("温度 单位(℃)") y轴的描述信息
        plt.title("10点到12点每分钟的温度变化情况") 标题的描述信息
## 02.02 查询 `matplotlib` 所有的字体
### 本节主要是对应上一节，使用相关代码查询机器自带的字体。（也可以从网上下载字体嵌入到Pycharm中）
## 03 `matplotlib` 绘制两个折线图
### 目标分析：在一张图片里面绘制2个折线图。
### 相关介绍：
#### 1.跟在一张图片上面绘制1个折线图的思想是一样子的，只不过需要定义2个 y 轴的数据点。
#### 2.为了使两条线看得更直观一些，在后面加上参数。
        plt.plot(x, y_1, label="自己", color="orange", linestyle=':')
        plt.plot(x, y_2, label="同桌", color="red", linestyle='--')  # 相关的颜色还可以在网上进行查找16进制的代码
#### 3.绘制一个网格可以使观看者看得更清晰一点。
        plt.grid(alpha=1)  # alpha 是透明度的意思 从0-1进行输出 1是最深，默认为最深的颜色，0是最浅的颜色
#### 4.添加图例(见自己和同桌那一栏 添加参数) 右上角会出现一个小的图例 默认在右上角进行显示 也可以在是左上角。
        plt.legend(loc="upper left")  # 在左上角显示
## 04 `matplotlib` 绘制散点图
### 目标介绍：根据数据在一张图片里面绘制出2个散点图。
### 相关介绍：
#### 1.主要的思想其实跟在一张图片上绘制一个散点图是一样子的，只不过需要建立2个 y 轴的数据。
#### 2.第二数据的x轴需要像右侧偏移。
        x_10 = range(51, 82)
        _xtick_label += ["10月{}日".format(i - 50) for i in x_10]
#### 3.使用 `scatter` 来绘制散点图
        plt.scatter(x_3, y_3, label="3月份")
        plt.scatter(x_10, y_10, label="10月份")
