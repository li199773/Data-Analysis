from matplotlib.font_manager import FontManager

mpl_fonts = set(f.name for f in FontManager().ttflist)

print('all font list get from matplotlib.font_manager:')

for f in sorted(mpl_fonts):
    print('\t' + f)

"""
会显示出所有支持的字体，大约100多种
其中你会发现有如下中文字体：
    DengXian
    FangSong
    KaiTi
    LiSu
    YouYuan
    Adobe Fan Heiti Std
    Adobe Fangsong Std
    Adobe Heiti Std
    Adobe Kaiti Std
"""
