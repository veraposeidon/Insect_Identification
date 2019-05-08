# coding=utf-8

import pandas as pd

# 创建特征列表
column_names = ['P_rect', 'P_extend', 'P_spherical', 'P_leaf', 'P_circle', 'Species']
# column_names = ['P_rect', 'P_extend', 'P_spherical', 'P_leaf', 'P_circle','P_complecate', 'Species']
data = pd.read_csv('data/data.csv', names=column_names)

# print data.shape

# 这个功能快要被抛弃了,分割训练和测试集
from sklearn.cross_validation import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(data[column_names[0:5]], data[column_names[5]], test_size=0.25,
                                                    random_state=33)

# print Y_train.value_counts()
# print Y_test.value_counts()

# 数据整理，但是整形的，需要注意
# from sklearn.preprocessing import StandardScaler
# ss = StandardScaler()
# X_train = ss.fit_transform(X_train)
# X_test = ss.transform(X_test)

from sklearn.neighbors import KNeighborsClassifier

knc = KNeighborsClassifier()
knc.fit(X_train, Y_train)
knc_y_predict = knc.predict(X_test)

from sklearn.metrics import classification_report

print "LR 精确度：" + str(knc.score(X_test, Y_test))
print classification_report(Y_test, knc_y_predict, target_names=[ 'fly','wo','jingui','zhang','zhizhu'])

# 保存训练结果，供后面直接使用
from sklearn.externals import joblib

joblib.dump(knc,'model/knc.model')
