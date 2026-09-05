import requests
import yfinance as yf

def get_proxy_session(ip="192.168.1.136",port="7890"):
    #创建并返回一个配置好代理的Session对象
    session=requests.Session()
    session.headers.update({
        'User-Agent':'Mozilla/5.0  (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    })

    proxy_url=f"http://{ip}:{port}"
    session.proxies.update({
        'http':proxy_url,
        'https':proxy_url
    })

    return session