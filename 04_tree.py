from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.tree import DecisionTreeClassifier,export_graphviz
from sklearn.ensemble import RandomForestClassifier
import pandas as pd 
def decision():
    """
    决策树对泰坦尼克号进行预测生死

    """
    # 1. pd 读取数据
    titan = pd.read_csv("http://biostat.mc.vanderbilt.edu/wiki/pub/Main/DataSets/titanic.txt")
    # 2. 选择有影响的特征 ，处理缺失值
    # 特征数据和目标值的提取
    x = titan[['pclass','age','sex']]
    y = titan['survived']

    # 缺失值处理
    x['age'].fillna(x['age'].mean(), inplace = True)


    # 3. 进行特征工程， pd转换字典，特征抽取
    # 分割数据集
    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.25)  


    # 进行特征工程  one-hot编码
    dict = DictVectorizer(sparse=False)
    x_train = dict.fit_transform(x_train.to_dict(orient = "records"))

    print(dict.get_feature_names())

    x_test = dict.transform(x_test.to_dict(orient = "records"))
    # print(x_train)

    # # 4. 决策树估计器流程
    # dec = DecisionTreeClassifier()

    # dec.fit(x_train, y_train)

    # print("准确率",dec.score(x_test,y_test))

    # # 导出树的结构
    # export_graphviz(dec, out_file="./tree.dot",feature_names = ['年龄', 'pclass=1st', 'pclass=2nd', 'pclass=3rd', '女性', '男性'])


    # 随机森林进行预测（超参数调优）
    rf = RandomForestClassifier()

    # 网格搜索交叉验证
    param = {"n_estimators":[100,120,200,300,500,1200],"max_depth":[3,4,5,8,15,30]}
    gc = GridSearchCV(rf, param_grid=param, cv=2)

    gc.fit(x_train,y_train)

    print("准确率",gc.score(x_test,y_test))
    print("查看选择的参数模型",gc.best_params_)

    return None


if __name__ == "__main__":
    decision()


