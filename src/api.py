import json
import requests
from abc import ABC, abstractmethod


class Api(ABC):
    """Абстрактный класс, определяющий интерфейс для работы с API сайта."""

    @abstractmethod
    def get_vacancies(self, words):
        """Абстрактный метод для получения списка вакансий по ключевым словам."""
        pass


class HeadHunterAPI(Api):
    """Класс для работы с API на hh.ru."""

    def __init__(self, count) -> None:
        """
        Конструктор с входным параметром количества вакансий.
        """
        self.url = 'https://api.hh.ru/vacancies/'
        self.params = {
            'per_page': count,
            'area': 1,
            'page': 1
        }

    def get_vacancies(self, words):
        """
        Метод для получения списка вакансий по ключевым словам с сайта hh.ru.

        Аргументы:
        words - список ключевых слов для поиска вакансий.

        Возвращает:
        vacancies - список вакансий, полученных с сайта hh.ru.
        """
        self.params['text'] = words
        r = requests.get(self.url, params=self.params)
        vacancies = json.loads(r.text)['items']
        return vacancies
