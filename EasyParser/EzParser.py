# HTTP 請求模組 (pip3 install requests2)
import requests as rq

# 解析 HTML 快速套件 (pip3 install beautifulsoup4)
from bs4 import BeautifulSoup

# 檔案處理模組
import io

# 時間處理模組
import time


# 定義休息函數(以避免被 Server 認為 DDOS 攻擊)
def SleepWindow(hour, min, sec):
    return hour*3600 + min*60 + sec

# 定義判斷項目數量函數
def BreakWhenMax(count, max):
    if count >= max:
        return True
    else:
        return False

# 主要邏輯
tStart = time.time()
file = io.open("EasyParser\\International_Finance_News_Title_List.txt", "ab+")

itemCount = 0
itemMax = 100
itemStrList = []

link = "https://tw.stock.yahoo.com/intl-markets"                    # 因為是動態網頁，不一定能一次抓到 itemMax 筆
response = rq.get(link)                                             # 使用 requests 將網頁抓下來
soup = BeautifulSoup(response.text, "lxml")                         # 使用 BeautifulSoup 解析抓下來的內容(搭配 LXML 解析器)
for find in soup.findAll('u', {'class': 'StretchedBox'}):
    title = find.next
    if len(title) > 0:
        #print (title)
        #file.write((title + "\n").encode('utf-8'))
        itemStrList.append((title + "\n").encode('utf-8'))          # Append the title into list
        itemCount += 1
        if BreakWhenMax(itemCount, itemMax) == True:
            break
    time.sleep(SleepWindow(0, 0, 1))

file.writelines(itemStrList)                                        # Write the all titles at one time

tEnd = time.time()
timeMsg = "[EzParser] Time Spend: %f (sec)\n\n" % (tEnd - tStart)
print (timeMsg)
file.write(timeMsg.encode('utf-8'))
file.close()
