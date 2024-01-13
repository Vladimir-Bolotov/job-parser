import os
from abc import ABC, abstractmethod

import requests

SUPERJOB_API_KEY = os.environ.get('SUPERJOB_API_KEY')


class WebsiteVacanciesAPI(ABC):
    @abstractmethod
    def search_vacancies(self):
        """
        Отправляет API запрос с указанными параметрами
        :return: возвращает словарь с вакансиями
        """
        pass

    @abstractmethod
    def processing_vacancies(self, vacancies):
        """
        Достает из словаря с вакансиями необходимые параметры
        :param vacancies: словарь с вакансиями
        :return: список вакансий с необходимыми параметрами
        """
        pass


class SuperJobAPI(WebsiteVacanciesAPI):
    """Класс для работы с API api.superjob.ru"""

    def __init__(self, keyword: str, payment_from: int, experience: int, no_agreement: int):
        self.keyword = keyword
        self.payment_from = payment_from
        self.no_agreement = no_agreement
        self.count = 100

        if experience == 0:
            self.experience = 1
        elif 1 < experience < 3:
            self.experience = 2
        elif 3 <= experience < 6:
            self.experience = 3
        else:
            self.experience = 4

        self.url = 'https://api.superjob.ru/2.0/vacancies/'

    def search_vacancies(self):
        headers = {'X-Api-App-Id': SUPERJOB_API_KEY}
        params = {'keyword': self.keyword,
                  'payment_from': self.payment_from,
                  'experience': self.experience,
                  'no_agreement': self.no_agreement,
                  'count': self.count}
        response = requests.get(self.url, params=params, headers=headers)

        return response.json()

    def processing_vacancies(self, vacancies):
        list_vacancies = list()
        for vacancy in vacancies['objects']:
            job_data = {
                'profession': vacancy['profession'],
                'experience': vacancy['experience']['title'],
                'salary_from': vacancy['payment_from'],
                'salary_to': vacancy['payment_to'],
                'link': vacancy['link'],
                'description': vacancy['candidat']}
            list_vacancies.append(job_data)
        return list_vacancies


class HeadHunterAPI(WebsiteVacanciesAPI):
    """Класс для работы с API api.hh.ru"""

    def __init__(self, text: str, salary: int, experience: int, only_with_salary):
        self.text = text
        self.salary = salary
        self.only_with_salary = only_with_salary
        self.per_page = 100

        if experience == 0:
            self.experience = 'noExperience'
        elif 0 < experience < 3:
            self.experience = 'between1And3'
        elif 3 <= experience < 6:
            self.experience = 'between3And6'
        else:
            self.experience = 'moreThan6'

        self.url = 'https://api.hh.ru/vacancies'

    def search_vacancies(self):
        params = {'text': self.text,
                  'salary': self.salary,
                  'experience': self.experience,
                  'only_with_salary': self.only_with_salary,
                  'per_page': self.per_page
                  }
        response = requests.get(self.url, params=params)

        return response.json()

    def processing_vacancies(self, vacancies):
        list_vacancies = list()

        for vacancy in vacancies['items']:
            try:
                job_data = {
                    'profession': vacancy['name'],
                    'experience': vacancy['experience']['name'],
                    'salary_from': vacancy['salary']['from'],
                    'salary_to': vacancy['salary']['to'],
                    'link': vacancy['alternate_url'],
                    'description': vacancy['snippet']['responsibility']}
                list_vacancies.append(job_data)
            except TypeError:
                continue
        return list_vacancies
        
