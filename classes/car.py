class Car:
    make = "Toyota"
    def __init__(self,color,model,speed):
        self.color = color
        self.model = model
        self.speed = speed

    def accelerate(self):
        return f"The acceleration of {self.model} is {self.speed}"

    def start_engine(self):
        return f"The engine of {self.make} is Single engine"
    
    def hired_car(self):
        return f"John hired {self.make} {self.model} of speed {self.speed}.Its colour is {self.color}"

    def acceleration(self,initial_speed,final_spedd,time):
        acceleration=(final_spedd-initial_speed)/time
        return f"the acceleration of the car is {acceleration}m/s2"




        


    

