import machine, time

ProxSensor = machine.ADC(26)
MotionSensor = machine.ADC(27)
convert = 1/65535

while True:
    
    readprox = str(not(round(ProxSensor.read_u16()*convert)))
    print(f"Proximity: " , readprox)
    readmotion = str(not(not(round(MotionSensor.read_u16()*convert))))
    print(f"Motion: " , readmotion)

    time.sleep(0.1)