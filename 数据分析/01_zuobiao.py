from matplotlib import pyplot as plt

x = range(2,26,2)
y = [15,13,14.5,17,20,25,26,26,24,22,18,15]

#设置图片大小
plt.figure(figsize=(15,6),dpi=80)

plt.plot(x,y)

# 绘制x轴的刻度
_xtick_labels = [i/2 for i in range(4,49)]
plt.xticks(_xtick_labels[::3])
plt.yticks(range(min(y),max(y)+1))
#保存
plt.savefig("./t1.png")


plt.show()





