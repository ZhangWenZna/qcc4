import requests
import time
from lxml import etree




class GetHtml():
    def __init__(self):
        self.all_com = []
        self.all_phone = []
        self.all_name = []
        self.all_em = []
    def getHtml(self,url):
        try:
            time.sleep(5)
            headers = {
                'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
                'CooKie': 'qcc_did=7d73a6e1-c64f-4227-919c-90516b986fc5; UM_distinctid=184a9af8c4e593-0fb5535465ea93-26021e51-1bcab9-184a9af8c4fd87; zg_did=%7B%22did%22%3A%20%22184aa004aa0319-0cc69c21bb2c74-26021e51-1bcab9-184aa004aa110f8%22%7D; zg_d609f98c92d24be8b23d93a3e4b117bc=%7B%22sid%22%3A%201669369069905%2C%22updated%22%3A%201669369116745%2C%22info%22%3A%201669299456676%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.qcc.com%22%2C%22zs%22%3A%200%2C%22sc%22%3A%200%2C%22firstScreen%22%3A%201669369069905%7D; MQCCSESSID=bec6652534b2b6d4643dedb510; QCCSESSID=39dd37e8784e6e29db4f037be4; acw_tc=af062a1816695312320397525eb7aafbdb1376e84ad640b0f43e85da10; CNZZDATA1254842228=204300658-1669293443-%7C1669529678'            }
            html = requests.get(url, headers=headers).text
            return html
        except Exception as e:
            return "获取html异常"
    def companyLink(self,html):
        getHtml=GetHtml()
        selector=etree.HTML(html)
        name_link=selector.xpath('.//tr/td/div/div/div[3]/span/span/span/a/@href')
        print(name_link)
        for i in name_link:
            a=i
            print(i)
            html_com=getHtml.getHtml(i)
            phone=getHtml.companyInformation(html_com)
    def managementCompany(self,tml):
        phone=[]
        getHtml = GetHtml()
        selector = etree.HTML(html)
        com_name = selector.xpath('.//div[1]/div[2]/div/div[2]/div/div[1]/div[2]/span/span/span/span/a/@href')
        name_url=getHtml.getHtml(com_name[0])
        managementHtml=getHtml.getHtml(name_url)
        management=etree.HTML(managementHtml)
        com_url=selector.xpath('//*[@id="legallist"]/div[2]/div[2]/table/tr/td[2]/div/span[2]/span/a/@href')
        for i in com_url:
            p=getHtml.telephone(getHtml.getHtml(i))
            phone.append(p)
        return phone
    def telephone(self,html):
        getHtml = GetHtml()
        selector = etree.HTML(html)
        phone = selector.xpath('.//div[2]/div/div[2]/div/div[3]/div[1]/span/span/span[2]/text()')
        return phone[0]
    def companyInformation(self,html):
        all_com = []
        all_phone = []
        all_name = []
        all_em = []
        selector = etree.HTML(html)
        #phone=getHtml.telephone(selector)
        print(html)
        name=selector.xpath('.//div[2]/div/div[1]/div[2]/span/span/span/span/a/text()')
        com_name=selector.xpath('.//div[2]/div/div[1]/div[2]/div[1]/span/span[1]/h1/text()')
        em=selector.xpath('.//div/div[2]/div/div[3]/div[2]/span/span/span/span/text()')
        print(selector)
        print(name,em,com_name)
        all_com.append(com_name[0])
        all_name.append(name[0])
        #all_phone.append(phone)
        all_em.append(em[0])
        print(com_name,all_name,all_em)
if __name__ == '__main__':
    a=GetHtml
    url='https://www.qcc.com/web/search/risk?ps=20&ia=true&iv=1&key=《中华人民共和国消防法》&st=381&f=%7B"dt"%3A"2"%7D&pi=1'
    html=a.getHtml(a,url)
    a.companyLink(a,html)
    print(html)
    #with open('../date/date.html', encoding='utf-8') as file_obj:
        #contents = file_obj.read()
    #a.companyInformation(a,contents)
    #print(a.all_phone)
    #print(a.all_name)
  #      print(html)
 #       with open('../date/index.html', 'w', encoding='utf-8') as fp:
 #           fp.write(html)
