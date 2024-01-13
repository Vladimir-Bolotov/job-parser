class Vacancies:
    """ Класс для работы с вакансиями """

    def __init__(self, vacancy):
        self.profession = vacancy['profession']
        self.experience = vacancy['experience']
        self.__salary_from = vacancy['salary_from']
        self.__salary_to = vacancy['salary_to']
        self.link = vacancy['link']
        self.description = vacancy['description']

    def __str__(self):
        if not self.__salary_from:
            self.__salary_from = 0

        if not self.__salary_to:
            self.__salary_to = 'и больше'

        if not self.description:
            self.description = 'Описание нет'

        snippet = f'Специальность: {self.profession}\n' \
            f'Стаж: {self.experience}\n' \
            f'Зарплата: {self.__salary_from} - {self.__salary_to}\n' \
            f'Ссылка: {self.link}\n' \
            f'Описание: {self.description[:100]}...\n'

        return snippet

    @property
    def salary(self):
        if self.__salary_from:
            return self.__salary_from
        return self.__salary_to

    @staticmethod
    def sorted_vacancies_salary(vacancies_list):
        """
        Метод сортирующий список вакансий по зарплате
        :return: отсортированный список вакансий
        """
        return sorted(vacancies_list, key=lambda x: x.salary, reverse=True)
