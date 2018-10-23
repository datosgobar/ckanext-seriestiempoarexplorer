from logging import getLogger

from pylons.config import config
import ckan.lib.base as base

logger = getLogger(__name__)


class TSArController(base.BaseController):
    def series_tiempo(self):
        return base.render('seriestiempoarexplorer/series_explorer.html', extra_vars={})
