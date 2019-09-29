#!/usr/bin/env python3

from time import sleep
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, SpeedPercent, MediumMotor
from ev3dev2.led import Leds

mA = MediumMotor(OUTPUT_A)
mB = MediumMotor(OUTPUT_B)

leds = Leds()
leds.all_off()

print("Robot Starting")

mA.on_for_rotations(SpeedPercent(50, 10)
mB.on_for_rotations(SpeedPercent(50, 10)
