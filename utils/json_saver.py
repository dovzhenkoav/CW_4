import os
import json

from utils.abstractclasses import AbstractJSONSaver


class JSONSaver(AbstractJSONSaver):
    existing_data_deleted = False

    @classmethod
    def add_vacancy(cls, vacancy):
        new_vacancy = vacancy.as_dict()
        old_data: list[dict] = cls._open_file()
        old_data.append(new_vacancy)
        cls._write_file(old_data)

    @classmethod
    def delete_vacancy_by_link(cls, link: str):
        old_data: list[dict] = cls._open_file()
        for i in old_data:
            if i['link'] == link:
                old_data.remove(i)
                print('Профессия была удалена')
                return None
        print('Не удалось найти вакансию на удаление')

    @classmethod
    def get_vacancies_by_salary(cls, min_payment: int = 0, max_payment: int = 999_999):
        data = cls._open_file()
        related_vacancies = []

        for vacancy in data:
            if vacancy["payment_from"] >= min_payment and vacancy["payment_to"] <= max_payment:
                related_vacancies.append(vacancy)
        return related_vacancies

    @classmethod
    def _open_file(cls):
        if not cls.existing_data_deleted:
            cls.delete_existing_data()

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

    @classmethod
    def delete_existing_data(cls):
        if os.path.exists('vacancies.json'):
            os.remove(os.path.join('vacancies.json'))
        cls.existing_data_deleted = True

    @classmethod
    def get_top_vacancies(cls, top_n: int):
        data = cls._open_file()
        top_vacancies = sorted(data, key=lambda x: x['payment_from'], reverse=True)[:top_n]
        return top_vacancies
