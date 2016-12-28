'''
用urllib下载远程url中的文件
'''
from urllib.request import urlretrieve
from urllib.request import urlopen

def download(url, filename):
    
    def cbk(a,b,c):
        '''
        显示下载进度的函数
        a:已经下载的数据块
        b:数据块的大小
        c:远程文件的大小
        '''
        per = 100.0 * a * b / c
        if per > 100 :
            per = 100
        print('%.2f%%' % per)
        
    print('正在下载文件%s'%url)    
    f = urlretrieve(url,filename,cbk)
    

if __name__ == '__main__':

    download('''
http://www.2cto.com/uploadfile/Collfiles/20140227/20140227084510351.png
''','1.png')
    
    
