#coding=utf-8
#加载模型进行预测

# 加载提前训练好的模型
from sklearn.externals import joblib


def Predict_LinearSVM(P_rect, P_extend, P_spherical, P_leaf, P_circle):
# def Predict_LinearSVM(P_rect, P_extend, P_spherical, P_leaf, P_circle,P_complecate):
    lsvc = joblib.load('model/lsvc.model')

    result = lsvc.predict([P_rect, P_extend, P_spherical, P_leaf, P_circle])
    # result = lsvc.predict([P_rect, P_extend, P_spherical, P_leaf, P_circle,P_complecate])
    return result[0]

def Predict_LinearRegression(P_rect, P_extend, P_spherical, P_leaf, P_circle):
# def Predict_LinearRegression(P_rect, P_extend, P_spherical, P_leaf, P_circle,P_complecate):
    lr = joblib.load('model/lr.model')

    result = lr.predict([P_rect, P_extend, P_spherical, P_leaf, P_circle])
    # result = lr.predict([P_rect, P_extend, P_spherical, P_leaf, P_circle,P_complecate])
    return result[0]

def Predict_KneiborClassfier(P_rect, P_extend, P_spherical, P_leaf, P_circle):
# def Predict_KneiborClassfier(P_rect, P_extend, P_spherical, P_leaf, P_circle,P_complecate):
    knc = joblib.load('model/lr.model')

    result = knc.predict([P_rect, P_extend, P_spherical, P_leaf, P_circle])
    # result = knc.predict([P_rect, P_extend, P_spherical, P_leaf, P_circle,P_complecate])
    return result[0]
