import requests

from utils.abstractclasses import AbstractAPI
from settings import HH_API_ENDPOINT


class HeadHunterDataHandler:
    @staticmethod
    def vacancy_parser(data: dict):
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
    def __init__(self):
        self.HH_ENDPOINT = HH_API_ENDPOINT
        self.host = "api.superjob.ru"

        self.max_results = 20  # Results per response. Default = 20. Max = 100.
        self.period = 3
        self.only_with_salary = True

    def get_vacancies(self, required_vacancy: str):
        params = {
            "per_page": self.max_results,
            "text": required_vacancy,
            "only_with_salary": self.only_with_salary,
            "period": self.period
        }

        response = requests.get(self.HH_ENDPOINT, params=params)
        return HeadHunterDataHandler.vacancy_parser(response.json())
















