import numpy as np



def fill_ndarray(t1):
    for i in range(t1.shape[1]):
        #遍历每一列
        temp_col = t1[:,i]
        
        # 判断是否有nan
        if np.count_nonzero(temp_col!=temp_col) != 0:
            temp_not_nan_col = temp_col[temp_col==temp_col]
            # mean()函数求取均值
            temp_col[np.isnan(temp_col)] = temp_not_nan_col.mean()
    return t1

if __name__ == "__main__":
    t1 = np.arange(12).reshape((3,4)).astype("float")
    #在第二行第三个数及以后都设为nan
    t1[1,2:] = np.nan
    print(t1)
    t1 = fill_ndarray(t1)
    print(t1)

