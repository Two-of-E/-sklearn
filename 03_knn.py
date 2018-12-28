from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report
import pandas as pd 


""" 
    分类：
        特征值：x，y坐标 定位准确性，时间，
        目标值：入住的id
    处理：
        1. 数据量太大，缩小xy的坐标
        2. 判断时间戳进行是否进行处理（转换成年月日时分秒），当做新的特征，丰富特征值
        3. 几千～几万的目标值类别数量过大

"""

def knncls():
    # 读取数据
    data = pd.read_csv("./03_knn/train.csv")

    # print(data.head(10))
    # 处理数据
    # 1.缩小数据,查询数据筛选
    data = data.query("x > 1.0 & x < 1.20 & y > 2.5 & y<2.70")
    # 处理时间的数据
    time_value = pd.to_datetime(data['time'], unit='s')
    # print(time_value)
    # 把日期换成字典格式
    time_value = pd.DatetimeIndex(time_value)

    # 构造特征
    data['day'] = time_value.day
    data['hour'] = time_value.hour
    data['weekday'] = time_value.weekday

    # 把时间戳特征删除
    data= data.drop(['time'],axis = 1)

    # 把签到数量少于N的删除
    place_count = data.groupby('place_id').count()
    # 大于3的保留下来  reset_index：旧索引将作为列添加，并使用新的顺序索引
    tf = place_count[place_count.row_id > 3].reset_index()
    data = data[data['place_id'].isin(tf.place_id)]

    # 取出数据当中的特征值和目标值
    y = data['place_id']

    x = data.drop(['place_id'], axis = 1)
    x = data.drop(['row_id'], axis = 1)

    # 进行数据的分割
    # y_train对应训练的目标值
    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.25)  

    #特征工程（标准化）
    std = StandardScaler()

    # 对测试机和训练集的特征值进行标准化
    x_train = std.fit_transform(x_train)
    x_test = std.transform(x_test)

    """
    自定义K值

    # 进行算法流程
    knn = KNeighborsClassifier(n_neighbors=5)

    # fit predict 
    knn.fit(x_train,y_train) 

    # 得出预测结果

    y_predict = knn.predict(x_test)
    print("预测值",y_predict)
    print("////////////////////////////////////////////////////")

    print("正确率",knn.score(x_test,y_test))
    """
    knn = KNeighborsClassifier()
    param = {"n_neighbors":[3,5,10]}
    
    gc = GridSearchCV(knn, param_grid=param, cv=10)
    gc.fit(x_train,y_train)
    print("测试集准确率",gc.score(x_test,y_test))
    print("在交叉验证中最好的结果：",gc.best_score_)
    print("选择最好的模型",gc.best_estimator_)
    print("每个超参数每次交叉验证的结果",gc.cv_results_)


    return None


def naviebayes():

    news = fetch_20newsgroups(subset='all')

    # 进行数据分割
    x_train,x_test,y_train,y_test = train_test_split(news.data,news.target,test_size = 0.25)  

    # 对数据集进行特征抽取
    tf = TfidfVectorizer()
    # 以训练集当中的词的列表进行每篇文章重要性统计
    x_train = tf.fit_transform(x_train)

    # print(tf.get_feature_names())
    # print(x_train)

    x_test = tf.transform(x_test)

    # 进行预测
    mlt = MultinomialNB(alpha=1.0)
    


    mlt.fit(x_train,y_train)

    y_predict = mlt.predict(x_test)
    print(y_predict)

    print("正确率",mlt.score(x_test,y_test))

    print("每个类别的精确率和召回率",classification_report(y_test, y_predict, target_names=news.target_names))
    return None







if __name__ == "__main__":
    knncls()


