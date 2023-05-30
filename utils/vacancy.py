import re


class Vacancy:
    """Allows to encapsulate vacancy data in an instance.

    Args:
        vacancy_data (dict[str]): dict with vacancy data.

    Attributes:
        all_vacancies (list[Vacancy]): contains info about all created vacations.
        profession (str): Vacancy profession.
        firm_name (str): Firm, that looks for employee.
        link (str): Job posting link.
        payment_from (int): Start payment value.
        payment_to (int): Finish payment value.
        town (str): Job area.

    """

    all_vacancies = []

    def __init__(self, vacancy_data: dict[str]):
        self.profession = vacancy_data['profession']
        self.firm_name = vacancy_data['firm_name']
        self.link = vacancy_data['link']
        self.payment_from = vacancy_data['payment_from']
        self.payment_to = vacancy_data['payment_to']
        self.town = vacancy_data['town']

        if vacancy_data['description'] is None:
            self.description = 'Без описания'
        else:
            self.description = re.sub(r'(\<(/?[^>]+)>)', '', vacancy_data['description'])

        Vacancy.all_vacancies.append(self)

    def as_dict(self) -> dict:
        """Representing Vacancy instance data as dict.

        Returns:
            dict:

        """
        return {
            "profession": self.profession,
            "firm_name": self.firm_name,
            "description": self.description,
            "payment_from": self.payment_from,
            "payment_to": self.payment_to,
            "town": self.town,
            "link": self.link
        }

    def __repr__(self):
        return f'Vacancy({self.profession}, {self.firm_name}, ' \
               f'{self.payment_from}, {self.payment_to}, ' \
               f'{self.description}, {self.town}, {self.link})'

    def __str__(self):
        return f"{self.profession}\n{self.firm_name}\n" \
               f"{self.payment_from}\n{self.payment_to}\n" \
               f"{self.description}\n{self.town}\n{self.link}\n"

    def __eq__(self, other):
        return self.payment_from == other.payment_from

    def __ne__(self, other):
        return self.payment_from != other.payment_from

    def __lt__(self, other):
        return self.payment_from < other.payment_from

    def __gt__(self, other):
        return self.payment_from > other.payment_from

    def __le__(self, other):
        return self.payment_from <= other.payment_from

    def __ge__(self, other):
        return self.payment_from >= other.payment_from
