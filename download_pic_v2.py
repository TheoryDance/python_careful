import re
import os
import time
import queue
import threading
from urllib.request import urlopen

path = 'http://139.159.246.121:22816/20190108/594569434/'  # 需要下载的图片目录网络路径
root_dir = 'd:/tmp/' + path.split('/')[-2] + '/'  # 图片本地存放路径
exit_flag = 0  # 程序线程结束表示，1表示退出，用于结束进程的生命
threadLock = threading.Lock()  # 线程锁
q = queue.Queue()  # 在线程中需要使用的队列

# 判断默认存放的位置目录是否存在，不存在就创建目录
if not os.path.exists(root_dir):
    print('存放的目录不存在，创建目录：', root_dir)
    os.makedirs(root_dir)


class PicDownloadThread(threading.Thread):
    """图片下载线程"""
    def __init__(self, thread_id, name):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name

    def run(self):
        """线程下载图片的过程"""
        print('开启线程：' + self.name)
        while not exit_flag:
            if not q.empty():
                threadLock.acquire()
                imgpath = q.get()
                threadLock.release()
                try:
                    f = open(root_dir + imgpath, 'wb')
                    for data in urlopen(path + imgpath):
                        f.write(data)
                    f.close()
                except Exception as e:
                    print(e)
            else:
                time.sleep(1)
        else:
            print('线程ID：', self.thread_id, '，name='+self.name+'线程退出')

# 启动6个图片下载线程进行下载
threadList = []
for i in range(6):
    tmp = PicDownloadThread(i, 'picDownloadThread'+str(i))
    tmp.start()

stime = time.clock()  # 记录程序开始执行的时间，用于测试下载用时
print('正在打开网页地址' + path + ', stime=', stime)
imglist = []
for line in urlopen(path):
    line = line.decode('utf-8')  # Decoding the binary data to text.
    # 使用正则表达式，提取需要下载的图片路径
    tmp_list = re.findall('<a href=[\"\'](.*?\.jpg)[\"\']', line)
    imglist.extend([x.split('/')[-1] for x in tmp_list])  # 把所有需要下载的图片都存放到列表中

total = len(imglist)
print('需要下载的图片总张数：{}'.format(total))
threadLock.acquire()
for imgpath in imglist:
    q.put(imgpath)
threadLock.release()

# 一直等待，直到下载完成
while q.qsize() > 0:
    down_num = total-q.qsize()
    etime = time.clock()
    cast = int(etime-stime)
    print('下载图片张数:{0},进度:{1:.2f}%,耗时:{2}分{3}秒'.format(down_num, down_num*100/total, cast//60, cast%60))
    time.sleep(10)

# 设置线程结束标志，各个线程自动结束
exit_flag = 1
time.sleep(2)
