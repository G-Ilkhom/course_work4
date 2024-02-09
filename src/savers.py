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

    @staticmethod
    def add_vacancy(vacancy: Vacancy):
        """
        Метод добавляет вакансию в файл json.
        Возвращает True, если вакансия была успешно добавлена, и False в противном случае.
        """

        if not os.path.exists(FILE):
            with open(FILE, 'w', encoding='utf-8') as f:
                json.dump([], f)
                print("Файл vacancies.json был создан.")

        # проверка корректности файла vacancies.json
        if JsonAgent.is_vacancy_present(vacancy):
            with open(FILE, 'r', encoding='utf-8') as f:
                try:
                    vacancies = json.load(f)
                except json.JSONDecodeError:
                    print("Файл vacancies.json поврежден. Создан новый файл.")
                    with open(FILE, 'w', encoding='utf-8') as new_f:
                        json.dump([], new_f)
                    vacancies = []

            vacancy_dict = vacancy.to_dict()  # преобразование вакансии в словарь
            vacancies.append(vacancy_dict)  # добавление вакансии в файл
            with open(FILE, 'w', encoding='utf-8') as f:
                json.dump(vacancies, f, ensure_ascii=False, indent=4)
            return True
        else:
            print("Произошла ошибка при добавлении вакансии")
            return False

    @staticmethod
    def delete_vacancy_by_title(title):
        """
        Метод удаляет вакансию из файла json по её названию.
        Возвращает True, если вакансия найдена и удалена, иначе False.
        """

        try:
            with open(FILE, 'r', encoding='utf-8') as f:
                vacancies = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            print("Произошла ошибка при загрузке вакансий.")
            return False

        f = False
        for vacancy in vacancies:
            if vacancy['title'] == title:
                vacancies.remove(vacancy)
                f = True
                break
        if f:
            with open(FILE, 'w', encoding='utf-8') as f:
                json.dump(vacancies, f, ensure_ascii=False)
            return True
        else:
            return False
