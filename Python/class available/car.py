class Car:
    wheels = 4 #class variable
    

    def __init__(self,make,model,year,color):
        self.make = make  #instance variable
        self.model = model
        self.year = year
        self.color = color