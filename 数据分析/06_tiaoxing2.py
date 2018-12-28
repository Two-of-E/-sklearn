from matplotlib import pyplot as plt
from matplotlib import font_manager



a = ["海王","无名之辈","狗十三","毒液：致命守护者"]

b_11 = [7370,638,291,135]
b_12 = [6198,595,324,118]
b_13 = [5478,580,363,117]

my_font = font_manager.FontProperties(fname="/home/jack/文档/字体/simhei.ttf")

bar_width = 0.2

x_11 = list(range(len(a)))
x_12 = [i+bar_width for i in x_11]
x_13 = [i+bar_width*2 for i in x_11]


plt.bar(range(len(a)),b_11,width = bar_width,label = "12月11日")
plt.bar(x_12,b_12,width = bar_width,label = "12月12日")
plt.bar(x_13,b_13,width = bar_width,label = "12月13日")

# 设置图例
plt.legend(prop = my_font)

plt.xticks(x_12,a,fontproperties = my_font)

plt.show()



