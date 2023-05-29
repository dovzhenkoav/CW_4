class Vacancy:
    all_vacancies = []

    def __init__(self, vacancy_data: dict[str]):
        self.profession = vacancy_data['profession']
        self.firm_name = vacancy_data['firm_name']
        self.link = vacancy_data['link']
        self.payment_from = vacancy_data['payment_from']
        self.payment_to = vacancy_data['payment_to']
        self.description = vacancy_data['description']
        self.town = vacancy_data['town']

        Vacancy.all_vacancies.append(self)

    def as_dict(self):
        return {
            "profession": self.profession,
            "firm_name": self.firm_name,
            "link": self.link,
            "description": self.description,
            "payment_from": self.payment_from,
            "payment_to": self.payment_to,
            "town": self.town
        }

    def __repr__(self):
        return f'Vacancy{(self.profession, self.firm_name, self.link, self.payment_from, self.payment_to, "self.description", self.town)}'

    def __eq__(self, other):
        return self.payment == other.payment

    def __ne__(self, other):
        return self.payment != other.payment

    def __lt__(self, other):
        return self.payment < other.payment

    def __gt__(self, other):
        return self.payment > other.payment

    def __le__(self, other):
        return self.payment <= other.payment

    def __ge__(self, other):
        return self.payment >= other.payment
