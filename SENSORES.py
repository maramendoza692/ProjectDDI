import machine
import time

#módulos de mqtt
import network 
from umqtt.simple import MQTTClient

#configuración mqtt
MQTT_BROKER = "192.168.137.147"
MQTT_USER = ""
MQTT_PASSWORD = ""
MQTT_CLIENT_ID = ""
MQTT_TOPIC_1 = "gas"
MQTT_TOPIC_2 = "temperatura"
MQTT_PORT = 1883

#Conexión a red wifi
def wifi_connect():
    print("Connecting...", end ="")

    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect('TUFLL9255', '272@Hu22')

    while not sta_if.isconnected():
        print(".", end = "")
        time.sleep(0.3)
    print("Wifi connection!")

# Configuración del pin del sensor de llama
FLAME_PIN = 21
flame_sensor = machine.Pin(FLAME_PIN, machine.Pin.IN)

# Configuración del pin del buzzer
BUZZER_PIN = 18
buzzer = machine.Pin(BUZZER_PIN, machine.Pin.OUT)

# Configuración del pin del sensor de gas MQ-5
MQ5_PIN = 33
mq5_sensor = machine.ADC(machine.Pin(MQ5_PIN))
mq5_sensor.atten(machine.ADC.ATTN_11DB)


# Configuración del pin del LED para sensor gas
LED_PIN = 14
led = machine.Pin(LED_PIN, machine.Pin.OUT)


# Configura el pin GPIO donde está conectado el sensor de temperatura
pin_sensor = machine.Pin(34, machine.Pin.IN)  # Por ejemplo, se usa el pin GPIO 34

# Configura el pin GPIO donde está conectado el LED
pin_led = machine.Pin(2, machine.Pin.OUT)  # Por ejemplo, se usa el pin GPIO 2
 
# Umbral de valor del sensor para encender el LED
UMBRAL_SENSOR = 1500

#Función para obtener el valor del sensor de gas MQ-5
def read_mq5():
    value = mq5_sensor.read()
    gas_value = value  # Mover esta línea antes de "return value"
    if gas_value >= UMBRAL_SENSOR:
        led.on()
    else:
        led.off()
    time.sleep(1)
    print("Valor del sensor de gas MQ-5:", gas_value)
    
    return gas_value 
    
#Función mqtt flama
def check_flame():
    if flame_sensor.value() == 0:
        print("¡Flama detectada!")
        buzzer.on()
        time.sleep(1)
    else:
        print("No se detecta flama.")
        buzzer.off()
        time.sleep(1)

def temperatura():
    # Lee el valor analógico del sensor de temperatura LM35
    sensor_value = machine.ADC(pin_sensor)
    voltage = sensor_value.read() * 2.8/ 8000  # Conversión a voltaje

    # Realiza la conversión a grados Celsius
    temperature = voltage * 100

    # Imprime la temperatura en grados Celsius
    print("Temperatura: {:.2f}°C".format(temperature))

    # Si la temperatura es mayor a 36 grados Celsius, enciende el LED
    if temperature > 36:
        pin_led.value(1)  # Encender el LED
    else:
        pin_led.value(0)  # Apagar el LED
    
    return temperature
    # Espera un segundo antes de tomar la siguiente lectura
    time.sleep(1)

#Función de publicado al topic 1
def publish_gas():
    gas_value = read_mq5()  # Obtener el valor actualizado del sensor de gas
    client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, port=MQTT_PORT, user=MQTT_USER, password=MQTT_PASSWORD, keepalive=30)
    client.connect()
    client.publish(MQTT_TOPIC_1, str(gas_value))
    time.sleep(1)
    client.disconnect()

def publish_temperatura():
    temperatura_value = temperatura()
    client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, port=MQTT_PORT, user=MQTT_USER, password=MQTT_PASSWORD, keepalive=30)
    client.connect()
    client.publish(MQTT_TOPIC_2, str(temperatura_value))
    time.sleep(1)
    client.disconnect()



#Establece conexión
wifi_connect()

while True:
    try:
        check_flame()
        publish_gas()
        publish_temperatura()  
        time.sleep(1)
    except OSError as e:
        if e.args[0] == 23:
            print("Operación bloqueada temporalmente, reintentando en 1 segundo...")
            time.sleep(1)
        else:
            print("Error:", e)
