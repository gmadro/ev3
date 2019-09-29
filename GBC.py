#!/usr/bin/env python3

from time import sleep
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, SpeedRPM, MediumMotor, MoveTank
from ev3dev2.led import Leds

mA = MediumMotor(OUTPUT_A)
mB = MediumMotor(OUTPUT_B)
m2 = MoveTank(OUTPUT_A, OUTPUT_B)

leds = Leds()
leds.all_off()

print("Robot Starting")

#mA.on_for_seconds(SpeedRPM(100), 10)
#mB.on_for_seconds(SpeedRPM(100), 10)
m2.on(SpeedRPM(100))
