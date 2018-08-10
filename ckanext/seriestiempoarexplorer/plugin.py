import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class SeriestiempoarexplorerPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IRoutes)

    valid_series_paths = [
        {"path": "/series/api"},
        {"path": "/series/api/", "name": "series_tiempo_ar_explorer"},
        {"path": "/series/api/series"},
        {"path": "/series/api/series/"},
    ]

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'seriestiempoarexplorer')

    def before_map(self, m):
        for path_conf in self.valid_series_paths:
            if path_conf.get("name"):
                m.connect(path_conf.get("name"), path_conf.get("path"),
                          controller='ckanext.seriestiempoarexplorer.controller:TSArController',
                          action='series_tiempo')
            else:
                m.connect(path_conf.get("path"),
                          controller='ckanext.seriestiempoarexplorer.controller:TSArController',
                          action='series_tiempo')
        return m

    def after_map(self, m):
        return m
