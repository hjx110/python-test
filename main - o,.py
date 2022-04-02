from machine import Pin
import utime
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
do_connect()
led = Pin(2, Pin.OUT)
# led.value(1)
for i in range(1000):
    utime.sleep_ms(500)
    pass
#     # 点亮LED
    led.value(1)
#     # 延时 500ms
    print('亮')
    utime.sleep_ms(500)
#     # 关闭LED
    led.value(0)
#     # 延时500ms
    print('灭')
    utime.sleep_ms(500)