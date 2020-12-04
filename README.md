# torres-de-hanoi

Algoritmos de búsqueda para el juego de torres de hanoi. Los algoritmos empleados para la busqueda de una solución fueron DFS, BFS, Best FS.

## Pre-requisitos 📋

Para la ejecución de los scripts se necesitan varias librerias como 
 numpy
 pandas
 pygal
 lxml.

### Instalación 🔧

Use la siguiente linea de comando para instalar la dependencias

```
pip install numpy pandas pygal lxml
```

## Comenzando 🚀

El seguimiento de los scripts es el siguiente, donde cada uno tiene una funcion especifica y algunos en particular tienen un orden de ejecución.

**torre-de-hanoi.py** - Este script lo que hace es hacer 20 iteraciones de los 3 algoritmos, donde se generara un estado inicial totalmente aleatorio y diferente de los demas.

![torre-de-hanoi.py](https://i.imgur.com/WESkKjF.png)

Después de haber generado los recorridos, el script generara un archivo con extención .csv, donde este contendra los datos obtenidos de los recorridos de los algoritmos.

![Explorador de Archivos](https://i.imgur.com/0q5f9qG.png)


**plot.py** - Despues de haber generado el archivo .csv ahora podemos ejecutar de manera correcta **plot.py**, lo que hará este script es que con los datos recabados generara unas graficas.

Por ejemplo, una de las graficas es que compare el tiempo de los tres algoritmos, desde el estado inicial al estado meta.

![Tiempo en Finalizar](https://i.imgur.com/OYrYxEc.png)

Otra grafica compara los movimientos realizados de los tres algoritmos, desde el estado inicial al estado meta.

![Movimientos Realizados](https://i.imgur.com/m57B8nQ.png)


**torre-de-hanoi-graphics.py** - Este script puede ser de utilidad ya que nos ofrece de manera visible el como se encontro la solución de cada estado inicial en cualquiera de los 3 algoritmos, solo hay que elegir el algoritmo.

![torre-de-hanoi-graphics.py](https://i.imgur.com/NrVo6Cq.png)

Despues se introduce el estado inicial, del que quieres ver el procedimiento. OJO: en caso de que en alguna columna, poste, etc; este no tenga algún disco solo se da enter y no se teclea nada.

De tal modo que para el primer estado, de lo que genero **torre-de-hanoi.py** en la imagen de arriba que asi.

![torre-de-hanoi-graphics.py](https://i.imgur.com/4bVMJ8G.png)

Una vez ingresado el estado inicial, empezara el algoritmo a encontrar una solución, y esta se vera de esta manera. 
Donde en la parte de arriba busca la solución del estado inicial, una vez que lo encuentra, empieza a dibujar los estados que se dieron con el fin de llegar al estado meta.

![torre-de-hanoi-graphics.py](https://i.imgur.com/ZoRmilK.png)


Las imagenes solo son demostrativas, los datos que incluyen pueden varias entre las imagenes.

## Autores ✒️

* **Fátima Lozoya** - [fatimalozoya](https://github.com/fatimalozoya)
* **Javier Gaona** - [JavierGaonaR](https://github.com/JavierGaonaR)
* **Carlos Sanchez** - [1998CarlosSanchez](https://github.com/1998CarlosSanchez)

