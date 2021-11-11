
import base64
from lxml import etree
import requests
for pages in range(1,5): #页数
    url = 'https://fofa.so/result?qbase64='
    search_data = ''
    search_data_bs = str(base64.b64encode(search_data.encode('utf-8')),'utf-8')  #py3中默认字符为unicode编码，而base64函数的参数为byte类型，所以必须先转码
    fofa_url = url + search_data_bs + '&page=' + str(pages) + '&page_size=10'
    header = {
        'User-Agent':
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:93.0) Gecko/20100101 Firefox/93.0',
        'Cookie':
            '',
    response = requests.get(fofa_url,headers=header).text
    soup =  etree.HTML(response) 
    url_data = soup.xpath('//span[@class="aSpan"]/a[@target="_blank"]/@href')  
    title_name = soup.xpath('//div[@class="rightListsMain"]//div[@class="contentLeft"]/p[@class="max-tow-row"]/text()')
    for i in range(len(url_data)):
        with open('your_file.txt','a+') as f:
            f.write(url_data[i])
            f.write('---' + str(title_name[i]).strip('\n').strip(' ') + '\n')
    f.close()
print('搜索完毕')



