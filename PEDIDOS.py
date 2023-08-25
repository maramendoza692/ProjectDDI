import time
import network 
from umqtt.simple import MQTTClient
from machine import Pin, I2C, ADC, PWM
import ssd1306
import ujson

# ESP32 Pin assignment 
i2c = I2C(0, scl=Pin(22), sda=Pin(21))

VIBRA_PIN = 23
# Configuración del servomotor
SERVO_PIN = 18
servo = PWM(Pin(SERVO_PIN), freq=50)
servo_min_duty = 20
servo_max_duty = 125
servo_off_duty = 0

vibrator_pin = Pin(VIBRA_PIN, Pin.OUT) 
vibrator_pin.off()

# Configuración del sensor de sonido KY-038
SOUND_PIN = 32  
sound_sensor = ADC(Pin(SOUND_PIN))
THRESHOLD = 100  


oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

#Hacemos las configuraciones de MQTT
MQTT_BROKER = "192.168.137.147"
MQTT_USER = ""
MQTT_PASSWORD = ""
MQTT_CLIENT_ID = ""
MQTT_TOPIC_1 = "pedidos"
MQTT_PORT = 1883

#Función para conectar a la red wifi
def wifi_connect():
    print("Connecting...", end="")
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect('TUFLL9255', '272@Hu22')

    while not sta_if.isconnected():
        print(".", end="")
        time.sleep(0.5)
    print("Wifi connection!")

wifi_connect()

# Función para activar el vibrador
def activate_vibrator():
    vibrator_pin.on() 
    time.sleep(5)    
    vibrator_pin.off()
    
# Función para mover el servomotor (ventilador)
def start_fan():
    servo.duty(servo_max_duty)

def stop_fan():
    servo.duty(servo_off_duty)

# Función para detectar el sonido
def detect_sound():
    return sound_sensor.read() > THRESHOLD


# SUBCRIPCION
def message_arrived(topic, msg):
    try:
        data = ujson.loads(msg.decode())  # Decodificar el mensaje JSON
        activate_vibrator() 
        oled.fill(0)  
        oled.text("PEDIDOS", 0, 0)

        # Obtener los tres últimos pedidos o menos si hay menos de tres
        last_three_pedidos = data[-3:]
        row = 20
        for pedido in last_three_pedidos:
            pedido_str = "{}".format(pedido['pedido'])
            oled.text(pedido_str, 0, row)
            row += 10

        oled.show()
    except Exception as e:
        print("Error processing message:", e)
  
        
client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, port=MQTT_PORT, user=MQTT_USER, password=MQTT_PASSWORD, keepalive=30)
client.set_callback(message_arrived)
client.connect()
client.subscribe(MQTT_TOPIC_1)

while True:
    client.wait_msg()
    client.check_msg()
    
    sound_value = sound_sensor.read()
    print(sound_value)
    
    # Detectar el sonido y encender el ventilador si es necesario
    if sound_value > THRESHOLD:
        start_fan()
    else:
        stop_fan()
        
   

