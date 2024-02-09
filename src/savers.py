import json
import os
from src.vacancy import Vacancy

FILE = 'vacancies.json'


class JsonAgent:
    """
    Класс для работы с данными json файла: 'vacancies.json'.
    """

    @staticmethod
    def is_vacancy_present(vacancy: Vacancy):
        """
        Метод проверяет, существует ли уже данная вакансия в файле json.
        Возвращает False, если вакансия уже существует, и True в противном случае.
        """

        try:
            with open(FILE, 'r', encoding='utf-8') as f:
                vacancies = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            vacancies = []  # Если файл не существует или пуст, создаем пустой список вакансий.

        for v in vacancies:
            if v['title'] == vacancy.title and v['url'] == vacancy.url and \
                    v['pay'] == vacancy.pay and v['city'] == vacancy.city and \
                    v['employer'] == vacancy.employer and v['requirement'] == vacancy.requirement:
                return False  # Вакансия уже существует, не добавляем ее.

        return True  # Вакансии с такими данными нет, можно добавить.