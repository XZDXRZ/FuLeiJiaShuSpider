import requests as rq
from bs4 import BeautifulSoup

def work(it,url):
    #url = 'https://www.ppzuowen.com/book/fuleijiashu/153999.html'

    page = rq.get(url)
    #print(page.text.encode('latin1').decode('gbk'))
    html = page.text.encode('latin1').decode('gbk')
    bs = BeautifulSoup(html,'lxml')
    #print(bs.select('.articleContent'))
    word = bs.select('.articleContent')[0]
    ls = word.find_all('u')
    for i in ls:
        word.u.extract()

    #print(word.get_text())


    #--------------
    f = open('book'+str(it)+'.txt','w')
    f.write(word.get_text()[1:])
    f.close()
    #--------------