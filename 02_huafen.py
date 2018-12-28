from sklearn.datasets import load_iris,fetch_20newsgroups,load_boston
from sklearn.model_selection import train_test_split

li = load_iris()
# print("特征值")
# print(li.data)
# print("目标值")
# print(li.target)
# print(li.DESCR)

# 返回值：训练集

# x_train,x_test,y_train,y_test = train_test_split(li.data,li.target,test_size = 0.25)

# print(x_train,y_train)
# print(x_test,y_test)


# news = fetch_20newsgroups(subset='all') 
# print(news.data)
# print(news.target)

lb = load_boston()



