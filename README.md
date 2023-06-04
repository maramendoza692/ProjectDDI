# ProjectVestSafe3000
## Objetivo del proyecto
El presente proyecto busca disminuir los accidentes viales de los ciclistas por medio de un chaleco mejorado, al cual se le integra TI para realizar predeterminas acciones que aumenten su seguridad. 

## Beneficiario
Osvaldo Baeza - Ciclista

## Integrantes
- Pedro Emmanuel Martinez Rodriguez 
- María Guadalupe Mendoza Ramírez
- Juan Luis Negrete Labrada
- Paola Guadalupe Patlán Gónzalez


## Componentes empleados
| No. | Componente | Descripción | Img | Costo | Cantidad |
|-----|------------|-------------|-----|-------|----------|
|1|Placa de desarrollo ESP32| Placa de desarrollo ESP32 con pantalla táctil de 2.8 pulgadas |<img src="https://github.com/maramendoza692/ProjectVetSafeC3000/assets/90641538/6606e7d5-c1ad-4ccd-b253-dcaa5afed3a0" width= "200px"/> |$169 | 1 |
|2|Sensor ultrasónico HCS|Sensor para detectar proximidad|<img src="https://github.com/maramendoza692/ProjectVetSafeC3000/assets/90641538/cb4e3f10-a399-4131-ac95-e7b542e64004" width= "200px"/> |$59| 1 |
|3| DHT22| Sensor De Temperatura Y Humedad Dht22 |<img src="https://github.com/maramendoza692/ProjectVetSafeC3000/assets/90641538/ec8a686b-40bf-4e83-9a69-efaddb7d0cae" width= "200px"/> |$99| 1|
|4| Buzzer| Altavoz que permite convertir una señal eléctrica en una onda de sonido |<img src="https://github.com/maramendoza692/ProjectVetSafeC3000/assets/90641538/8971c075-c206-46ee-b3ac-b7f5571011f7" width= "200px"/> |$47| 1|
|5| Resistencias 220 Ohms| Paquete de resistencias fabricadas con una alambre conductor de una resistividad alta  |<img src="https://github.com/maramendoza692/ProjectVetSafeC3000/assets/90641538/5f5fda94-8ba5-4405-94b3-ff202b49117d" width= "200px"/> |$81| 1|
|6| Led | 2 Piezas Max7219 Matriz De Leds 8x8 Arduino Led Pic|<img src="https://github.com/maramendoza692/ProjectVetSafeC3000/assets/90641538/9a3bacc9-ee5d-4f1e-b610-eaf287839f64" width= "200px"/>| $129|1|





## Software utilizado
| Id | Software | Version | Tipo |
|----|----------|---------|------|
| S1 | Fritzing |     0.9.3    |Modelado|
| S2 | Wokwi    |         | Programación / Modelado |
| S3 | Node-RED |    3.0.2     |Programación |
| S4 | Tinkercad |         |Modelado 3D |

## Historias de Usuario
| Id | Historia de usuario | Prioridad | Estimación | Cómo probarlo | Responsable |
|----|---------------------|-----------|------------|---------------|-------------|
|HU01|Yo como usuario quiero que el dispositivo me permita mostrar la dirección (izquierda o derecha) a la que me dirijo para evitar accidentes con automoviles.|Debe|4 días|El usuario utiliza un dispositivo con luces led y una pantalla integrada para seleccionar las operaciones predeterminadas de dirección|Luis Negrete|
|HUO2|Yo como usuario quiero que el dispositivo esté en la parte delantera de mi bicicleta y me notifique mediante un sonido cuando estoy muy cerca de un automóvil para tomar mi distancia y evitar accidentes.|Debe |4 días| Posicionar un objeto un objeto a 3 metros o menos del dispositivo, el sensor ultrasónico enviará una indicación al buzzer para que suene.|Pedro Martínez |
|HU03|Yo como usuario quiero visualizar en la pantalla del dispositivo la temperatura y humedad|Debe|3 días|Visualizar la temperatura y humedad en la pantalla, acercar un objeto con fuego como un encendedor cerca del sensor para visualizar el cambio de la temperatura en la pantalla. Realizar la misma pueba con un objeto que altere la humedad| Paola Patlán |
|HU04|Yo como usuario quiero visualizar mi ubicación en la pantalla mediante un mapa para saber dónde me encuentro| Puede |10 días| Seleccionar el botón "Ver ubicación" en la pantalla del dispositivo, en seguida, visualizar el mapa y la ubicación actual. Avanzar un par de metros y observar que la ubicción cambia |María Mendoza|
|HU05|Yo como usuario quiero que el dispositivo sea recargable para cargarlo antes de salir en mi bicicleta|Debe|5 días|Conectar el dispositivo a la corriente electrica y verificar que esté cargando|Luis Negrete|
|HU06|Yo como usuario quiero que se muestre la hora en el dispositivo.|Debe|2 días|El usuario visualizará la hora en la pantalla del dispositivo|Pedro Martínez|
|HU07|Yo como usuario quiero que el dispositivo mida mi actividad física para saber cuál fue mi recorrido diario.|Estaría bien|7 días|Presionar el botón "Ver mi actividad" y visualizar los kilometros recorridos.|Paola Patlán|
|HU08|Yo como usuario quiero compartir mi ubicación a otros dispositivos para que sepan dónde estoy.|Estaría bien|8 días|Presionar el botón "Ver ubicación" y después "Compartir ubicación"|María Mendoza|

## Prototipo en dibujo
- Coloca la fotografia de tu prototipo dibujado a lapiz
![Imagen de WhatsApp 2023-06-03 a las 00 55 32](https://github.com/maramendoza692/ProjectVetSafeC3000/assets/87114168/c1fd84f6-b6bf-4043-98c8-66b3efdea064)

## Prototipo en Fritzing

![image](https://github.com/maramendoza692/ProjectVetSafeC3000/assets/90641538/b0afe428-e119-42b0-9ca5-d090fe23aae2)


## Placa PCB

![image](https://github.com/maramendoza692/ProjectVetSafeC3000/assets/90641538/fe32acaf-4333-4bd0-8362-fb37d197e085)


## Prototipo en 3D
- Imagen de prototipo realizado en tinkercad
![Captura de pantalla 2023-06-03 142936](https://github.com/maramendoza692/ProjectVetSafeC3000/assets/87114168/9e7a4027-dd06-4565-81cf-60c1d9dab557)
![Captura de pantalla 2023-06-03 142947](https://github.com/maramendoza692/ProjectVetSafeC3000/assets/87114168/2e41cbf7-1afe-4a95-b7d1-6e0416e918e3)

