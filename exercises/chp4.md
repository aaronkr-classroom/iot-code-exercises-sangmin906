# chp3 연습문제
6. 다음 정보를 참조해 dictionary 자료형의 변수를 표현하세요.
   - 2개의 센서가 있습니다.
   - 첫 번째 센서의 이름은 'dht11'이고 'temperature'와 'humidity' 값으로 23과 47을 나타냅니다.
   - 첫 번째 센서의 온도 표현 방식('unit')은 섭씨 ('celsius')입니다.
   - 두 번째 센서의 이름은 'bh1750'인데 조도 값으로 450을 나타냅니다.
   - 두 번째 센서의 측정 단위는 룩스('lux')입니다.
   - 다음과 같은 형식으로 표현합니다. sensors={'dht11':{중략},중략}

- hw 3_6_code
- sensors={
-     'dht11':{
-         'temperature':{'value':23,'unit':'celsius'},
-         'humidity':47
-         },
-     'bh1750':{'value':45, 'unit':'lux'}
-     }
- print(sensors)
   

# chp4 연습문제
2. 다음 내용을 하나의 조건식으로 만드세요.
   - 홀수 달의 15일 또는 짝수 달의 16일이면 "그날"을 출력함.
   - 8월 15일이면 "광복절"을 출력함.
   - 그 외는 "평일"을 출력함.
   - 변수는 month와 day를 사용함.

- hw 4_2
- month=[1,2,3,4,5,6,7,8,9,10,11,12]
- day=[
-     1,2,3,4,5,6,7,8,9,10,
-     11,12,13,14,15,16,17,18,19,20,
-     21,22,23,24,25,26,27,28,29,30,31
-     ]
- for m in month:
-     print(f"{m}월")
-     for d in day:
-         if (m==8 and d==15): #광복절인 경우
-             print(f"{d}일 광복절")
-             continue
-         if m%2==1: #홀수 달인 경우
-             if d==15:
-                 print(f"{d}일 그날")
-             else:
-                 if (m>=9 and d==31): #9월 이전:31일까지, 9월 이후:30일까지
-                     break
-                 print(f"{d}일 평일")
-         else: #짝수 달인 경우
-             if (m==2 and d==29): #2월 말은 올해 기준으로 28일까지 존재
-                 break
-             elif d==16:
-                 print(f"{d}일 그날")
-             else:
-                 if (m<=6 and d==31): #6월 이전:30일까지, 9월 이후:31일까지
-                     break
-                 print(f"{d}일 평일")

   
3. for 문을 이용해 1~50의 짝수 합을 구하되, 3의 배수는 제외하세요.
- hw 4_3
- sum=0
- for i in range(1,51):
-     if i%3==0:
-         continue
-     if i%2==0:
-         sum+=i
- print(sum)

   
4. 연습문제 4.3을 while 문으로 해결하세요.
- hw 4_4
- sum=0
- i=0
- while(i<50):
-     i+=1
-     if i%3==0:
-         continue
-     if i%2==0:
-         sum+=i
- print(sum)
