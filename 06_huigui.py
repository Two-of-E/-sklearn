from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression, SGDRegressor, Ridge, LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, classification_report
from sklearn.externals import joblib
import numpy as np
import pandas as pd

def mylinear():
    """
    预测房子价格
    """
    # 获取数据
    lb = load_boston()

    #分割数据集
    x_train,x_test,y_train,y_test = train_test_split(lb.data,lb.target, test_size = 0.25)
    
    
    # 进行标准化处理
    # 特征值和目标值都需进行标准化处理， 并实例化两个API
    std_x = StandardScaler()
    x_train = std_x.fit_transform(x_train)
    x_test = std_x.transform(x_test)

    # 目标值
    std_y = StandardScaler()
    y_train = std_y.fit_transform(y_train.reshape(-1,1))
    y_test = std_y.transform(y_test.reshape(-1,1))

    # 预测
    # 正规方程
    lr = LinearRegression()
    lr.fit(x_train,y_train)

    # 保存训练好的模型
    joblib.dump(lr,"./tmp/test.pkl")

    # # 调用模型
    # model = joblib.load("./tmp/test.pkl")
    # y_predict = std_y.inverse_transform(model.predict(x_test))
    # print("保存好的模型的结果",y_predict)

    # 超参数
    # print(lr.coef_)

    # 预测测试集房子价格
    y_predict = std_y.inverse_transform(lr.predict(x_test))
    print("测试集里面每个房子的价格",y_predict)
    print("均方误差",mean_squared_error(std_y.inverse_transform(y_test),y_predict))

    # 梯度下降
    sgd = SGDRegressor()
    sgd.fit(x_train,y_train)
    # print(sgd.coef_)

    # 预测测试集房子价格
    y_predict = std_y.inverse_transform(sgd.predict(x_test))
    print("测试集里面每个房子的价格",y_predict)
    print("均方误差",mean_squared_error(std_y.inverse_transform(y_test),y_predict))

    # 岭回归取进行房价预测
    rd = Ridge(alpha=1.0)
    rd.fit(x_train,y_train)
    # print(sgd.coef_)

    # 预测测试集房子价格
    y_predict = std_y.inverse_transform(rd.predict(x_test))
    print("测试集里面每个房子的价格",y_predict)
    print("均方误差",mean_squared_error(std_y.inverse_transform(y_test),y_predict))

def logistic():
    """
    逻辑回归
    """
    # 1. pd 读取数据
    # 构造列名
    column = ['Sample code number','Clump Thickness','Uniformity of Cell Size','Uniformity of Cell Shape ','Marginal Adhesion','Single Epithelial Cell Size','Bare Nuclei','Bland Chromatin','Normal Nucleoli','Mitoses','Class']

    data = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data",names= column)
    data = data.replace(to_replace = '?',value = np.nan)

    data = data.dropna()

    # 进行数据的分割
    x_train,x_test,y_train,y_test = train_test_split(data[column[1:10]],data[column[10]], test_size = 0.25)

    # 标准化处理
    std = StandardScaler()
    x_train = std.fit_transform(x_train)
    x_test = std.transform(x_test)

    lg = LogisticRegression(C=1.0)
    lg.fit(x_train,y_train)
    print(lg.coef_)
    y_predict = lg.predict(x_test)
    print("准确率",lg.score(x_test, y_test))
    print("召回率",classification_report(y_test, y_predict, labels = [2,4],target_names=["良性","恶性"]))

    return None


if __name__ == "__main__":
    logistic()