#main.py

from lib.room_sensor import RoomSensor

sensor1=RoomSensor("Kitchen",31,72,180)
sensor2=RoomSensor("Bedroom",24,50,300)
sensor3=RoomSensor("Balcony",28,65,220)

sensors=[sensor1,sensor2,sensor3]

comfortable=0
normal=0
warning=0

for i in sensors:
    i.show_info()
    
    comfort=i.comfort_level()
    light=i.light_status()
    
    print(f"Comfort Level: {comfort}")
    print(f"Light Status: {light}")
    print()
    
    if comfort=="Comfortable":
        comfortable+=1
    elif comfort=="Normal":
        normal+=1
    elif comfort=="Warning":
        warning+=1
        
print(f"Comfortable: {comfortable}")
print(f"Normal: {normal}")
print(f"Warning: {warning}")
