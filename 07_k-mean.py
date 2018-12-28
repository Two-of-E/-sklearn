from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import pandas as pd
import matplotlib.pyplot as plt

# 读取四张表的数据
prior = pd.read_csv("./超市/order_products__prior.csv")
products = pd.read_csv("./超市/products.csv")
orders = pd.read_csv("./超市/orders.csv")
aisles = pd.read_csv("./超市/aisles.csv")

# 合并四张表，用户和物品类别
_mg = pd.merge(prior,products,on=['product_id','product_id'])
_mg = pd.merge(_mg,orders,on=['order_id','order_id'])
mt = pd.merge(_mg,aisles,on = ['aisle_id','aisle_id'])

# 交叉表（特殊的分组）
cross = pd.crosstab(mt['user_id'],mt['aisle'])

# 进行主成分
pca = PCA(n_components = 0.9)

data = pca.fit_transform(cross)

# 降低样本数量

x = data[:500]
km = KMeans(n_clusters=4)
km.fit(x)
predict = km.predict(x)

plt.figure(figsize = (10,10))

# 随机指定两个特征

# 建立四个颜色的列表
colored = ['orange', 'green', 'blue', 'red']

colr = [colored[i] for i in predict]
plt.scatter(x[:, 1],x[:,20],color =colr )

plt.xlabel("1")
plt.xlabel("20")
print(silhouette_score(x, predict))
plt.show()

