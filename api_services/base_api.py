import logging

import requests
from requests import Response
import config

logger = logging.getLogger(__name__)


class BaseApiService:

    def __init__(self):
        self._base_url = config.BASE_API_URL
        self._session = requests.Session()

    def _get(self, *routes, **kwargs) -> Response:
        url = self.__construct_url(*routes)
        logger.info(f"GET request to {url}")
        return self._session.get(url, **kwargs)

    def _post(self, body: dict, *routes, **kwargs) -> Response:
        url = self.__construct_url(*routes)
        logger.info(f"POST request to {url}")
        return self._session.post(url, json=body, **kwargs)

    def _delete(self, *routes, **kwargs) -> Response:
        url = self.__construct_url(*routes)
        logger.info(f"DELETE request to {url}")
        return self._session.delete(url, **kwargs)

    def __construct_url(self, *routes):
        return self._base_url + "/" + "/".join(map(str, routes))
