from machine import Pin
import utime
import dht

# import bluetooth

# bt = bluetooth.Bluetooth()
# bluetooth
# bt.active(1)
# bt.advertise(100, 'ESP32_BLE_01')

def do_connect():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('HJX', 'mylink159')
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())
# 声明一个LED对象 （P2）
# do_connect()
mydht = dht.DHT22(Pin(2))

# 声明一个LED对象 （P2）

'''
声明一个LED对象 （P2）

'''







for i in range(100000):
    try:
        mydht.measure()
    except Exception as e:
        print('=============Error==========:',e)
    # wdt.feed()
    temperature = mydht.temperature()
    humidity = mydht.humidity()
    print(i,':',temperature,humidity)
    # print(humidity)
    utime.sleep_ms(10)