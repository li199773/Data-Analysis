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
## 02.01 matplotlib绘制 0-12 的气温图
