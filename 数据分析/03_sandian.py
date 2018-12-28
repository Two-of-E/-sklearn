from matplotlib import font_manager
from matplotlib import pyplot as plt

y_3 = [1,5,3,6,7,8,9,10,11,10]
y_10 = [10,11,10,9,8,7,6,3,5,1]

x_3 = range(0,10)
x_10 = range(20,30)

plt.figure(figsize=(15,6), dpi=80)

plt.scatter(x_3,y_3)
plt.scatter(x_10,y_10)

# 调整x轴的刻度

plt.show()

