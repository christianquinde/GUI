# GUI
Esta herramienta permite transmitir cualquier video en formato YUV hacia otro ordenador dentro de la misma
red y calcular las métricas de delay, thoughput, packet loss, consumo de CPU, tiempo de codificación y PSNR.

Esta herramienta se diseñó mediante scripts de Linux para cumplir con las distintas funcionalidades y los experimentos se efectuaron en ordenadores con sistema operativo Ubuntu 20.04. Para efectuar los diferentes cálculos también se implementaron scripts en Python 3.7. 

Esta herramienta se ejecuta en paralelo con la herramienta GUI dsiponible en: https://github.com/christianquinde/GUI-rx

En la siguiente Figura se muestra el diagrama secuencial de las herramientas en Tx y Rx.
![gui_func](https://user-images.githubusercontent.com/68077496/155746084-d72953c8-5abe-495d-9334-043c382a87b2.png)

En las siguiente Figura se muestran la interfaz del transmisor.

![gui_int_tx](https://user-images.githubusercontent.com/68077496/155747349-2fce1065-2df0-4f4a-bdf8-4d0b23a5daa6.png)


# Funcionamiento
## 1: Cargar
Primero se cargan los datos mediante el botón Cargar.
Para el transmisor se selecciona el video deseado en formato YUV, las IPs de origen y destino, el códec, el puerto
de destino, el framework multimedia, el piso del ordenador receptor y finalmente el número de transmisión. 
Cabe recalcar que se puede seleccionar el tipo de herramienta tanto GStreamer como FFMPEG.

## 2: Sincronizar
Seguidamente, por medio del botón Sincronizar, se sincroniza con el servidor NTP ubicado en uno de los ordenadores.

## 3: Transmitir
Se envía el video al presionar el botón Transmitir para enviar el video al receptor. Además de realizar una captura de tráfico con tcpdump.

## 4: Stop
Al terminar de transmitir y reproducir el video, se da clic al botón Stop para finalizar la captura de paquetes y convertirlos a Comma Separated Values (CSV). 

## 5: Recibir PCAPs
Luego, se oprime el botón Recibir PCAPs, para abrir un puerto determinado para aceptar los archivos.

## 6: Calcular métricas
Finalmente se da clic en el botón Calcular para medir el throughput, el porcentaje de uso de la CPU, el delay promedio, el porcentaje de packet loss y finalmente el tiempo de transmisión.


## 7: Calcular promedio y generar gráficas comparativas
Por último, los dos botones "Generar Gráficas" y "GRÁFICAS" abren dos diferentes interfaces, con el primer
botón se abre la interfaz que se observa en la siguiente Figura, donde se realiza una comparación entre los códecs por
cada transmisión de los cuatro diferentes códecs. 

![gui_int_3](https://user-images.githubusercontent.com/68077496/155747766-7e857a1c-b811-4b29-a483-74106d809f7c.png)

En cambio, el segundo botón abre otra interfaz que se observa
en la siguiente Figura donde se realiza un promedio de las cinco diferentes transmisiones de cada métrica (delay,
throughput, packet loss, PSNR, consumo de CPU y tiempo de codificación) y se determinan los intervalos de confianza del 95% de fiablidad. Al final de esta interfaz se encuentra el botón Grabar, el cual mueve todas las
figuras generadas a una carpeta específica donde existe una mayor organización para documentar los resultados.


![gui_int_4](https://user-images.githubusercontent.com/68077496/155747776-84fdc4bc-f2b8-4c3c-bc8e-e7a73b8e49e4.png)

# Funciones Adicionales
Además, se incluyeron los botones: "Codificar Video" y "Play Video". De los
cuales, el primero se utiliza para codificar y almacenar un video con los parámetros seleccionados pero no se
transmite. El botón Play Video sirve para reproducir el video previamente codificado en el transmisor.
