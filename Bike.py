# Assignment: Bike
# Create a new class called Bike with the following properties/attributes:
#
# price
# max_speed
# miles
# Create 3 instances of the Bike class.
#
# Use the __init__() function to specify the price and max_speed of each
# instance (e.g. bike1 = Bike(200, "25mph");
# In the __init__() also write the code so that the initial miles is set to be 0
# whenever a new instance is created.
#
# Add the following functions to this class:
# displayInfo() - have this method display the bike's price, maximum speed, and the total miles.
# ride() - have it display "Riding" on the screen and increase the total miles ridden by 10
# reverse() - have it display "Reversing" on the screen and decrease the total miles ridden by 5...
#
# Have the first instance ride three times, reverse once and have it displayInfo().
# Have the second instance ride twice, reverse twice and have it displayInfo().
# Have the third instance reverse three times and displayInfo().
#
# What would you do to prevent the instance from having negative miles?
#
# Which methods can return self in order to allow chaining methods?

class Bike:
    def __init__(self, price, maxSpeed):
        self.price = price
        self.maxSpeed = maxSpeed
        self.miles = 0;
    def displayInfo(self):
        print "  $:{0}  Max Speed: {1} mph  Odometer: {2} miles".format(self.price, self.maxSpeed, self.miles)
        return self;
    def ride(self):
        self.miles += 10
        print "  Riding"
        # print "         {0}".format(self.miles)
        return self;
    def reverse(self):
        self.miles -= 5
        if (self.miles < 0):
            self.miles = 0
        print "  Reversing"
        # print "         {0}".format(self.miles)
        return self

Bike_One   = Bike(1200, 150)
Bike_One.ride().ride().ride().reverse().displayInfo()

Bike_Two   = Bike(200, 50)
Bike_Two.ride().ride().reverse().reverse().displayInfo()

Bike_Three = Bike(20, 10)
Bike_Three.reverse().reverse().reverse().displayInfo()
