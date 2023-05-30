import requests

from utils.abstractclasses import AbstractAPI
from settings import HH_API_ENDPOINT


class HeadHunterDataHandler:
    """Parser for response data from hh.ru."""

    @staticmethod
    def vacancy_parser(data: dict) -> list[dict]:
        """Get from hh.ru JSON response necessary data.

        Args:
            data (dict): JSON response from hh.ru.

        Returns:
            list[dict]: necessary data from all vacancy JSON data.

        """
        clear_vacancies = []

        for vacancy in data['items']:
            single_vacancy = {
                "profession": vacancy['name'],
                "firm_name": vacancy['employer']['name'],
                "link": vacancy['alternate_url'],
                "description": vacancy['snippet']['responsibility'],
                "payment_from": vacancy['salary']['from'],
                "payment_to": vacancy['salary']['to'],
                "town": vacancy['area']['name']
            }

            if single_vacancy["payment_from"] is None:
                single_vacancy["payment_from"] = 0
            if single_vacancy["payment_to"] is None:
                single_vacancy["payment_to"] = 0

            clear_vacancies.append(single_vacancy)
        return clear_vacancies


class HeadHunterAPI(AbstractAPI):
    """API class, that allows to get data from hh.ru.

    Attributes:
        max_results (int): Max results per response. Default=20, max=100.
        period (int): Vacancy publication period in days.
        only_with_salary (bool): May shows vacancies with/without salary.

    """

    def __init__(self):
        self._HH_ENDPOINT = HH_API_ENDPOINT

        self.max_results = 20
        self.period = 3
        self.only_with_salary = True

    def get_vacancies(self, required_vacancy: str) -> list[dict]:
        """Get vacancies from hh.ru.

        Args:
            required_vacancy (str): required query string.

        Returns:
            list[dict]: response data runs through
                HeadHunterDataHandler class and become pure to work with.

        """
        params = {
            "per_page": self.max_results,
            "text": required_vacancy,
            "only_with_salary": self.only_with_salary,
            "period": self.period
        }

        response = requests.get(self._HH_ENDPOINT, params=params)
        return HeadHunterDataHandler.vacancy_parser(response.json())
