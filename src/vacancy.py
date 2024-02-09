import json

FILE = 'vacancies.json'


class Vacancy:
    """
    Класс для хранения и работы с информацией о вакансиях.
    """

    def __init__(self, title, url, pay, city, employer, requirement) -> None:
        """
        Конструктор класса. Принимает название вакансии, ссылку на вакансию,
        заработную плату, город, работодателя и требования к кандидату.
        """
        self.title = title
        self.url = url
        self.pay = pay
        self.city = city
        self.employer = employer
        self.requirement = requirement