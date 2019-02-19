# ckanext-seriestiempoarexplorer

SeriesTiempoArExplorerPlugin para Andino.
Integración de [Portal Andino](https://github.com/datosgobar/portal-andino) y [Series de Tiempo Ar Explorer](https://github.com/datosgobar/series-tiempo-ar-explorer/)

## Instalación

Para instalar `ckanext-seriestiempoarexplorer`:

1. Activá el _virtualenv_ de tu instancia de CKAN:

     . /usr/lib/ckan/default/bin/activate

2. Instalá el paquete de Python `ckanext-seriestiempoarexplorer` dentro del _virtualenv_:

     pip install -e git+https://github.com/datosgobar/ckanext-seriestiempoarexplorer.git#egg=ckanext-seriestiempoarexplorer

3. Agregá `seriestiempoarexplorer` a la lista de `ckan.plugins` en tu archivo de configuración de CKAN
   (por defecto ubicada en `/etc/ckan/default/production.ini` dentro del contenedor `portal`).

4. Reiniciá Andino.

## Crear release 

Para tener listo el nuevo release en el entorno de desarrollo:

1. En este repositorio:

     a. Actualizar template `series_explorer.html` para que la URL al archivo `main.js` sea la perteneciente a la última versión del plugin, y modificar, en caso de que sea necesario, los parámetros del script de rendereo.
     
     b. Actualizar el archivo `main.css` con los nuevos estilos implementados. Es posible que hayan problemas entre éstos y los estilos propios de Andino; en ese caso, modificar los estilos escritos de modo tal que quede de la forma deseada.
     
2. En portal-andino:

     a. Actualizar el Dockerfile para que se realice un pip install de la nueva versión de `ckanext-seriestiempoarexplorer`; tiene que quedar de una forma parecida al siguiente ejemplo empleando el nombre del branch donde se implementaron los cambios:
     `git+https://github.com/datosgobar/ckanext-seriestiempoarexplorer.git@{nombre-del-branch-nuevo}#egg=ckanext-seriestiempoarexplorer`.
     
     b. Levantar una instancia de Andino, probar que los cambios se hayan aplicado, y que no haya ningún problema con los estilos.
     
     c. Ahora se puede mergear el branch a master, crear un release nuevo _para este repositorio_, y cambiar el nombre del branch en el Dockerfile de portal-andino por el tag generado.

