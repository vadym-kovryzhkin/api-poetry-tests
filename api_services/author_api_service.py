from api_services.base_api import BaseApiService
from routes import routes


class AuthorApiService(BaseApiService):

    def get_poems_by_author(self, author_name):
        return self._get(routes.AUTHOR_ROUTE, author_name)
