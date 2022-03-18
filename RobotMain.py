from MotorModule import Motor
import KeyBoardModule as kb

import JoyStickModule as js
from time import sleep

#motor module
motor=Motor(2,3,4,22,27,17)

movement = "Joystick"


# Key board module
kb.init()




def main():
    if movement=="Joystick":
        jsVal=js.getJS()
        motor.move(jsVal["axis4"],jsVal["axis3"],0.1)
    else:

      if kb.getKey("UP"):
          motor.move(-0.6,0,0.1)
      elif kb.getKey("DOWN"):
          motor.move(0.6,0,0.1)
      elif kb.getKey("LEFT"):
          motor.move(-0.6,-0.5,0.1)
      elif kb.getKey("RIGHT"):
          motor.move(-0.6,0.5,0.1)
      else:
          motor.stop(0.1)

if __name__ == "__main__":
    while True:
        main()
