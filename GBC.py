#!/usr/bin/env python3

from time import sleep
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, SpeedPercent, MediumMotor
from ev3dev2.led import Leds

mA = MediumMotor(OUTPUT_A)
mB = MediumMotor(OUTPUT_B)

leds = Leds()
leds.all_off()

def roll(motor, led_group, direction):
    def on_press(state):
        if state:
            motor.run_forever(speed_sp=600*direction)
            leds.set_color(led_group, 'GREEN')
        else:
            motor.stop(stop_action='brake')
            leds.all_off()
    
    return on_press

print("Robot Starting")

run = True

while run:
    roll(mA, 'LEFT', 1)
    roll(mB, 'RIGHT', 1)
