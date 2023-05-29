import requests

from utils.abstractclasses import AbstractAPI
from settings import SUPERJOB_API_ENDPOINT, SUPERJOB_API_KEY


class SuperJobDataHandler:
    @staticmethod
    def vacancy_parser(data: dict):
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
    def __init__(self):
        self.SUPERJOB_API_ENDPOINT = SUPERJOB_API_ENDPOINT
        self.SUPERJOB_API_KEY = SUPERJOB_API_KEY
        self.host = "api.superjob.ru"
        self.authorization = "Bearer r.000000010000001.example.access_token"
        self.content_type = "application/x-www-form-urlencoded"

        self.max_results = 20  # Results per response. Default = 20. Max = 100.
        # Empty town string should give results across Russia.
        # Can be "moscow", "saint-petersburg" or etc.
        # for particular search by town.
        self.town = ""
        self.required_vacancy = None  # ?
        self.period = 3  # Publication period. 1 = 24 hours, 3 = 3 days, 7 = 7 days, 0 = all time.

        # self.profession = None
        # self.firm_name = None
        # self.payment = None
        # self.description = None
        # self.address = None

    def get_vacancies(self, required_vacancy: str):
        self.required_vacancy = required_vacancy

        headers = {"Host": self.host,
                   "X-Api-App-Id": SUPERJOB_API_KEY,
                   "Authorization": self.authorization,
                   "Content-Type": self.content_type}

        params = {"keyword": self.required_vacancy,
                  "town": self.town,
                  "count": self.max_results,
                  "period": self.period}

        response = requests.get(self.SUPERJOB_API_ENDPOINT, headers=headers, params=params)
        return SuperJobDataHandler.vacancy_parser(response.json())
