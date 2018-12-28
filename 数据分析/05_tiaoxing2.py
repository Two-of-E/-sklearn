# 横着的条形图

from matplotlib import pyplot as plt
from matplotlib import font_manager

a = ["战狼2","速度与激情8","羞羞的铁拳","前任3：再见前任","功夫瑜伽","西游伏妖篇","变形金刚5：最后的骑士"
,"芳华","摔跤吧！爸爸","寻梦环游记","加勒比海盗5：死无对证","金刚：骷髅岛","极限特工：终极回归","生化危机6：终章","乘风破浪"
,"神偷奶爸3","智取威虎山","蜘蛛侠：英雄归来","大闹天竺","雷神3：诸神黄昏"]

b = [871.41,876.95,797.47,777.32,765.46,752.2,720.28,626.89,586.15,649.42,603.73,583.31,547.78,498.56,491.75,523.17,513.11,475.22,500.2,375.46]

my_font = font_manager.FontProperties(fname="/home/jack/文档/字体/simhei.ttf")

plt.figure(figsize=(10,6),dpi=80)
plt.barh(range(len(a)),b,height=0.3,color = "orange")
# 将y轴和中文对应
plt.yticks(range(len(a)),a,rotation=0,fontproperties = my_font)

plt.grid(alpha=0.5)

plt.show() 
