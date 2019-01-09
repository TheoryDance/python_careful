#!/usr/bin/python3
import pymysql


def execute_sql(sql):
    # 打开数据库连接
    db = pymysql.connect("139.159.234.230", "root", "Grand_403?", "p1project")

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    # 使用 execute()  方法执行 SQL 查询
    cursor.execute(sql)

    # 使用 fetchone() 方法获取单条数据.
    # data = cursor.fetchone()

    # print ("Database version : %s " % data)
    db.commit();
    print(sql, 'execute ok!')
    # 关闭数据库连接
    db.close()


sql = """
insert into region_pic_count(region_code,pic_count,date) 
select sp.region_code,count(p.id) pic_count,'${day}' date 
from view_pic_all p,sys_point sp 
where p.addtime >= '${day}' and p.addtime < DATE_ADD('${day}',INTERVAL 1 DAY) and p.point_code = sp.point_code GROUP BY sp.region_code;
"""

import datetime
day = datetime.datetime.now().strftime('%Y-%m-%d')
print(day)

# execute_sql(sql.replace('${day}', day))


