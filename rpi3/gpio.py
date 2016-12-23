import pigpio
from math import sin
from time import sleep

pi = pigpio.pi()

def px(x,y):
    pi.set_PWM_dutycycle(x,y)

x = 0.05

while True:
    px(17,0)
    sleep(x)
    px(17,255)
    sleep(x)
