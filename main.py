import pprint

from utils.superjobapi import SuperJobAPI
from utils.headhunerapi import HeadHunterAPI
from utils.vacancy import Vacancy
from utils.json_saver import JSONSaver


superjob_api = SuperJobAPI()
headhunter_api = HeadHunterAPI()


def main():
    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))

    superjob_vacancies = superjob_api.get_vacancies(search_query)
    headhunter_vacancies = headhunter_api.get_vacancies(search_query)

    for data in headhunter_vacancies + superjob_vacancies:
        Vacancy(data)

    for vacancy in Vacancy.all_vacancies:
        JSONSaver.add_vacancy(vacancy)

    pprint.pprint(JSONSaver.get_top_vacancies(top_n))


if __name__ == '__main__':
    main()