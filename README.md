# WebScraping-Manar
A la fecha, este proyecto es parte de la iniciativa de Innovación de Manar.
Principalmente se centra en el proceso de Web Scraping para el retail de cadenas importantes como el Exito y Olimpica.

## Configuración

### Virtual Env
Antes de trabajar, es recomendable crear un ambiente virtual de python para facilitar el control de las versiones y los paquetes necesarios. 
> De no saber como hacerlo, [acá](https://docs.python.org/3/tutorial/venv.html) hay una corta guía.

Adicionalmente, el archivo **requirements.txt** es un pip freeze de las versiones utilizadas al momento de la creación del repositorio.
> Para trabajar con estas mismas versiones, se puede utilizar la funcion `install -r` de pip.

### Scrapy
Este proyecto tiene sus fundamentos en el framework **Scrapy**, lo cual facilita el manejo, ejecución y mantenimiento de los "spyders", permitiendo un mejor crecimiento del proyecto a largo plazo.
> **La implementación utilizada es sumamente superficial, la lógica de los spyders es diferente a la utilizada originalmente en scrapy debido a que las páginas objetivo son dinámicas.**

La documentación de Scrapy se puede encontrar [acá](https://scrapy.org/).

Algunos videos que pueden ayudar al entendimiento de Scrapy y en general aprender como funciona el web Scraping:
- [Intro To Web Crawlers & Scraping With Scrapy](https://www.youtube.com/watch?v=ALizgnSFTwQ).
- [Python Scrapy Tutorial (Playlist)](https://www.youtube.com/watch?v=ve_0h4Y8nuI&list=PLhTjy8cBISEqkN-5Ku_kXG4QW33sxQo0t).
- [Python Scrapy Tutorial - Cats & Spiders? Web Scraping Reddit with Scrapy](https://www.youtube.com/watch?v=ogPMCpcgb-E&t).

> En los videos también se mencionan algunas herramientas útiles para el proceso de Web Scraping, como [Web Scrapper](https://www.youtube.com/watch?v=n7fob_XVsbY&t) para la extracción de los tags necesarios.

### Selenium
En el proyecto se utiliza **Selenium** para renderizar la información dinámica de las páginas objetivo y posteriormente obtener la información.
La documentación necesaria se puede encontrar [acá](https://selenium-python.readthedocs.io/)

### Webdrivers
Dado el tipo de implementación utilizada en este proyecto para es scraping de páginas dinámicas, es necesario el uso de web drivers, los cuales se integran con **Selenium** para renderizar primero la información y luego ser extraida mediante las técnicas comunes de web scraping.

Los Drivers pueden ser encontrados acá:
- [Google Chrome](https://chromedriver.chromium.org/downloads).
- [Firefox](https://github.com/mozilla/geckodriver/releases).

Por omisión, el proyecto usa el driver de Chrome para trabajar, pero puede ser configurado para que utilice cualquier driver que se desee o se requierea y no debería presentar problemas.
> Si se desea cambiar el driver, hay que tener en cuenta los parametros de personalización propios de cada navegador, como especificar una resolución o cancelar las notificaciones.
