from controller import Robot
from controller import Motor
from controller import Altimeter
import math

class MyController(Robot):
    def __init__(self):
        super(MyController, self).__init__()
        self.timeStep = 32 

        
        self.distanceSensor = self.getDevice('ds0')     
        self.distanceSensor.enable(self.timeStep)  # enable sensors to read data from them
        
        self.altimeter=self.getDevice("altimeter")
        self.altimeter.enable(self.timeStep)     
                
         
        self.left_motor = self.getDevice("left wheel motor")
        self.right_motor = self.getDevice("right wheel motor")
        self.left_motor.setPosition(math.inf)
        self.right_motor.setPosition(math.inf)
        
        
        self.left_motor.setVelocity(0.5)
        self.right_motor.setVelocity(-0.5)
        self.direction_switch = True

        self.front_led = self.getDevice("front_led")
        self.back_led = self.getDevice("back_led")
        self.left_led = self.getDevice("left_led")
        self.right_led = self.getDevice("right_led")

        self.altValues=[]


    def run(self):
            
        while self.step(self.timeStep) != -1:
           

            for i in range(3):
                 self.altValues.append(self.altimeter.getValue())    


            if (abs(self.altValues[1]) > abs(self.altValues[0])):
                self.front_led.set(False)
                self.back_led.set(False)
                self.left_led.set(self.altValues[1] > 0.0)
                self.right_led.set(self.altValues[1] < 0.0)
            else:
                self.front_led.set(self.altValues[0] <0.0)
                self.back_led.set(self.altValues[0] > 0.0)
                self.left_led.set(False)
                self.right_led.set(False)

            
            self.altValues=[]


controller = MyController()
controller.run()