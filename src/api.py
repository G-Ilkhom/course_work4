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