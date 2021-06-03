# Data-Analysis
## 本章节开始开始进行数据的分析。其中包括`matplotlib`
## 01 matplotlib基础绘图和调整x轴
### 相关介绍：
### 1.导入 `matplotlib` 模块
        from matplotlib import pyplot as plt
### 2.通常要通过`figsize` 设置图片的大小
### 3.开始绘图
        plt.plot(x, y)
### 注：1.我们可以使用 `_xtick_label` `_ytick_label` 对x轴和y轴进行设置，如果不进行设置的话，通过默认输出的值达不到我们的需求。
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
### 目标分析：在一张图片里面绘制2个折线图
## 04 `matplotlib` 绘制散点图
### 目标介绍：根据数据绘制2个散点图。
### 相关介绍：1.想在一张图片里面绘制出2个散点图，需要将第二个图片的x的数据点整体
