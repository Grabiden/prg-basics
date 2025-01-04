import random
#print(random.randint(34, 42))
class thermometer():
    def __init__(self,):
        self.temperature = 0
        self.status = False
    
    def power_on(self):
        self.status = True
        print("Thermometer is on")

    def power_off(self):
        self.status = False
        print("Thermometer is off")

    def measure_temperature(self):
        self.temperature = round(random.uniform(34, 42),1)    

    def fever(self):
        if self.status == True:
            if self.temperature >= 37:
               print(f"Temperature: {self.temperature} (fever)")
            else:
               print(f"Temperature: {self.temperature}") 
        else:
            print("Turn on the thermometer")       
    
def main():
    
    termometr = thermometer()
    termometr.power_on()
    termometr.measure_temperature()
    termometr.fever()
    termometr.power_off()

main()    