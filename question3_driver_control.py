#This is a program that extends a class and adds more functionality to the derived class
class DriverControl:
    def __init__(self):
        pass
    def drive(self):
        pass
#create a class UserControl that is derived from the main DriverControl class
class UserControl(DriverControl):
    def __init__(self):
        DriverControl.__init__(self)  #instantiate the class 

    def eco_driving(self):     #add other methods eco_driving,sport_driving and off_road_driving
        pass

    def sport_driving(self):
        pass

    def off_road_driving(self):
        pass

#Test that object formed from the UserControl class has the drive method
car=UserControl()
car.drive()

