import time
import datetime

PERIODS = ["300","900","1800","7200","14400","86400"]
DURATIONS_IN_DAYS = [7,30,60,90,180]

end_month = 12
end_day = 30

duration_index = 1

START_DAY = 1
START_MONTH = 1
START_YEAR = 2017


today = datetime.date.today() - datetime.timedelta(days=DURATIONS_IN_DAYS[duration_index])
today = today.strftime("%d%m%Y")
# current_day,current_month,current_year = list(map(int,[today[:2],today[2:4],today[4:]]))
till_day,till_month,till_year = list(map(int,[today[:2],today[2:4],today[4:]]))

for year in range(START_YEAR,till_year+1):
    if year == till_year:
        end_month = till_month
        print(end_month)
        end_day = till_day
        print(end_day)
    for month in range(START_MONTH,end_month+1):
        for day in range(START_DAY,end_day+1):
            print(day,month,year)

# time.mktime(datetime.datetime.strptime(s, "%d/%m/%Y").timetuple())
