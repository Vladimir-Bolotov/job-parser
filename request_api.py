
import os
from abc import ABC, abstractmethod

import requests

SUPERJOB_API_KEY = os.environ.get('SUPERJOB_API_KEY')


class WebsiteVacanciesAPI(ABC):
    @abstractmethod
    def search_vacancies(self):
        pass


class SuperJobAPI(WebsiteVacanciesAPI):

    def __init__(self, keyword: str = None, town: str = None, payment_from: int = 0,
                 payment_to: int = 0, vacancies_count: int = 0, experience: int = None):
        self.keyword = keyword
        self.town = town
        self.payment_from = payment_from
        self.payment_to = payment_to
        self.vacancies_count = vacancies_count
        self.experience = experience
        self.url = 'https://api.superjob.ru/2.0/'

    def search_vacancies(self):
        headers = {'X-Api-App-Id': SUPERJOB_API_KEY}
        params = {'keyword': self.keyword,
                  'payment_from': self.payment_from,
                  'payment_to': self.payment_to,
                  'town': self.town,
                  'count': self.vacancies_count,
                  'experience': self.experience}

        response = requests.get(self.url + 'vacancies/', params=params, headers=headers)

        return response
