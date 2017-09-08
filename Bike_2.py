class Bike():
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def __str__(self):
        return "Price: {}, Max Speed:{}, Miles: {}".format(self.price, self.max_speed, self.miles)
    def displayInfo(self):
        print self.__str__()
        return self
    def ride(self):
        print "Riding"
        self.miles += 10
        return self
    def reverse(self):
        print "Reversing"
        self.miles -= 5
        if self.miles < 0:
            self.miles = 0
        return self


One = Bike(1000, "90 mph")
One.ride().ride().ride().reverse().displayInfo()

Two = Bike(1000, "90 mph")
Two.ride().reverse().reverse().reverse().displayInfo()
