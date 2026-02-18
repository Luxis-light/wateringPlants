# Automatisierung von Bewässerung von Pflanzen



## Beschreibung
Die Idee ist die, dass man Pflanzen, ohne auf diese zu achten, automatisiert bewässern kann.
Die Feuchtigkeit der Erde sowie Raumtemperatur und Luftfeuchtigkeit werden an **Node-RED** weiterversendet und Informationen werden auf einer **InfluxDB** abgespeichert. Außerdem bekommt man eine Benachrichtigung via Telegram, dass die Pflanzen bewässert werden.

## Benötigte Hardware

- [ ] 1 x **ESP32** (stand jetzt werde ich nur einen verwenden für alle Pflanzen)
- [ ] 1 x **Raspberry Pi** (Darauf läuft Node-RED und InfluxDB. Man kann das auch auf einem "normalen" PC, aber der muss im Dauerbetrieb sein, um die Datenbank aufrechtzuerhalten)
- [ ] 1 x **DHT22** (DHT22 ist der Beste)
- [ ] 2 x **Kapazitiver Bodenfeuchtigkeitssensor**
- [ ] 2 x **Wasserpumpe**
- [ ] 2 x **Relaismodul**
- [ ] 2 x **2 Meter Schlauch**
- [ ] ca. 10 x **Jumper Wires**
- [ ] 1 x **[Akku](https://amzn.eu/d/0cpPDY9M)**

## Verwendete Technologien

- [MicroPython](https://docs.micropython.org/en/latest/)
- [Node-RED](https://nodered.org/)
- [MQTT](https://mqtt.org/)
- [InfluxDB](https://www.influxdata.com/)
- [Telegram Bot API](https://core.telegram.org/bots/api)
- [Eclipse Mosquitto](https://mosquitto.org/)

## Grober Ablauf und Verwendung

Ich benutze Thonny als IDE und schreibe den Algorithmus, um einmal die Pflanzen zu gießen bei niedriger Feuchtigkeit.
Via MQTT wird es dann an den Raspberry Pi gesendet (für eine genauere Erklärung wie das funktioniert -> [MQTT](https://mqtt.org/)).
Auf dem Raspberry Pi läuft Node-RED und dieser versendet die Daten einmal auf InfluxDB und nochmal als Benachrichtigung an den Telegram Bot.


## Genauer Ablauf 
To be continued


## Fehler aus denen ich gelernt habe 
Beim Verlöten der Pumpe mit dem Akku habe ich anschließend die Kabel am Relaismodul angebracht. Dabei waren Batterien im Akkufach, von denen eine umgekehrt eingesetzt war. Was passiert ist: Zum einen wurde die Batterie 'rückwärts' geladen und fing an, Rauch zu bilden. Zum anderen entwickelte sich Hitze, welche das Gehäuse des Akkupacks geschmolzen hat.
Moral der Geschichte: **Nicht verkablen und löten wenn Strom angeschlossen ist !**

