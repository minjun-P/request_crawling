import pandas as pd
import requests
from bs4 import BeautifulSoup as BS
from matplotlib import pyplot as plt

url = 'https://finance.naver.com/item/sise_day.nhn?code=302440&page=1'
headers = {'User-Agent':
           'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'}

# 마지막 페이지 가져오기 
res = requests.get(url, headers = headers)
soup = BS(res.content, 'lxml')
last_page = soup.select_one('td.pgRR a')['href'].split('=')[-1]

# 빈 테이블 생성                                                                     
df = pd.DataFrame()

# 빈 테이블에 일별 시세 데이터 추가
for page in range(1, int(last_page)+1):
    url = 'https://finance.naver.com/item/sise_day.nhn?code=302440&page='+str(page)
    res = requests.get(url,headers = headers)
    table = pd.read_html(res.content,header=0)[0]
    df = df.append(table)
    print(page)

#데이터 후처리
df.dropna(inplace=True)
df.set_index('날짜',inplace=True)
print(df)
    
