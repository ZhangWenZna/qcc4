from lxml import etree
class RiskData():
    def riskDaata(html):
        selector=etree.HTML(html)
        com_name=selector.xpath('/html/body/div/div[2]/div[2]/div/div/div[1]/div[2]/div/div[2]/div/div[3]/div[1]/span/span/span[2]')
        print(com_name)
        for i in com_name:
            print(i)
    if __name__ == '__main__':
        with open('../date/com.html', encoding='utf-8') as file_obj:
            contents = file_obj.read()
        riskDaata(contents)