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

    def show_info(self):
        """
        Метод, который выводит в консоль информацию о вакансии.
        """
        print(self.title)
        print(self.url)
        print(self.pay)
        print(self.city)
        print(self.employer)
        print(self.requirement)

    def __repr__(self) -> str:
        """
        Метод для представления объекта вакансии в виде строки.
        """
        return f"{self.__class__.__name__}\n({self.title}\n{self.pay}\n{self.url}\n{self.city}\n{self.employer}\n{self.requirement})"

    def __eq__(self, other):
        """
        Метод для сравнения двух вакансий по заработной плате (равенство).
        """
        return self.pay == other.pay

    def __ne__(self, other):
        """
        Метод для сравнения двух вакансий по заработной плате (неравенство).
        """
        return self.pay != other.pay

    def __lt__(self, other):
        """
        Метод для сравнения двух вакансий по заработной плате (меньше).
        """
        return self.pay < other.pay

    def __gt__(self, other):
        """
        Метод для сравнения двух вакансий по заработной плате (больше).
        """
        return self.pay > other.pay


class VacancyAgent:
    """Класс для обработки информации о вакансиях."""

    @staticmethod
    def pars_hh_ru(vacancies):
        """
        Метод, который получает на вход словарь из hh.ru и возвращает массив Vacancy
        """
        vacancies_list = []
        url_hh_v = 'https://hh.ru/vacancy/'
        for vacancy in vacancies:
            if vacancy['salary'] is not None:
                if vacancy['salary']['from'] is not None:
                    tmp = Vacancy(vacancy['name'], f'{url_hh_v}{vacancy["id"]}', vacancy['salary']['from'],
                                  vacancy['area']['name'], vacancy['employer']['name'],
                                  vacancy['snippet']['requirement'])
                else:
                    tmp = Vacancy(vacancy['name'], f'{url_hh_v}{vacancy["id"]}', vacancy['salary']['to'],
                                  vacancy['area']['name'], vacancy['employer']['name'],
                                  vacancy['snippet']['requirement'])
            else:
                tmp = Vacancy(vacancy['name'], f'{url_hh_v}{vacancy["id"]}', "0",
                              vacancy['area']['name'], vacancy['employer']['name'], vacancy['snippet']['requirement'])
            vacancies_list.append(tmp)
        return vacancies_list
