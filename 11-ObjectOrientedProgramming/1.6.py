class phone():
    def __init__(self,brand,model,battery):
        self.brand = brand
        self.model = model
        self.battery = battery
        self.is_on = False

    def power_on(self):
        self.is_on = True
    def power_off(self):
        self.is_on = False
    def battery_alert(self):
        if self.battery < 20:
            print("Low battery")
    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Battery: {self.battery}%")
        if self.is_on == True:
            print("Phone is on")
            self.battery_alert()
        else:    
            print("Phone is off")

def main():

    phone1 = phone("Apple", "iPhone 13", 15)
    phone1.power_on()
    phone1.display_info()
    

if __name__ == "__main__":
    main()
                       




