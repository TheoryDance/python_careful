path = 'http://139.159.246.121:22816/20190108/594569434/'

import re
from urllib.request import urlopen
for line in urlopen(path):
    line = line.decode('utf-8')  # Decoding the binary data to text.
    imglist = re.findall('<tt>(.*?)</tt>', line)
    for imgpath in imglist:
        try:
            f = open('d:/'+'594569434/'+imgpath, 'wb')
            for data in urlopen(path + imgpath):
                f.write(data)
            f.close()
        except:
            print('download pic is error!')
