#!/usr/bin/env python3

from time import sleep
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, SpeedRPM, MediumMotor
from ev3dev2.led import Leds

mA = MediumMotor(OUTPUT_A)
mB = MediumMotor(OUTPUT_B)

leds = Leds()
leds.all_off()

print("Robot Starting")

mA.on(SpeedRPM(100))
mB.on(SpeedRPM(100))
