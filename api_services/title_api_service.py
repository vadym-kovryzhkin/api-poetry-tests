from api_services.base_api import BaseApiService
from routes import routes


class TitleApiService(BaseApiService):

    def get_poem_by_title(self, title):
        return self._get(routes.TITLE_ROUTE, title, "title,lines")
