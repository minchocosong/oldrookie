from datetime import datetime, timedelta

start = datetime.strptime("1964-10-10","%Y-%m-%d")
end = datetime.strptime("2020-07-24","%Y-%m-%d")
step = timedelta(days=1) #  시간 간격 더하기 days = 1 


while start<=end:
    day = bin(int(start.strptime("%Y%m%d"))).replace("0b","")
    if day == day[::-1] :
        print (start.strftime("%Y-%m-%d"))
    start + = step

# 