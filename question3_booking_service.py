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

    def eco_driving(self):     #add other methods
        pass

    def sport_driving(self):
        pass

    def off_road_driving(self):
        pass

