import numpy as np
import pandas as pd
def calculate_zscore(series,window=30):
    # 封装计算Z-Score的逻辑，方便重复调用
    rlook=series.rolling(window=window)
    mean=rlook.mean()
    std=rlook.std()
    return (series-mean)/std

def generate_signals(zscore,threshold=2.0):
    #封装信号产生逻辑
    signals=pd.Series(index=zscore.index,data=0)
    signals[zscore>threshold]=-1 #卖出
    signals[zscore<threshold]=1 #买入
    return signals

