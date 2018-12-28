from matplotlib import pyplot as plt
import random
import matplotlib
from matplotlib import font_manager
# windows和linux上设置
# font = {'family' : 'NotoSansCJK-Bold',
#         'weight' : 'bold',
#         'size'   : 'larger'}

# matplotlib.rc(font, **font)
# 解决中文的问题
# fc-list ：lang=zh命令查看可以用的字体
my_font = font_manager.FontProperties(fname="/home/jack/文档/字体/simhei.ttf")


x =  range(0,120)
y = [random.randint(20,35) for i in range(120)]

# dpi每英寸的像素值
plt.figure(figsize=(15,6),dpi=80)

plt.plot(x,y)

# 调整x轴的刻度
# 解决中文不显示
_xtick_lables = ["十点{}".format(i) for i in range(60)]
_xtick_lables += ["11:{}".format(i) for i in range(60)]

# 对列表取步长，数字和字符串一一对应，数据的长度都一样.
# rotation度数
plt.xticks(list(x)[::10],_xtick_lables[::10],rotation=45,fontproperties = my_font)
plt.xlabel("Time")
plt.ylabel("Temperature")

plt.show()