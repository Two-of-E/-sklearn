import numpy as np

us_data = "./us.csv"
uk_data = "./uk.csv"

# 加载国家数据

us_data = np.loadtxt(us_data,delimiter=",",dtype="double")
uk_data = np.loadtxt(uk_data,delimiter=",",dtype="double")

# 添加国家
#构造全为0的数据:制作标记
zeros_data = np.zeros((us_data.shape[0],1))
ones_data = np.ones((uk_data.shape[0],1))

# 分别添加一列全为0,1的数组：添加标记
us_data = np.hstack((us_data,zeros_data))
uk_data = np.hstack((uk_data,ones_data))

# 拼接两组数据
  
final_data = np.vstack((us_data,uk_data))
print(final_data)
