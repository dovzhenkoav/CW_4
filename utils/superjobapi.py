import requests

from utils.abstractclasses import AbstractAPI
from settings import SUPERJOB_API_ENDPOINT, SUPERJOB_API_KEY


class SuperJobDataHandler:
    """Parser for response data from superjob.ru."""

    @staticmethod
    def vacancy_parser(data: dict) -> list[dict]:
        """Get from superjob.ru JSON response necessary data.

        Args:
            data (dict): JSON response from superjob.ru.

        Returns:
            list[dict]: necessary data from all vacancy JSON data.

        """

        clear_vacancies = []

        for vacancy in data['objects']:
            single_vacancy = {
                "profession": vacancy['profession'],
                "firm_name": vacancy['firm_name'],
                "link": vacancy['link'],
                "description": vacancy['vacancyRichText'],
                "payment_from": vacancy['payment_from'],
                "payment_to": vacancy['payment_to'],
                "town": vacancy['town']['title']
            }
            clear_vacancies.append(single_vacancy)
        return clear_vacancies


class SuperJobAPI(AbstractAPI):
    """API class, that allows to get data from superjob.ru.

    Attributes:
        max_results (int): Max results per response. Default=20, max=100.
        period (int): Vacancy publication period
            1 = 24 hours, 3 = 3 days, 7 = 7 days, 0 = all time.

    """

    def __init__(self):
        self._SUPERJOB_API_ENDPOINT = SUPERJOB_API_ENDPOINT
        self._SUPERJOB_API_KEY = SUPERJOB_API_KEY
        self._host = "api.superjob.ru"
        self._authorization = "Bearer r.000000010000001.example.access_token"
        self._content_type = "application/x-www-form-urlencoded"

        self.max_results = 20
        self.period = 3

    def get_vacancies(self, required_vacancy: str) -> list[dict]:
        """Get vacancies from superjob.ru.

        Args:
            required_vacancy (str): required query string.

        Returns:
            list[dict]: response data runs through
                SuperJobDataHandler class and become pure to work with.

        """
        headers = {"Host": self._host,
                   "X-Api-App-Id": self._SUPERJOB_API_KEY,
                   "Authorization": self._authorization,
                   "Content-Type": self._content_type}

        params = {"keyword": required_vacancy,
                  "count": self.max_results,
                  "period": self.period}

        response = requests.get(self._SUPERJOB_API_ENDPOINT,
                                headers=headers,
                                params=params)
        return SuperJobDataHandler.vacancy_parser(response.json())
