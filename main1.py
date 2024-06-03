from bs4 import BeautifulSoup
import pandas as pd
import requests


url = 'https://www.rib.gg/ja/series/63736?match=0&tab=player-stats&time-range=0,150&plot=heatmap&kill-type=all&kd-mode=kills&players=8386&location=all'
# BeautifulSoupでHTMLをパース
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

# 行を見つける
rows = soup.find_all('tr', class_='MuiTableRow-root')


# data = {'player' ,'KD', 'ACS','K',D,A,plus,KD,ADR,FK,FD,puls,Clutches,KAST,HS}
# 各行のデータを抽出
for row in rows:
    # 列を取得
    columns = row.find_all('td')
    # 各列のテキストを取得して出力
    for column in columns:
        print(column.text.strip())
    print('---')

    csvlist=[]
    for elem in elem:
        csvlist.append(elem)

    f = open("pal.csv","w",encoding='utf-8')
    writecsv = csv.writer(f,lineterminator= '\n')

    writecsv.writerow(csvlist)
    f.close
#player ,KD, ACS,K,D,A,plus,KD,ADR,FK,FD,puls,Clutches,KAST,HS