from gpiozero import Robot
import time
import sys
import tty, termios
from ultrasound import UltraSound
import RPi.GPIO as GPIO



def getchar():
    fd = sys.stdin.fileno()
    old_setting = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch=sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN,old_setting)
    return ch

try:
    us = UltraSound(6,12)
    robot = Robot(left=(23,22),right=(17,18))
    speed=1.0

    while True:
    
        key = getchar()
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
            print(key)
finally:
    # Reset GPIO settings
    GPIO.cleanup()

