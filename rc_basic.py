from ev3dev.auto import *

mA = Motor(OUTPUT_A)
mB = Motor(OUTPUT_B)
mC = Motor(OUTPUT_C)
mD = Motor(OUTPUT_D)

mC.run_timed(time_sp=3000, speed_sp=500)
mD.run_timed(time_sp=3000, speed_sp=500)