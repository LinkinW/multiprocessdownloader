'''
htmelpaser
'''
from urllib.request import urlopen
from bs4 import BeautifulSoup
class main():
    print('haha ')
    name = None
    try:
        html = urlopen('https://www.zhihu.com/question/22232528')
    except HTTPError as e:
        if html is None:
            print('URL不存在')
    else:
        bsObj = BeautifulSoup(html.read().decode('utf-8'),'html.parser')
        nameList = bsObj.findAll('img')
        f = open('urllist.txt','w')
        for name in nameList:
            #print(name.get('src2'))
            f.write(str(name.get('src')) + '\n')
        f.close()
        import urlfinder
            