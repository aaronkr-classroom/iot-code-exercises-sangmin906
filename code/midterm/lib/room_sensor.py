#room_sensor.py

class RoomSensor:
    def __init__(self,name,temperature,humidity,light):
        self.name=name
        self.temperature=temperature
        self.humidity=humidity
        self.light=light
        
    def show_info(self):
        print(f"Sensor: {self.name}")
        print(f"Temperature: {self.temperature}")
        print(f"Humidity: {self.humidity}")
        print(f"Light: {self.light}")
        
    def comfort_level(self):
        t=self.temperature
        h=self.humidity
        if 20 <= t <= 26 and 40 <= h <= 60:
            return "Comfortable"
        elif t >= 30 or h >= 70:
            return "Warning"
        else:
            return "Normal"
        
    def light_status(self):
        l=self.light
        if l<200:
            return "Dark"
        else:
            return "Bright"