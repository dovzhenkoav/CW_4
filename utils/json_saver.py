import os
import json

from utils.abstractclasses import AbstractJSONSaver


class JSONSaver(AbstractJSONSaver):
    """Allows to manage vacancy's data JSON file.

    Args:
        existing_data_deleted (bool): flag, that allows to delete existing
            data before new search.

    """

    existing_data_deleted = False

    @classmethod
    def add_vacancy(cls, vacancy):
        """Add vacancy in JSON file.

        Args:
            vacancy (Vacancy): An instance of Vacancy class.
        """
        new_vacancy = vacancy.as_dict()
        old_data: list[dict] = cls._open_file()
        old_data.append(new_vacancy)
        cls._write_file(old_data)

    @classmethod
    def delete_vacancy_by_link(cls, link: str):
        """Delete vacancy if JSON file.

        Args:
            link (str): Job post link.

        """
        old_data: list[dict] = cls._open_file()
        for i in old_data:
            if i['link'] == link:
                old_data.remove(i)
                print('Профессия была удалена')
                return None
        print('Не удалось найти вакансию на удаление')

    @classmethod
    def get_vacancies_by_salary(cls, min_payment: int = 0,
                                max_payment: int = 999_999) -> list[dict]:
        """Get vacancies from JSOn file with min/max payment filter.

        Args:
            min_payment (int): Filter for minimal payment value
            max_payment (int): Filter for maximum payment value

        Returns:
            list[dict]: Returns all appropriate vacancies by min/max payment.

        """
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
        """Delete existing JSON data in project directory."""
        if os.path.exists('vacancies.json'):
            os.remove(os.path.join('vacancies.json'))
        cls.existing_data_deleted = True

    @classmethod
    def get_top_vacancies(cls, top_n: int) -> list[dict]:
        """Get `top_n` number vacancies by `min_payment` from JSON file.

        Args:
            top_n (int): required len of top.

        Returns:
            list[dict]

        """
        data = cls._open_file()
        top_vacancies = sorted(data, key=lambda x: x['payment_from'], reverse=True)[:top_n]
        return top_vacancies
