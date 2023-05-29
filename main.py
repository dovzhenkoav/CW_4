import pprint

from utils.superjobapi import SuperJobAPI
from utils.headhunerapi import HeadHunterAPI
from utils.vacancy import Vacancy
from  utils.json_saver import JSONSaver

superjob_api = SuperJobAPI()
headhunter_api = HeadHunterAPI()

superjob_vacancies = superjob_api.get_vacancies('Python')
headhunter_vacancies = headhunter_api.get_vacancies('Python')

for data in superjob_vacancies:
    Vacancy(data)

for i in Vacancy.all_vacancies:
    print(i)
# pprint.pprint(superjob_vacancies)

for vacancy in Vacancy.all_vacancies:
    JSONSaver.add_vacancy(vacancy)













