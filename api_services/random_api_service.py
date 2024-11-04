from api_services.base_api import BaseApiService
from routes import routes


class RandomApiService(BaseApiService):

    def get_random_poems_with_linecount(self, random_count):
        return self._get(routes.RANDOM_ROUTE, random_count)
