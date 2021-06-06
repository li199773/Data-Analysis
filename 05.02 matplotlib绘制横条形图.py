"""
条形图：
数据是离散的采用条形图来绘制
项目的需求：
    假设你获取到了2017暖内地电影票房前20的电影和电影的票房数据，那么如何更加直观的展示该数据呢？
a = ["战狼2","速度与激情6","功夫瑜伽","西游降佛篇","变形金刚5 最后的骑士","摔跤吧 爸爸","加勒比海盗5 死无对证","金刚 骷髅岛","极限特工 终极回归"
,"生化危机6 终章","乘风破浪","神偷奶爸3","智取威虎山","大闹天竺","金刚狼3 殊死一战","蜘蛛侠 英雄归来","悟空传","银河护卫队2","情圣","新木乃伊"]
b = [56.01,26.49,17.53,16.49,15.45,12.96,11.8,11.61,11.28,11.12,10.49,10.3,8.75,7.55,7.32,6.99,6.88,6.86,6.58,6.23]单位 亿
"""
from matplotlib import pyplot as plt
import matplotlib

matplotlib.rc("font", family=' DengXian')

plt.figure(figsize=(20, 8), dpi=80)

a = ["战狼2", "速度与激情6", "功夫瑜伽", "西游降佛篇", "变形金刚5 最后的骑士", "摔跤吧 爸爸", "加勒比海盗5 死无对证", "金刚 骷髅岛", "极限特工 终极回归", "生化危机6 终章", "乘风破浪", "神偷奶爸3", "智取威虎山", "大闹天竺", "金刚狼3 殊死一战", "蜘蛛侠 英雄归来", "悟空传",
     "银河护卫队2", "情圣", "新木乃伊"]
b = [56.01, 26.49, 17.53, 16.49, 15.45, 12.96, 11.8, 11.61, 11.28, 11.12, 10.49, 10.3, 8.75, 7.55, 7.32, 6.99, 6.88, 6.86, 6.58, 6.23]

# barh就是绘制横向条形图(看源码即可，转换成横向的)
plt.barh(range(len(a)), b, height=0.3, color="red")  # 首先先画一个图出来,将图片绘制成0.3

plt.yticks(range(len(a)), a)  # 将上面的文字一一对应即可
# 这里要将 xticks 换成 yticks 即可

# 绘制一个网格，看得更清楚一些
plt.grid(alpha=0.4)

plt.show()
