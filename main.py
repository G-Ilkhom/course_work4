import json
import os

from src.api import HeadHunterAPI
from src.savers import JsonAgent
from src.vacancy import Vacancy, VacancyAgent


def load_vacancies_to_json():
    """
    Метод запрашивает у пользователя количество вакансий и ключевые слова.
    Добавляет найденные вакансии в файл 'vacancies.json'.
    """
    while True:
        try:
            hh_vacancies_count = int(input('Введите количество вакансий(сайт hh.ru): '))
        except ValueError:
            print("Ошибка: введите целое число.")
        else:
            if hh_vacancies_count <= 100:
                break

    search_words = input('Введите ключевые слова для поиска: ').split()

    # Инициализация JSON-файла, если он не существует
    if not os.path.exists("vacancies.json"):
        with open("vacancies.json", "w", encoding="utf-8") as file:
            json.dump([], file)

    hh_api = HeadHunterAPI(hh_vacancies_count)

    hh_vacancies = VacancyAgent.pars_hh_ru(hh_api.get_vacancies(search_words))

    counter = 0
    for vacancy in hh_vacancies:
        if JsonAgent.add_vacancy(vacancy):
            counter += 1
    print(f'Добавлено {counter} вакансий')