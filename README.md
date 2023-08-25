# TACOMANDI
## Objetivo del proyecto
Tacomandi tiene como objetivo crear un mandil diseñado específicamente para taqueros y cocineros que se enfrentan a una alta demanda de pedidos diarios. Este mandil inteligente busca proporcionar un entorno de trabajo más seguro y eficiente al alertar a los usuarios sobre situaciones potencialmente peligrosas y brindarles acceso rápido a la información de los pedidos pendientes.

## Objetivos específicos:
Mejorar la seguridad y el bienestar de los taqueros y cocineros al proporcionar alertas en tiempo real sobre situaciones peligrosas.
Optimizar la gestión de pedidos mediante una interfaz gráfica intuitiva y de fácil acceso, lo que resultará en una mayor eficiencia y satisfacción del cliente.
Reducir los desperdicios de recursos al evitar el mal uso de llaves y prevenir fugas de gas.

## Beneficiario
 - Ana Luisa Muñoz Hernández

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
|7| Sensor de gas| MQ-5 Detección de: Gas LP, Metano/Gas Natural, Hidrógeno, Alcohol y Humo. Alta sensibilidad al: Gas LP y Metano/Gas Natural  |<img src="https://github.com/maramendoza692/ProjectVetSafeC3000/assets/90641538/853bb66a-0be2-41f3-ac98-3dfc73e340fc" width= "200px"/> |$81| 1|
|8| Pantalla OLED ssd1606 |controlador SSD1606 permite la visualización de gráficos y texto en pantallas OLED.|<img src="https://www.winstar.com.tw/uploads/photos/graphic-oled-display/WEA012864DW-01.jpg" width= "200px"/>|$110|1




## Software utilizado
| Id | Software | Version | Tipo |Funcionalidad|
|----|----------|---------|------|-------------|
| 1 | Fritzing | 0.9.3 |Licencia libre|Modelado|
| 2 | Wokwi    | N/A | Licencia libre | Programación / Modelado|
| 3 | Node-RED | 3.0.2 | Licencia libre| Programación|
| 4 | Tinkercad | N/A |Licencia libre|Modelado 3D |
| 5 | Librería NewPing |N/A|Licencia libre|Para sensores ultrasónicos, incluyendo el HC-SR04.|

## Historias de Usuario
| Id | Historia de usuario | Prioridad | Estimación | Cómo probarlo | Responsable | Sprint |
|----|---------------------|-----------|------------|---------------|-------------|--------|
|HU01|Yo como taquero quiero que el mandil me alerte mediante un sonido cuando este se esté comenzando a incendiar, para poder tomar acciones inmediatas y que el resto de los cocineros pueda darse cuenta y ayudarme, pues siempre estoy muy ocupado y algunas veces no detecto el fuego hasta que este ya se ha extendido en la mayoría del mandil.|Debe| 1 |Se enciende una llama a 5 cm del sensor y el buzzer debe emitir un sonido|Paola Patlán|1|
|HUO2|Yo como taquero quiero que el mandil me alerte mediante una luz cuando una llave de la estufa esté abierta y se esté escapando el gas, para poder tomar medidas inmediatas y prevenir accidentes.|Debe |1 |Liberar gas de un encendedor cerca del sensor de gas para simular una fuga (posicionar cerca para que pueda reconocer el gas pues es una cantidad pequeña)y observar cómo el led rojo parpadea| Pedro Martínez |1|
|HU03|Yo como taquero quiero que el mandil me alerte mediante una luz cuando he pasado mucho tiempo frente al calor del fuego y mi temperatura es demasiado alta, para prevenir deshidratación, agotamiento por calor e incluso un golpe de calor, recordándome que es momento de tomar una bebida hidratante.|Debe|1 |Acercar un objeto con fuego como un encendedor cerca del sensor para aumentar la temperatura, observar que el led azul comeinza a parpadear| María Mendoza |1|
|HU04|Yo como mesero quiero poder enviar los pedidos desde la mesa que estoy atendiendo hasta la cocina, mediante la pantalla de mi celular, para agilizar el proceso de pedidos sin tener que ir hasta la cocina a realizar el pedido. | Debe |4| Seleccionar los botones con las opciones de los platillos y la cantidad de estos en la pantalla del celular (Por ejemplo: platillo: tacos bisteck, cantidad: 10). En seguida, presionar le boton "Enviar pedido"|Luis Negrete|2|
|HU05|Yo como taquero quiero contar con una pantalla integrada en el mandil de manera estratégica, que sea desplegable y únicamente visualizarla cuando lo necesito, para poder visualizar los pedidos pendientes por realizar.|Debe| 4 |Enviar un pedido desde el celular descrito en la HU04. Desplegar la pantalla ubicada en la parte superior del mandil. Observar el pedido en la pantalla. Regresar la pantalla a su posición inicial|Paola Patlán|2|
|HU06|Yo como taquero quiero recibir una notificación mediante vibración cada que llegue un pedido, para darme cuenta que tengo nuevos pedidos y debo presionarme, además de desplegar la pantalla y poder visualizarlo.|Debe|2|Enviar un pedido desde el celular descrito en la HU04. Sentir una vibración. Desplegar la pantalla ubicada en la parte superior del mandil. Observar el pedido en la pantalla. Regresar la pantalla a su posición inicial|Pedro Martínez|2|
|HU07|Yo como taquero quiero que el mandil cuente con un botón posicionado estratégicamente para que al presionarlo, se informe al mesero mediante una notificación en la pantalla de su celular que el pedido en cola ya se realizó.|Debe|4 |Visualizar los pedidos en la pantalla. Presionar el botón. Visualizar nuevamente la pantalla y ver que este se ha eliminado. Visualizar la notificación en el celular del mesero.|María Mendoza|2|
|HU08|Yo como taquero quiero que el mandil cuente con un segundo botón que notifique al mesero que no reciba más pedidos, pues la lista está saturada, asimismo, al volver a presionar el botón, renaudar el envío de pedidos.|Deben|4|Presionar el botón y recibir la notificación en el celular del mesero|Luis Negrete|2|

1 Punto de esfuerzo es igual a desarrollo de un Login.

## Prototipo en 3D
- Imagen de prototipo realizado en tinkercad
![image](https://github.com/maramendoza692/ProjectVetSafeC3000/assets/90641538/e43656cf-49b0-4d67-9eb5-f18bc8fd497f)

## Imagen del mandil

## Aplicación web

![image](https://github.com/maramendoza692/ProjectVetSafeC3000/assets/90641538/e34dbe7d-f2df-4e82-b8e7-7f2d6d4ef68d)


## Dashboard en Grafana

## Carta de aceptación del proyecto firmada por la beneficiaria

## Vídeo de aceptación del proyecto

## Vídeo demostrativo

## Código fuente









