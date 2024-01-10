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


class SuperJobAPI(WebsiteVacanciesAPI):
    """Класс для работы с API api.superjob.ru"""

    def __init__(self, keyword: str, payment_from: int = None, experience: int = None, no_agreement: int = 1):
        self.keyword = keyword
        self.payment_from = payment_from
        self.experience = experience
        self.no_agreement = no_agreement
        self.url = 'https://api.superjob.ru/2.0/vacancies/'

    def search_vacancies(self):
        headers = {'X-Api-App-Id': SUPERJOB_API_KEY}
        params = {'keyword': self.keyword,
                  'payment_from': self.payment_from,
                  'experience': self.experience,
                  'no_agreement': self.no_agreement}
        response = requests.get(self.url, params=params, headers=headers)

        return response.json()


class HeadHunterAPI(WebsiteVacanciesAPI):
    """Класс для работы с API api.hh.ru"""
    def __init__(self, text: str, salary: int = None, experience: str = None, only_with_salary=True):
        self.text = text
        self.salary = salary
        self.experience = experience
        self.only_with_salary = only_with_salary
        self.url = 'https://api.hh.ru/vacancies'

    def search_vacancies(self):
        params = {'text': self.text,
                  'salary': self.salary,
                  'experience': self.experience,
                  'only_with_salary': self.only_with_salary
                  }
        response = requests.get(self.url, params=params)

        return response.json()
