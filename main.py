import machine
import time


def main():
    # read settings.json
    from lib.at_client import io_util
    ssid, password, atSign = io_util.read_settings()
    del io_util # make space in memory

    # connect to wifi
    from lib import wifi
    print('Connecting to WiFi %s...' % ssid)
    wifi.init_wlan(ssid, password)
    del ssid, password, wifi # make space in memory

    # connect and pkam authenticate into secondary
    from lib.at_client import at_client
    atClient = at_client.AtClient(atSign, writeKeys=False) # set writeKeys=False once you've wrote your keys at least once.
    atClient.pkam_authenticate(verbose=True)
    del at_client

    

    # Start of sending data
    led = machine.Pin("LED", machine.Pin.OUT)
    led.on()
    ProxSensor = machine.ADC(26)
    MotionSensor = machine.ADC(27)
    convert = 1/65535

    while True:
        readprox = str(not(round(ProxSensor.read_u16()*convert)))
        print(f"Proximity: " , readprox)
        readmotion = str(not(not(round(MotionSensor.read_u16()*convert))))
        print(f"Motion: " , readmotion)
        atClient.put_public("inProximity" , readprox)
        atClient.put_public("inMotion" , readmotion)

        time.sleep(0.1)

if __name__ == '__main__':
    main()