

class Vacancies:
    """ Класс для работы с вакансиями """
    def __init__(self, profession, experience, salary_from, salary_to, link, description):
        self.profession = profession
        self.experience = experience
        self.__salary_from = salary_from
        self.__salary_to = salary_to
        self.link = link
        self.description = description
        self.vacancies_list = []

    @property
    def salary(self):
        if self.__salary_from:
            return self.__salary_from
        return self.__salary_to

    def __call__(self):
        self.vacancies_list.append(self)

    def sorted_vacancies(self):
        """
        Метод сортирующий список вакансий по зарплате
        :return: отсортированный список вакансий
        """
        return sorted(self.vacancies_list, key=lambda x: x.salary)
