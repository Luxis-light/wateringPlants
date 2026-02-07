import network
import machine
import time

SSID = "Name des WLANs"

PASSWORD = "Passwort des WLANs"


wlan = network.WLAN()

wlan.active(True)

if not wlan.isconnected():
    print('connecting to network...')
    wlan.connect(SSID, PASSWORD)
    while not wlan.isconnected():
        print(f'Versucht verbindung aufzubauen')
        time.sleep(3)
    print('network config:', wlan.ipconfig('addr4'))
    
    

