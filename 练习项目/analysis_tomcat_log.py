import re
"""
公司的tomcat日志
日志格式：pattern=%h,%l,%u,%t,%T,"%r",%s,%b,%{Referer}i,"%{User-Agent}i",%{X-Requested-With}i,%{passport}c
"""
# 读取tomcat的日志
# with open('tomcat_log/localhost_access_log.2019-01-23.txt') as f:
#     while True:
#         line = f.readline()
#         if not line:
#             break
#         print(line)

with open('tomcat_log/localhost_access_log.2019-01-23.txt') as f:
    line = f.readline()
    searchObj = re.search('(?P<ip>.*?),.*?,.*?,(?P<time>.*?),(?P<htime>.*?),"(?P<resource>.*?)",(?P<response_code>.*?),(?P<bytes>.*?),(?P<refer>.*?),"(?P<user_agent>.*?)",(?P<X_Requested_With>.*?),(?P<passport>.*)', line)
    print(searchObj.groupdict())
