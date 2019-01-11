import re

site = 'www.runoob.com'
print(re.match('www',  site).span())
print(re.match('com', site))
print('-------------------------------------')

line = 'Cats are smarter than dogs'
matchObj = re.match(r'(.*) are (.*?) .*', line, re.M|re.I)
if matchObj:
    print('matchObj.group(): ', matchObj.group())
    print('matchObj.group(1): ', matchObj.group(1))
    print('matchObj.group(2): ', matchObj.group(2))
else:
    print('No match!')
searchObj = re.search('(?P<value>runoob)', site)
print(searchObj)