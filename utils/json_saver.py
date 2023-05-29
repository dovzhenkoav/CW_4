import os
import json

from utils.abstractclasses import AbstractJSONSaver
from utils.vacancy import Vacancy


class JSONSaver(AbstractJSONSaver):

    @classmethod
    def add_vacancy(cls, vacancy):
        new_vacancy = vacancy.as_dict()
        old_data: list[dict] = cls._open_file()
        old_data.append(new_vacancy)
        cls._write_file(old_data)

    @classmethod
    def delete_vacancy(cls, vacancy):
        old_data: list[dict] = cls._open_file()
        for i in old_data:
            if i['link'] == vacancy.link:
                old_data.remove(i)
                print('Профессия была удалена')
                break
        print('Не удалось найти вакансию на удаление')

    @classmethod
    def get_vacancies_by_salary(cls, min_payment: int = 0, max_payment: int = 999_999):
        data = cls._open_file()
        related_vacancies = []

        for vacancy in data:
            if vacancy["payment_from"] >= min_payment or vacancy["payment_to"] <= max_payment:
                related_vacancies.append(vacancy)

    @classmethod
    def _open_file(cls):

        try:
            with open(os.path.join('vacancies.json'), mode='r', encoding='utf-8') as file:
                file = file.read()
            return json.loads(file)

        except FileNotFoundError:
            with open(os.path.join('vacancies.json'), 'w', encoding='utf-8') as file:
                file.write('[]')
            return cls._open_file()

    @classmethod
    def _write_file(cls, old_data: list[dict]):
        new_data = json.dumps(old_data, ensure_ascii=False)

        with open(os.path.join('vacancies.json'), mode='w', encoding='utf-8') as file:
            file.write(new_data)
