# TACOMANDI
## Objetivo del proyecto
Tacomandi tiene como objetivo crear un mandil diseñado específicamente para taqueros y cocineros que se enfrentan a una alta demanda de pedidos diarios. Este mandil inteligente busca proporcionar un entorno de trabajo más seguro y eficiente al alertar a los usuarios sobre situaciones potencialmente peligrosas y brindarles acceso rápido a la información de los pedidos pendientes.

## Objetivos específicos:
Mejorar la seguridad y el bienestar de los taqueros y cocineros al proporcionar alertas en tiempo real sobre situaciones peligrosas.
Optimizar la gestión de pedidos mediante una interfaz gráfica intuitiva y de fácil acceso, lo que resultará en una mayor eficiencia y satisfacción del cliente.
Reducir los desperdicios de recursos al evitar el mal uso de llaves y prevenir fugas de gas.

## Beneficiario
 - 

## Integrantes
- Pedro Emmanuel Martinez Rodriguez 
- María Guadalupe Mendoza Ramírez
- Juan Luis Negrete Labrada
- Paola Guadalupe Patlán Gónzalez


## Componentes empleados
| No. | Componente | Descripción | Img | Costo | Cantidad |
|-----|------------|-------------|-----|-------|----------|
|1|Placa de desarrollo ESP32| Placa de desarrollo ESP32 con pantalla táctil de 2.8 pulgadas. CPU de doble núcleo y una frecuencia de reloj de 240 MHz. Integra periféricos de recursos, SDO de alta velocidad, SP, UART y otras funciones, y admite la descarga automática. |<img src="https://github.com/maramendoza692/ProjectVetSafeC3000/assets/90641538/6606e7d5-c1ad-4ccd-b253-dcaa5afed3a0" width= "200px"/> |$169 | 1 |
|2| Sensor de temperatura| Modulo Ky-001 Sensor De Temperatura |<img src="https://github.com/maramendoza692/ProjectVetSafeC3000/assets/90641538/42fcd6e5-30ac-4b3a-b80c-49a1fb623dbf" width= "200px"/> |$42| 1|
|3| Buzzer| Altavoz que permite convertir una señal eléctrica en una onda de sonido |<img src="https://github.com/maramendoza692/ProjectVetSafeC3000/assets/90641538/8971c075-c206-46ee-b3ac-b7f5571011f7" width= "200px"/> |$47| 1|
|4| ESP32| Tarjeta de desarrollo ESP32 de 30 pines, trae integrado Wi-Fi, Bluetooth y BLE (Bluetooth Low Energy).|<img src="https://github.com/maramendoza692/ProjectVetSafeC3000/assets/90641538/8e9f544f-3a6d-4e98-87c7-2c9083a0b6c6" width= "200px"/>|$158| 1|
|5| Resistencias 220 Ohms| Paquete de resistencias fabricadas con una alambre conductor de una resistividad alta  |<img src="https://github.com/maramendoza692/ProjectVetSafeC3000/assets/90641538/5f5fda94-8ba5-4405-94b3-ff202b49117d" width= "200px"/> |$81| 1|
|6| Sensor de flama| Sensor De Flama |<img src="https://github.com/maramendoza692/ProjectVetSafeC3000/assets/90641538/3116347d-9819-483d-9629-1caf9c7533c0" width= "200px"/> |$49| 1|
|5| Sensor de gas| Paquete de resistencias fabricadas con una alambre conductor de una resistividad alta  |<img src="https://github.com/maramendoza692/ProjectVetSafeC3000/assets/90641538/5f5fda94-8ba5-4405-94b3-ff202b49117d" width= "200px"/> |$81| 1|




## Software utilizado
| Id | Software | Version | Tipo |Funcionalidad|
|----|----------|---------|------|-------------|
| 1 | Fritzing | 0.9.3 |Licencia libre|Modelado|
| 2 | Wokwi    | N/A | Licencia libre | Programación / Modelado|
| 3 | Node-RED | 3.0.2 | Licencia libre| Programación|
| 4 | Tinkercad | N/A |Licencia libre|Modelado 3D |
| 5 | Librería NewPing |N/A|Licencia libre|Para sensores ultrasónicos, incluyendo el HC-SR04.|

## Historias de Usuario
| Id | Historia de usuario | Prioridad | Estimación | Cómo probarlo | Responsable |
|----|---------------------|-----------|------------|---------------|-------------|
|HU01|Yo como ciclista quiero que el dispositivo me permita mostrar la dirección (izquierda o derecha) a la que me dirijo para evitar accidentes con automoviles.|Debe| 1 |El usuario utiliza un dispositivo con luces led y una pantalla integrada para seleccionar las operaciones predeterminadas de dirección|Luis Negrete|
|HUO2|Yo como ciclista quiero que el dispositivo esté en la parte delantera de mi bicicleta y me notifique mediante un sonido cuando estoy muy cerca de un automóvil para tomar mi distancia y evitar accidentes.|Debe |1 y medio| Posicionar un objeto un objeto a 3 metros o menos del dispositivo, el sensor ultrasónico enviará una indicación al buzzer para que suene.|Pedro Martínez |
|HU03|Yo como ciclista quiero visualizar en la pantalla del dispositivo la temperatura y humedad|Debe|1 |Visualizar la temperatura y humedad en la pantalla, acercar un objeto con fuego como un encendedor cerca del sensor para visualizar el cambio de la temperatura en la pantalla. Realizar la misma pueba con un objeto que altere la humedad| Paola Patlán |
|HU04|Yo como ciclista quiero visualizar mi ubicación en la pantalla mediante un mapa para saber dónde me encuentro| Puede |8| Seleccionar el botón "Ver ubicación" en la pantalla del dispositivo, en seguida, visualizar el mapa y la ubicación actual. Avanzar un par de metros y observar que la ubicción cambia |María Mendoza|
|HU05|Yo como ciclista quiero que el dispositivo sea recargable para cargarlo antes de salir en mi bicicleta|Debe|3 |Conectar el dispositivo a la corriente electrica y verificar que esté cargando|Luis Negrete|
|HU06|Yo como ciclista quiero que se muestre la hora en el dispositivo.|Debe|1/2|El usuario visualizará la hora en la pantalla del dispositivo|Pedro Martínez|
|HU07|Yo como ciclista quiero que el dispositivo mida mi actividad física para saber cuál fue mi recorrido diario.|Estaría bien|4 |Presionar el botón "Ver mi actividad" y visualizar los kilometros recorridos.|Paola Patlán|
|HU08|Yo como ciclista quiero compartir mi ubicación a otros dispositivos para que sepan dónde estoy.|Estaría bien|6|Presionar el botón "Ver ubicación" y después "Compartir ubicación"|María Mendoza|
|HU09| Yo como cicista quiero ver la vista trasera de todo lo que me rodea para poder evitar algun accidente, por lo cual quiero que la camara este en la parte trasera de mi espalda. Así mismo este sera usado como un retrovisor| Estaria Bien | 3| Seleccionar el boton ver retrovisor y le tendra que dar el panorama de a parte trasera e ir viendo quein va detras de el| Pedro Martinez |

## NOTA
1 Punto de esfuerzo es igual a desarrollo de un Login.

## Prototipo en dibujo
![image](https://github.com/maramendoza692/ProjectVetSafeC3000/assets/90641538/5e53288f-e11a-48bb-a677-c403db53b844)

## Prototipo en Fritzing

![image](https://github.com/maramendoza692/ProjectVetSafeC3000/assets/90641538/b0afe428-e119-42b0-9ca5-d090fe23aae2)


## Placa PCB

![image](https://github.com/maramendoza692/ProjectVetSafeC3000/assets/90641538/fe32acaf-4333-4bd0-8362-fb37d197e085)


## Prototipo en 3D
- Imagen de prototipo realizado en tinkercad
![Captura de pantalla 2023-06-03 142936](https://github.com/maramendoza692/ProjectVetSafeC3000/assets/87114168/9e7a4027-dd06-4565-81cf-60c1d9dab557)
![Captura de pantalla 2023-06-03 142947](https://github.com/maramendoza692/ProjectVetSafeC3000/assets/87114168/2e41cbf7-1afe-4a95-b7d1-6e0416e918e3)

