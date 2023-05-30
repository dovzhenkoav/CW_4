from abc import ABC, abstractmethod


class AbstractAPI(ABC):
    """Abstract class, that define what methods should use API classes"""

    @abstractmethod
    def get_vacancies(self, required_vacancy: str):
        pass


class AbstractJSONSaver(ABC):
    """Abstract class, that define what methods should use JSONSaver class"""

    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def delete_vacancy_by_link(self, link: str):
        pass

    @abstractmethod
    def get_vacancies_by_salary(self, min_payment: int, max_payment: int):
        pass

    @classmethod
    @abstractmethod
    def delete_existing_data(cls):
        pass

    @classmethod
    @abstractmethod
    def get_top_vacancies(cls, top_n: int):
        pass

    @classmethod
    @abstractmethod
    def _open_file(cls):
        pass

    @classmethod
    @abstractmethod
    def _write_file(cls, old_data: list[dict]):
        pass
