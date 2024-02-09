import json
import requests
from abc import ABC, abstractmethod


class Api(ABC):
    """Абстрактный класс, определяющий интерфейс для работы с API сайта."""

    @abstractmethod
    def get_vacancies(self, words):
        """Абстрактный метод для получения списка вакансий по ключевым словам."""
        pass