from urldownloader import download
import time
'''
url从urllist文本文件中读取，对每一个url执行下载
'''
filepath = 'urllist.txt'
i = 0
urllist = open(filepath,'rb').readlines()
with open(filepath,'r') as f:
    for url in f.readlines():
        #去掉url最后添加的换行符
        url = url.rstrip('\n')
        #print(url)
        i=i+1
        outpath = ".\downloadfile\\" + str(i) + '.jpg'
        download(url,outpath)

