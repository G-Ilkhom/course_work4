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


def show_vacancies_by_title():
    """
     Метод выводит в консоль названия всех вакансий, сохраненных в файле 'vacancies.json'.
    """
    JsonAgent.show_vacancies_title()


def delete_vacancy_by_title():
    """
    Метод удаляет вакансию из файла 'vacancies.json' по названию вакансии.
    """
    title = input('Введите название вакансии для удаления: ')
    if JsonAgent.delete_vacancy_by_title(title):
        print(f'Вакансия {title} удалена')
    else:
        print(f'Вакансия {title} не найдена')


def clear_json():
    """
    Метод очищает файл 'vacancies.json', удаляя все сохраненные вакансии.
    """
    JsonAgent.clear_json()


def show_info_by_title():
    """
    Метод выводит в консоль информацию о вакансии, найденной по названию в файле 'vacancies.json'.
    """
    title = input('Введите название вакансии для вывода информации: ')
    JsonAgent.show_info_by_title(title)


def get_vacancies_by_k_words():
    """
    Метод выводит в консоль названия вакансий, которые соответствуют заданным ключевым словам.
    """
    keywords = input('Введите ключевые слова для поиска: ').split()
    vacancies = Vacancy.from_json()
    filtered = VacancyAgent.get_vacancies_by_keywords(vacancies, keywords)
    if len(filtered) > 0:
        for title, pay in filtered:
            print(f"{title}, зарплата: {pay} руб/мес")
    else:
        print('Вакансий по таким словам не найдено')


def get_vacancies_by_salary():
    """
    Метод выводит в консоль названия вакансий, заработная плата по которым находится в заданном диапазоне.
    """
    while True:
        try:
            salary_from = int(input('Введите заработную плату от: '))
            salary_to = int(input('Введите заработную плату до: '))
            if salary_to < salary_from:
                print(f"Ошибка: заработная плата не может быть от {salary_from} до {salary_to}")
            else:
                break
        except ValueError:
            print("Ошибка: введите целое число.")
    vacancies = Vacancy.from_json()
    filtered = VacancyAgent.get_vacancies_by_salary(vacancies, salary_from, salary_to)
    if len(filtered) > 0:
        for title, pay in filtered:
            print(f"{title}, зарплата: {pay} руб/мес")
    else:
        print('Вакансий по такому диапазону зарплаты не найдено')


def sort_vacancies_by_salary():
    """
    Метод сортирует вакансии по заработной плате в порядке убывания и сохраняет их в файл 'vacancies.json'.
    """
    vacancies = Vacancy.from_json()
    vacancies = sorted(vacancies, key=lambda x: int(x.pay), reverse=True)
    JsonAgent.clear_json()
    for vacancy in vacancies:
        JsonAgent.add_vacancy(vacancy)
    print('Файл отсортирован')
