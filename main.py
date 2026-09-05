#在main.py中调用引擎
import yfinance as yf
from src.engine import calculate_zscore,generate_signals
from src.utils import get_proxy_session
import matplotlib.pyplot as plt

def run_strategy():
    # 1.获取session
    #这里的ip和port可以根据实际情况修改
    my_session=get_proxy_session(ip="192.168.1.136",port="7890")
    tickers=["KO","PEP"]
    print(f"正在通过代理抓取 {tickers} 数据...")

    #2.下载数据
    #auto_adjust=False 确保我么能拿到独立的Adj Close列
    data=yf.download(
        tickers,
        start='2022-01-01',
        end='2024-01-01',
        session=my_session,
        auto_adjust=False
    )['Adj Close']

    if data.empty:
        print("❌ 数据为空，请检查代理设置")

    #下载后立刻保存到data文件夹
    data.to_csv("data/raw_prices.csv")
    print("原始数据已缓存至data/raw_prices.csv")

    #3.策略逻辑（调用engine.py里的函数）
    ratio=data['KO']/data['PEP']
    z_score=calculate_zscore(ratio,window=30)
    signals=generate_signals(z_score,threshold=2.0)

    #4.打印最新状态
    current_status = "买入 KO/卖出 PEP" if signals.iloc[-1] == 1 else \
                     "卖出 KO/买入 PEP" if signals.iloc[-1] == -1 else "观望"
    print(f"策略计算完成，当前建议状态：{current_status}")

    #5.可视化（在工业项目中，通常会保存为图片）
    z_score.plot()
    plt.title("Z-Score Logic")
    plt.savefig("result_plot.png") #保存结构，方便上传github
    print("结果图已保存为result_plot.png")

if __name__=="__main__":
    run_strategy()
