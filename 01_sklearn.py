from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
from sklearn.preprocessing import MinMaxScaler,Imputer,StandardScaler
from sklearn.feature_selection import VarianceThreshold
from sklearn.decomposition import PCA
import jieba
import numpy as np


def dictvec():
    """
    字典数据数据抽取
    return NONE
    """
    dict = DictVectorizer()

    data = dict.fit_transform([{'city':'北京','temp':100},{'city':'上海','temp':27},{'city':'杭州','temp':50}])

    print("fit_transform",data)

    data = dict.transform([{'city':'北京','temp':100},{'city':'上海','temp':27},{'city':'杭州','temp':50}])
    print("transform",data)
    # 得到特征值
    # print(dict.get_feature_names())

    # print(dict.inverse_transform(data))
    # print(data.toarray())
    return None

# 对英文进行处理
def countvec():
    """
    对文本进行特征值化
    return None
    """
    cv = CountVectorizer()
    data = cv.fit_transform(["Life is short,i like python","life is too long , i dislike python"])
    # 不支持中文,要用jieba进行分词
    # data = "杨幂刘恺威离婚！将以亲人身份共同抚养孩子 ,气愤！不到3块钱 你的自拍竟被印在酒店小卡片上 ,皇马夺世俱杯三连冠；曼城蓝军爆大冷输球；索圣首秀大胜 ,灵活多变的MK-48垂发系统，为节省空间可以挂在直升机机库上 ,暴风集团巨亏 2千万资金能否偿还3日后2亿到期债券？ ,“武汉号”有多牛？央视新闻：互联网要“上天”了 ,房地产“差别化调控”变“分类指导”，意味着什么？ ,反转！“老太被电动车带倒诬陷公交车”事件司机道歉 ,日本抗议军机遭韩军舰雷达照射 韩军：反应过度 " 
    # data = jieba.cut(data)
    # print(data)
    # print("--------------------------\n")
    # data = cv.fit_transform(data)
    # data = cv.fit_transform(["人生苦短，我喜欢python","人生漫长 , 不用python"])
    print(cv.get_feature_names())
    #单个字母不进行统计
    print(data.toarray())

    return None


# 中文词汇切割
def cutword(data):
    data = jieba.cut(data)
    # 转化成列表
    data_list = list(data)
    # 列表转化成字符串
    data_str = ' '.join(data_list)

    return data_str

# 汉字特征处理
def hanzivec():
    """
    中文特征值化
    """
    cv = CountVectorizer()
    data = open("./essays.txt")
    # 转为字符串类型的
    data = " ".join(data.readlines())
    

    data = cutword(data)
    # print(data)
    data = cv.fit_transform([data])
    data_feat = cv.get_feature_names()
    #print(data_feat)
    data_array = data.toarray()
    #print(data_array)
    print(np.where(data_array == 7))
    print(data_feat[187])
    return None



# tfidf文章分类优化 
def tfidfvec():
    """
    中文特征值化
    """
    tf = TfidfVectorizer()

    data_str1 = cutword("""那最美的花瓣是柔软的，那最绿的草原是柔软的，
    那最广大的海是柔软的，那无边的天空是柔软的，那在天空自在飞翔的云，最是柔软!
    我们心的柔软，可以比花瓣更美，比草更绿，比海洋更广，比天空更无边，比云还要自在
    ，柔软是最有力量，也是最恒常的。且让我们在卑湿污泥的人间，开出柔软清净的智慧之
    莲吧!""")
    data_str2 = cutword("他唱的是心中的荒凉之城吧!外在的城池，时而繁华，时而荒凉，内心那小小寂寞的城呀!虽也有兴衰起落，却总有一块无欢的幽州台，前不见古人，後不见来者，念天地之悠悠，独怆然而涕下!在最深最深的地方，这是诗人的大寂寞，也是诗人的荒城。")
    data_str3 = cutword("柠檬花盛开时节，我走过柠檬园，花的浓郁的芬芳总是熏得我迷离。一切花中，柠檬花是最香甜的，有稠稠的蜜意;但是一切果里，柠檬果又是最酸涩的，其酸胜醋。这种迷离之感，使我忍不住会附身细细地端详柠檬花，看着一花五叶的纯白中，生起嫩嫩的黄，有的还描着细细的紫色滚边，让花的香甜流入我的胸腹。")
    # print(data)
    data = tf.fit_transform([data_str1,data_str2,data_str3])
    data_feat = tf.get_feature_names()
    print(data_feat)
    data_array = data.toarray()
    print(data_array)
    # print(np.where(data_array == 7))
    # print(data_feat[187])

    return None


def mm():
    """
    归一化处理
    """
    mm = MinMaxScaler()

    data = mm.fit_transform([[90,2,10,40],[60,4,15,45,],[75,3,13,46]])

    print(data)

    return None 
def stand():
    """
    标准化
    """
    std = StandardScaler()
    data = std.fit_transform([[1.,-1.,3.],[2.,4.,2.,],[4.,6.,-1]])
    print(data)
    return None

# def im():
#     """
#     缺失值处理
#     """
#     Imputer()

def var():
    """
    删除低方差的特征
    """
    var = VarianceThreshold(threshold=0.0)
    data = var.fit_transform([[0,2,0,3],[0,1,4,3],[0,1,1,3]])
    print(data)
    return None

def pca():
    """
    主成分分析进行降维
    """
    pca = PCA(n_components=0.9)
    data = pca.fit_transform([[2,8,4,5],[6,3,0,8],[5,4,9,1]])
    print(data)
    return None

if __name__ == "__main__":
    dictvec()