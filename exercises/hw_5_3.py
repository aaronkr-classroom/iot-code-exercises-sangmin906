#hw 5_3_code

class SayDays:
    def __init__(self,year,month,day):
        self.year=year
        self.month=month
        self.day=day
        
    def is_leap(self):
        year=self.year
        return (year%4==0 and year%100!=0)or(year%400==0)
        
    def days(self):
        if self.is_leap():
            m=[31,29,31,30,31,30,31,31,30,31,30,31]
        else:
            m=[31,28,31,30,31,30,31,31,30,31,30,31]
        return sum(m[:self.month-1])+self.day
        
    def days_left(self):
        if self.is_leap():
            total=366
        else:
            total=365
        return total-self.days()
        
    def weekday(self):
        y=self.year
        m=self.month
        d=self.day
        
        if m<3:
            m+=12
            y-=1
            
        K=y%100
        J=y//100
        
        h=(d+(13*(m+1))//5+K+K//4+J//4+5*J)%7
        
        return h
        
    def weekday_name(self):
        names=["토","일","월","화","수","목","금"]
        return names[self.weekday()]

#실행
while True:
    year,month,day=map(int,input("날짜를 입력하세요(year/month/day의 형식으로) : ").split("/"))
    if ((year+month+day)==0):
        break;
    s=SayDays(year,month,day)
    
    print(f"새해부터 D+{s.days()}")
    print(f"연말까지 D-{s.days_left()}")
    print(f"{s.weekday()}")
    print(f"오늘은 {s.weekday_name()}요일")
    print()