class TaxiRide:
    def __init__(self, rate_per_km):
        self.rate_per_km = rate_per_km # value in € (e.g. €2)
        self.distance = 0
        self.fare = 0

    def calculate_fare(self, distance):
        self.distance = distance
        self.fare = self.distance * self.rate_per_km
    def print_receipt(self):
<<<<<<< HEAD
        print(f"Distance: {self.distance} km")
        print(f"Fare: {self.distance*self.rate_per_km} €")
        print(f"rate: {self.rate_per_km}/km")
        

def main():
    # your program
    taxi1 = TaxiRide(2)
    taxi2 = TaxiRide(3)
    taxi1.rate_per_km = 2
    taxi1.distance = 10
    taxi2.distance = 10
    TaxiRide.print_receipt(taxi1)
    TaxiRide.print_receipt(taxi2)

=======
        print(self.distance * self.rate_per_km)
        print(self.rate_per_km)
        print(self.distance)

def main():
    # your program
    ride1 = TaxiRide(4)
    ride2 = TaxiRide(4)
    ride1.distance = 20
    ride2.distance = 15
    ride1.print_receipt()
    ride2.print_receipt()
    
>>>>>>> 11cd2cebed6eda48bd3f9bc9be5b72ae7019f7cf
if __name__ == "__main__":
    main()
