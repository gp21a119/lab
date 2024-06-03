# lab
import requests
from bs4 import BeautifulSoup
import csv
import os

# 現在の作業ディレクトリを表示
current_directory = os.getcwd()
print(f"カレントディレクトリは: {current_directory}")

# URLを設定
url = 'https://www.rib.gg/ja/series/63736?match=0&tab=player-stats&time-range=0,150&plot=heatmap&kill-type=all&kd-mode=kills&players=8386&location=all'

# URLからHTMLを取得してパース
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

# テーブルの行を取得
rows = soup.find_all('tr', class_='MuiTableRow-root')

# CSVファイルに書き込むデータを格納するリスト
data = []

# 各行のデータを抽出
for row in rows:
    # 列を取得
    columns = row.find_all('td')
    # 各列のテキストをリストとして抽出
    row_data = [column.text.strip() for column in columns]
    # 行データが存在する場合のみ追加
    if row_data:
        data.append(row_data)

# CSVファイルに書き込む
with open("player_stats.csv", "w", newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    # ヘッダーを書き込む（ヘッダーが存在する場合は追加）
    writer.writerow(['Player', 'KD', 'ACS', 'K', 'D', 'A', '+/-', 'KD', 'ADR', 'FK', 'FD', '+/-', 'Clutches', 'KAST', 'HS'])
    # データを書き込む
    writer.writerows(data)

print("CSVファイルが作成されました。")