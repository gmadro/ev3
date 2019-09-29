#!/usr/bin/env python3

from time import sleep
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, SpeedPercent, MediumMotor
from ev3dev2.sensor.lego import InfraredSensor
from ev3dev2.led import Leds

rc = InfraredSensor()
mA = MediumMotor(OUTPUT_A)
mC = LargeMotor(OUTPUT_C)
mD = LargeMotor(OUTPUT_D)

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

def steer(motor, direction):
    def on_press(state):
        if state:
            motor.run_to_pos(direction)
        else:
            motor.set_pos(0)

    return on_press

rc.on_channel1_top_left = roll(mC, 'LEFT',   1)
rc.on_channel1_top_left = roll(mD, 'RIGHT',   1)
rc.on_channel1_bottom_left = roll(mC, 'LEFT',  -1)
rc.on_channel1_bottom_left = roll(mD, 'RIGHT',  -1)

rc.on_channel1_top_right = steer(mA, 1)
rc.on_channel1_bottom_right = steer(mA, -1)
print("Robot Starting")

run = True

while run:
    rc.process()
    sleep(0.01)
