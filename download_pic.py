import re
import time
import queue
import threading
from urllib.request import urlopen

path = 'http://139.159.246.121:22816/20190108/594569434/'
equ = path.split('/')[-2]
exit_flag = 0
threadLock = threading.Lock()
q = queue.Queue()


class PicDownloadThread(threading.Thread):
    def __init__(self, thread_id, name):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name

    def run(self):
        print('开启线程：' + self.name)
        while not exit_flag:
            if not q.empty():
                threadLock.acquire()
                imgpath = q.get()
                threadLock.release()
                try:
                    f = open('d:/tmp/' + equ + '/' + imgpath, 'wb')
                    for data in urlopen(path + imgpath):
                        f.write(data)
                    f.close()
                except Exception as e:
                    print(e)
            else:
                time.sleep(1)
        else:
            print('线程ID：', self.thread_id, '，name='+self.name+'线程退出')

threadList = []
for i in range(6):
    tmp = PicDownloadThread(i, 'picDownloadThread'+str(i))
    tmp.start()

stime = time.clock()
print('正在打开网页地址' + path + ', stime=', stime)
for line in urlopen(path):
    line = line.decode('utf-8')  # Decoding the binary data to text.
    imglist = re.findall('<a href=[\"\'](.*?\.jpg)[\"\']', line)
    while True:
        if q.qsize() < 100:
            threadLock.acquire()
            for ss in imglist:
                print(ss)
                imgpath = ss.split('/')[-1]
                q.put(imgpath)
            threadLock.release()
            break
        else:
            time.sleep(1)

while q.qsize() > 0:
    time.sleep(5)

exit_flag = 1
etime = time.clock()
print('程序用时{}s'.format(etime - stime))