import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class SeriestiempoarlandingPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IRoutes)

    valid_series_paths = [
        "/series/api",
        "/series/api/",
        "/series/api/series",
        "/series/api/series/",
    ]

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'seriestiempoarlanding')

    def before_map(self, m):
        for path in self.valid_series_paths:
            m.connect(path,
                      controller='ckanext.seriestiempoarlanding.controller:TSArController',
                      action='series_tiempo')
        return m

    def after_map(self, m):
        return m
