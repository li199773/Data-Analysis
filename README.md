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
## 05.01 `matplotlib` 绘制条形图
### 项目需求：假设你获取到了2017年内地电影票房前20的电影和电影的票房数据，绘制一个适合该数据的图形进行可视化处理。
### 相关介绍：
### 1.条形图：数据是离散的采用条形图来绘制。
### 2.条形图：`bar`
        plt.bar(range(len(a)), b, width=0.3) # 首先先画一个图出来,将宽度绘制成0.3，默认情况下是1.
## 05.02 matplotlib绘制横条形图
### 目标介绍：紧接上文，对上面的代码进行升级改造。
### 相关操作：
#### 1.发现使用`rotation`旋转45度发现店也是显示不太完整，所以画出横条形图，即x y轴的数据进行调换即可。
#### 2.横条形图：barh
        plt.barh(range(len(a)), b, height=0.3, color="red") 
## 05.03 matplotlib绘制多次条形图
## 项目需求：假设知道了三天不同电影的票房记录，绘制一个更加直观的条形图来表示数据。实则是在一个条形图里面绘制不同的数据信息即可。
#### 1.根据x y轴的参数画出简单的图形。
#### 2.发现画出来的图形与x轴对应不上，需要进行相关参数的调节：
        bar_width = 0.2 # 将每个第二个第三个条形图都往右移动0.2个单位即可
        x_14 = list(range(len(a)))
        x_15 = [i + bar_width for i in x_14]
        x_16 = [i + bar_width * 2 for i in x_14]
### 3.设置x轴的刻度，让电影名字实现居中处理：
        plt.xticks(x_15, a)
## 06.01 matplotlib绘制直方图
### 项目需求：假设获取到了250部电影的时长在列表 a 中,希望统计出来电影的时长分布状况（比如时长为100分钟到120分钟的电影的数量，出现的频率等等信息，如何进行呈现）。
### 一般遇到这种数据量比较大的时候，尽量采用直方图进行呈现。
### 相关操作：
###
