import requests
from bs4 import BeautifulSoup
import lxml
#/web/search/risk?key=《中华人民共和国招标投标法实施条例》&f=%7B"dt"%3A"2"%7D&pi=1
url=' https://qcc.com/web/search/risk?key=《中华人民共和国招标投标法实施条例》&f=%7B"dt"%3A"2"%7D&pi=1'
headers={
    "cookie": "qcc_did=7d73a6e1-c64f-4227-919c-90516b986fc5; UM_distinctid=184a9af8c4e593-0fb5535465ea93-26021e51-1bcab9-184a9af8c4fd87; zg_did=%7B%22did%22%3A%20%22184aa004aa0319-0cc69c21bb2c74-26021e51-1bcab9-184aa004aa110f8%22%7D; zg_d609f98c92d24be8b23d93a3e4b117bc=%7B%22sid%22%3A%201669299456675%2C%22updated%22%3A%201669299466431%2C%22info%22%3A%201669299456676%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.qcc.com%22%7D; MQCCSESSID=835dfb204589d53a4fdc8a6453; QCCSESSID=265f1c19490a25b92165cc71b9; CNZZDATA1254842228=204300658-1669293443-%7C1669366346; acw_tc=3caa0b9e16693669231595818e6cd6b2245d4d48e7fe64efe88752b135",
    "User-Agent": "User-Agent:Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
}
response = requests.get(url, headers=headers,timeout=5)
print(response.text)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
try:
    if response.status_code != 200:
        response.encoding = 'utf-8'
        print(response.status_code)
        print('ERROR')
        print(response.text)
    #soup = BeautifulSoup(response.text, "lxml")
except Exception:
    print('请求失败')
name=soup.select('div.app-search-risk > div.container.m-t > div.risk-list > div > div.bigsearch-list > table > tr:nth-child(1) > td > div > div > div:nth-child(3) > span > span > span > span')
for name in name:
    print(name.get_text())


