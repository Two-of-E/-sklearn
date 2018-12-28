import numpy as np

us_file_path = "./ceshi.csv"
# unpack=True转置，读取时进行转置
t1 = np.loadtxt(us_file_path,delimiter=",",dtype="double")
# 在np里实现数组的转置 t1.T也行
# t1 = t1.transpose()

# 取不连续的多行
# print(t1[[2,3,5]])

# 取列
# print(t1[:,[3,2]])
# t2 = t1[:,[3,2]]
# 取指定行列的值
t2 = t1[2:5,1:3]
# 取不相邻的点
t2 = t1[[0,1],[0,2]]
print(t2)
