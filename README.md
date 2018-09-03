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

