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

    def to_dict(self):
        """
        Метод возвращает информацию о вакансии в виде словаря
        """
        return {
            'title': self.title,
            'url': self.url,
            'pay': self.pay,
            'city': self.city,
            'employer': self.employer,
            'requirement': self.requirement,
        }

    @classmethod
    def from_dict(cls, params):
        """
        Классовый метод, который создает объект вакансии на основе словаря.
        """
        return cls(params['title'], params['url'], params['pay'], params['city'], params['employer'],
                   params['requirement'])
