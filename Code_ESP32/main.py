from machine import Pin, unique_id, reset, ADC
import ubinascii
import time
import dht
from umqtt.simple import MQTTClient

# --- Konfiguration ---
MQTT_SERVER = '192.168.xxx.xxx' # IP-Adresse des MQTT-Brokers, z.B. des Raspberry Pi
MQTT_TOPIC_Erde = 'x/pflanzen/feuchtigkeit'
MQTT_TOPIC_Temp = 'x/temp'
MQTT_TOPIC_Hum = 'x/hum'


CLIENT_ID = ubinascii.hexlify(unique_id()).decode('utf-8')

#Ausgedachte Zahlen
MIN_ADC = 15000 
MAX_ADC = 45000 


#Temporäre zuteilung
Erde_SENSOR_PIN = 4
Temp_Hum_sensor = 5

Pumpen_Pin = 7


# --- MQTT Setup ---
def connect_mqtt():
    try:
        client = MQTTClient(client_id=CLIENT_ID, server=MQTT_SERVER, port=1883, keepalive=60)
        client.set_last_will(MQTT_TOPIC + "/LWT", b'Offline', retain=True) 
        client.connect()
        print('MQTT Connected')
        client.publish(MQTT_TOPIC + "/LWT", b'Online', retain=True)
        return client
    except Exception as e:
        print(f'Connection failed: {e}')
        time.sleep(5)
        reset() # Hard reset bei Initialisierungsfehler


def read_sensors():
    
    erde_raw_value = Erde_SENSOR_PIN.read_u16()
    
    erde_percentage = (MAX_ADC - erde_raw_value) / (MAX_ADC - MIN_ADC) * 100
    
    erde_percentage = max(0, min(100, erde_percentage))
    
    d = dht.DHT22(Pin(Temp_Hum_sensor))
    d.measure()
    temperatur = d.temperature() 
    feuchtigkeit = d.humidity()    
    
    return erde_percentage, temperatur , feuchtigkeit
    

def watering_plant():
    #TODO Implementieren der Logik, Digitaler Output in Digitalen verwandeln
    pass

while True:
    #TODO: Es soll gemessen werden in intervallen und dann einmal bewassert und dann gesendet werden
    try:
        client = connect_mqtt()
        erde, temp, hum = read_sensors()
        client.publish(MQTT_TOPIC_Erde, str(erde))
        client.publish(MQTT_TOPIC_Temp, str(temp))
        client.publish(MQTT_TOPIC_Hum, str(hum))
        time.sleep(60) # Intervall in Sekunden
    except Exception as e:
        print(f"Fataler Fehler: {e}")
        reset()
    finally:
        try:
            client.disconnect()
        except:
            pass
