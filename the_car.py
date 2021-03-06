from gpiozero import Robot
import time
import sys, os
import tty, termios
from ultrasound import UltraSound
import RPi.GPIO as GPIO



def getchar():
    fd = sys.stdin.fileno()
    old_setting = termios.tcgetattr(fd)
    ch=None
    try:
        tty.setraw(sys.stdin.fileno())
        ch=sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd,termios.TCSANOW,old_setting)
    return ch

try:
    us = UltraSound(6,12)
    robot = Robot(left=(23,22),right=(17,18))
    speed=1.0

    while True:
        obstdistance = us.measure()
        #print(obstdistance)
        if obstdistance < 1.5:
            robot.stop()
        elif obstdistance < 15:
            speed=0.5
            robot.stop()
            robot.right(speed)
            time.sleep(0.01)
            robot.reverse()
            time.sleep(0.95)
            speed =1.0
            robot.forward(speed)
        
        #key = getchar()
        key="/"
        if key == "w":
            robot.stop()
            time.sleep(0.01)
            robot.forward(speed)
        elif key == "z":
            robot.stop()
            time.sleep(0.01)
            robot.backward(speed)
        elif key == "a":
            robot.stop()
            time.sleep(0.01)
            robot.left(speed)
        elif key == "d":
            robot.stop()
            time.sleep(0.01)
            robot.right(speed)
        elif key == " ": # space bar
            robot.stop()
        elif key == "q": # q key for quit  
            break
        else:
            #print(key)
            pass
            
    
finally:
    # Reset GPIO settings
    #GPIO.cleanup()
    pass

