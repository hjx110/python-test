# This file is executed on every boot (including wake-boot from deepsleep)
# import esp
#esp.osdebug(None)
from machine import Pin
import network
import uos, machine
#uos.dupterm(None, 1) # disable REPL on UART(0)
import gc
# import machine
machine.freq(160000000)
# IOS0= Pin(0, Pin.OUT)
# IOS0.value(0)

# led = Pin(2, Pin.OUT)
# led.value(0)
import webrepl
ap_if = network.WLAN(network.AP_IF)
ap_if.config(authmode=network.AUTH_WPA_WPA2_PSK, password="mylink159")
webrepl.start()
gc.collect()