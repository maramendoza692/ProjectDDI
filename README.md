# TACOMANDI
## Objetivo del proyecto
Tacomandi tiene como objetivo crear un mandil diseñado específicamente para taqueros y cocineros que se enfrentan a una alta demanda de pedidos diarios. Este mandil inteligente busca proporcionar un entorno de trabajo más seguro y eficiente al alertar a los usuarios sobre situaciones potencialmente peligrosas y brindarles acceso rápido a la información de los pedidos pendientes.

## Objetivos específicos:
Mejorar la seguridad y el bienestar de los taqueros y cocineros al proporcionar alertas en tiempo real sobre situaciones peligrosas.
Optimizar la gestión de pedidos mediante una interfaz gráfica intuitiva y de fácil acceso, lo que resultará en una mayor eficiencia y satisfacción del cliente.
Reducir los desperdicios de recursos al evitar el mal uso de llaves y prevenir fugas de gas.

## Beneficiario
 - María Auxiliadora Hernández R

## Integrantes
- Pedro Emmanuel Martinez Rodriguez 
- María Guadalupe Mendoza Ramírez
- Juan Luis Negrete Labrada
- Paola Guadalupe Patlán Gónzalez


## Componentes empleados
| No. | Componente | Descripción | Img | Costo | Cantidad |
|-----|------------|-------------|-----|-------|----------|
|1|Placa de desarrollo ESP32| Placa de desarrollo ESP32 con pantalla táctil de 2.8 pulgadas. CPU de doble núcleo y una frecuencia de reloj de 240 MHz. Integra periféricos de recursos, SDO de alta velocidad, SP, UART y otras funciones, y admite la descarga automática. |<img src="https://github.com/maramendoza692/ProjectVetSafeC3000/assets/90641538/6606e7d5-c1ad-4ccd-b253-dcaa5afed3a0" width= "200px"/> |$169 | 3 |
|2| Sensor de temperatura| Modulo Ky-001 Sensor De Temperatura |<img src="https://github.com/maramendoza692/ProjectVetSafeC3000/assets/90641538/42fcd6e5-30ac-4b3a-b80c-49a1fb623dbf" width= "200px"/> |$42| 1|
|3| Buzzer| Altavoz que permite convertir una señal eléctrica en una onda de sonido |<img src="https://github.com/maramendoza692/ProjectVetSafeC3000/assets/90641538/8971c075-c206-46ee-b3ac-b7f5571011f7" width= "200px"/> |$47| 1|
|4| ESP32| Tarjeta de desarrollo ESP32 de 30 pines, trae integrado Wi-Fi, Bluetooth y BLE (Bluetooth Low Energy).|<img src="https://github.com/maramendoza692/ProjectVetSafeC3000/assets/90641538/8e9f544f-3a6d-4e98-87c7-2c9083a0b6c6" width= "200px"/>|$158| 1|
|5| Resistencias 220 Ohms| Paquete de resistencias fabricadas con una alambre conductor de una resistividad alta  |<img src="https://github.com/maramendoza692/ProjectVetSafeC3000/assets/90641538/5f5fda94-8ba5-4405-94b3-ff202b49117d" width= "200px"/> |$81| 1|
|6| Sensor de flama| Sensor De Flama |<img src="https://github.com/maramendoza692/ProjectVetSafeC3000/assets/90641538/3116347d-9819-483d-9629-1caf9c7533c0" width= "200px"/> |$49| 1|
|7| Sensor de gas| MQ-5 Detección de: Gas LP, Metano/Gas Natural, Hidrógeno, Alcohol y Humo. Alta sensibilidad al: Gas LP y Metano/Gas Natural  |<img src="https://github.com/maramendoza692/ProjectVetSafeC3000/assets/90641538/853bb66a-0be2-41f3-ac98-3dfc73e340fc" width= "200px"/> |$81| 1|
|8| Pantalla OLED ssd1606 |controlador SSD1606 permite la visualización de gráficos y texto en pantallas OLED.|<img src="https://www.winstar.com.tw/uploads/photos/graphic-oled-display/WEA012864DW-01.jpg" width= "200px"/>|$110|1
|9| Actuador Led |Un LED es un diodo emisor de luz, es decir, un tipo particular de diodo que emite luz al ser atravesado por una corriente eléctrica. Los diodos (emisor de luz, o no) son unos de los dispositivos electrónicos fundamentales.|<img src="https://github.com/maramendoza692/ProjectVetSafeC3000/assets/87044535/10874366-de68-4dee-9ea3-39ef752debf6" width="200px"/>|$ 80|2
|10| Modulo de Vibración ARD-385 |El Módulo de Vibración PWM es un dispositivo que causara efecto vibratorio cuando la entrada de PWM es alta, similar al que un teléfono celular estando en modo vibración/silencioso. Funciona en un rango de voltaje 3V a 5.3 V DC, siendo un motor de corriente continua.|<img src="https://github.com/maramendoza692/ProjectVetSafeC3000/assets/87044535/c7f7bc21-de7d-4320-884f-aeb7984cb542" width= "200px"/>|$150|1
|11| Sensor de Sonido KY-038|El modulo KY-038 es un sensor analógico y/o digital de sonido, diseñado para proyectos y circuitos elaborados con Arduino. Cuenta con un micrófono de condensador omnidireccional de alta sensibilidad, que permite detectar con precisión hasta sonidos de muy baja intensidad.|<img src="https://github.com/maramendoza692/ProjectVetSafeC3000/assets/87044535/189d82ce-1657-404d-80fb-8bc0b2f85f02" width= "200px"/>|$200|1
|12| Servomotor |Un servomotor, también conocido como servo, es un dispositivo que permite controlar con máxima precisión la posición y movimientos de su eje. |<img src="https://github.com/maramendoza692/ProjectVetSafeC3000/assets/87044535/70ba7884-7439-43b2-a8a1-fe4e8d22e2db" width= "200px"/>|$90|1


## Software utilizado
| Id | Software | Version | Tipo |Funcionalidad|
|----|----------|---------|------|-------------|
| 1 | Fritzing | 0.9.3 |Licencia libre|Modelado|
| 2 | Wokwi    | N/A | Licencia libre | Programación / Modelado|
| 3 | Node-RED | 3.0.2 | Licencia libre| Programación|
| 4 | Tinkercad | N/A |Licencia libre|Modelado 3D |
| 5 | Librería NewPing |N/A|Licencia libre|Para sensores ultrasónicos, incluyendo el HC-SR04.|
| 6 | Libreria machine|N/A|Licencia Libre| Proporciona una interfaz para interactuar con el hardware del microcontrolador|
| 7 | Libreria time | N/A | Licencia Libre| ofrece funciones para trabajar con medidas de tiempo.|
| 8 | Libreria network | N/A| Licencia Libre| permite la configuración y gestión de conexiones de red en el microcontrolador|
| 9 | Libreria umqtt | N/A| Licencia Libre| está diseñada para admitir el protocolo MQTT (Message Queuing Telemetry Transport) en entornos de MicroPython.| 

## Historias de Usuario
| Id | Historia de usuario | Prioridad | Estimación | Cómo probarlo | Responsable | Sprint |
|----|---------------------|-----------|------------|---------------|-------------|--------|
|HU01|Yo como taquero quiero que el mandil me alerte mediante un sonido cuando este se esté comenzando a incendiar, para poder tomar acciones inmediatas y que el resto de los cocineros pueda darse cuenta y ayudarme, pues siempre estoy muy ocupado y algunas veces no detecto el fuego hasta que este ya se ha extendido en la mayoría del mandil.|Debe| 1 |Se enciende una llama a 5 cm del sensor y el buzzer debe emitir un sonido|Paola Patlán|1|
|HUO2|Yo como taquero quiero que el mandil me alerte mediante una luz cuando una llave de la estufa esté abierta y se esté escapando el gas, para poder tomar medidas inmediatas y prevenir accidentes.|Debe |1 |Liberar gas de un encendedor cerca del sensor de gas para simular una fuga (posicionar cerca para que pueda reconocer el gas pues es una cantidad pequeña)y observar cómo el led rojo parpadea| Pedro Martínez |1|
|HU03|Yo como taquero quiero que el mandil me alerte mediante una luz cuando he pasado mucho tiempo frente al calor del fuego y mi temperatura es demasiado alta, para prevenir deshidratación, agotamiento por calor e incluso un golpe de calor, recordándome que es momento de tomar una bebida hidratante.|Debe|1 |Acercar un objeto con fuego como un encendedor cerca del sensor para aumentar la temperatura, observar que el led azul comeinza a parpadear| María Mendoza |1|
|HU04|Yo como mesero quiero poder enviar los pedidos desde la mesa que estoy atendiendo hasta la cocina, mediante la pantalla de mi celular, para agilizar el proceso de pedidos sin tener que ir hasta la cocina a realizar el pedido. | Debe |4| Seleccionar los botones con las opciones de los platillos y la cantidad de estos en la pantalla del celular (Por ejemplo: platillo: tacos bisteck, cantidad: 10). En seguida, presionar le boton "Enviar pedido"|Luis Negrete|2|
|HU05|Yo como taquero quiero contar con una pantalla integrada en el mandil de manera estratégica, que sea desplegable y únicamente visualizarla cuando lo necesito, para poder visualizar los pedidos pendientes por realizar.|Debe| 4 |Enviar un pedido desde el celular descrito en la HU04. Desplegar la pantalla ubicada en la parte superior del mandil. Observar el pedido en la pantalla. Regresar la pantalla a su posición inicial|Paola Patlán|2|
|HU06|Yo como taquero quiero recibir una notificación mediante vibración cada que llegue un pedido, para darme cuenta que tengo nuevos pedidos y debo presionarme, además de desplegar la pantalla y poder visualizarlo.|Debe|2|Enviar un pedido desde el celular descrito en la HU04. Sentir una vibración. Desplegar la pantalla ubicada en la parte superior del mandil. Observar el pedido en la pantalla. Regresar la pantalla a su posición inicial|Pedro Martínez|2|
|HU07|Yo como taquero quiero que por medio de aumentar el nivel de mi voz, se active un ventilador que permita refrescarme|Puede|1|Aumentar el nivel de voz un poco más de lo normal| Luis Negrete | 2


1 Punto de esfuerzo es igual a desarrollo de un Login.

## Prototipo en 3D
- Imagen de prototipo realizado en tinkercad
![image](https://github.com/maramendoza692/ProjectVetSafeC3000/assets/90641538/e43656cf-49b0-4d67-9eb5-f18bc8fd497f)

## Imagen del mandil

![image](https://github.com/maramendoza692/ProjectVetSafeC3000/assets/90641538/b0a6f4b9-dd22-407d-aa93-85275c112d46)

![image](https://github.com/maramendoza692/ProjectVetSafeC3000/assets/90641538/073e1fd1-a49c-4028-b462-22d9c36f6580)


## Aplicación web

![image](https://github.com/maramendoza692/ProjectVetSafeC3000/assets/90641538/ba913c2d-7569-4453-87ac-3e457bdbc1cc)


## Dashboard en Grafana

![image](https://github.com/maramendoza692/ProjectVetSafeC3000/assets/90641538/c0db028b-f037-44a5-986c-8c84ab44d813)


## Carta de aceptación del proyecto firmada por la beneficiaria

![image](https://github.com/maramendoza692/ProjectVetSafeC3000/assets/90641538/33b539f8-e1e3-44e1-965e-08cf0114072e)

## Vídeo de aceptación del proyecto

https://drive.google.com/drive/folders/1qVjTsDf6Mc0yx3wUxBGgX2C_--_Lmx8n?usp=drive_link 

## Código fuente

Funcionamiento de los sensores: https://github.com/maramendoza692/ProjectVetSafeC3000/blob/main/SENSORES.py                  
Funcionamiento de la oled para visualizar pedidos: https://github.com/maramendoza692/ProjectVetSafeC3000/blob/main/PEDIDOS.py        
Flow del crud de la aplicación web: https://github.com/maramendoza692/ProjectVetSafeC3000/blob/main/CRUD%20%20Tacomandi.json      
Flow del broker mqtt: https://github.com/maramendoza692/ProjectVetSafeC3000/blob/main/SENSORES%20Tacomandi.json         









