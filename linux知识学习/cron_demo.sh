linux系统由cron(crond)这个系统服务来控制的，linux系统上原来有非常多的计划性工作，因此，这个系统服务是默认启动的。
cron进程每分钟会定期检查是否有要执行的任务，如果有就自动执行该任务。
/etc/crontab
参考博客：https://www.cnblogs.com/intval/p/5763929.html
用户编写的任务，存放在/var/spool/cron/[user]中
minute hour day month week command
$ crontab -e            # 进行编辑
$ crontab -l            # 显示当前任务的详细就是/var/spool/cron/[user]文件中的内容
$ crontab -r            # 从/var/spool/cron/中删除用户的crontab文件
$ service crond start   # 启动
$ service crond stop    # 停止
$ service crond restart # 重启
$ service crond reload  # 重新加载
$ service crond status  # 状态

在ubuntu中，服务不是crond而是cron,使用crontab -e修改了内容，不需要重启之类的，会自动生效
需要注意的是环境变量和加载文件的问题，
比如我想每分钟记录一下当前时间到一个文件：
方式一：使用crontab -e进行修改如下，不会记录出来，应该是跟bash的加载方式有关
*/1 * * * * echo `date +"%Y-%m-%d %H:%M:%S"` >> /home/master/environment/run_records.log

方式二：可行
*/1 * * * * sh /home/master/environment/record.sh
record.sh内容
#！/bin/bash
echo `date +"%Y-%m-%d %H:%M:%S"` >> /home/master/environment/run_records.log