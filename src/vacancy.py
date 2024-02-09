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

    @classmethod
    def from_json(cls):
        """
        Классовый метод, который создает список объектов вакансий на основе информации из json файла.
        """
        with open(FILE, 'r', encoding='utf-8') as f:
            vacancies = json.load(f)
        vacancy_list = []
        for vacancy in vacancies:
            tmp = Vacancy.from_dict(vacancy)
            vacancy_list.append(tmp)
        return vacancy_list
