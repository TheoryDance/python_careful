import datetime
day = '2018-12-12'
days = []
n = 0
while True:
    days.append(day)
    day = datetime.datetime.strptime(day, '%Y-%m-%d')
    day = day + datetime.timedelta(days=1)
    day = day.strftime('%Y-%m-%d')
    n = n + 1
    if n >= 27:
        break
print(days)

sql = "select count from data_${day} where 1 =1 "
for day in days:
    print(sql.replace('${day}', day))






