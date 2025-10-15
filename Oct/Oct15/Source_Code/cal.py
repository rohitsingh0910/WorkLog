import calendar
mm,dd,yyyy=list(map(int,input().strip().split()))
a=calendar.weekday(yyyy,mm,dd)
lis=["MONDAY","TUESDAY","WEDNESDAY","THURSDAY",'FRIDAY',"SATURDAY","SUNDAY"]
print(lis[a])

