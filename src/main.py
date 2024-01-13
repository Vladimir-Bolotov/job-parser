from src.request_api import SuperJobAPI, HeadHunterAPI
from src.vacancies import Vacancies
from src.working_to_file import save_all_vacancies, save_favorites_vacancies, clear_favorites_vacancies


def user_interaction():
    print('Здравствуйте!')
    user_keyword = input('Введите поисковый запрос\n')

    user_payment = input('Введите желаемую зарплату (Default = None)\n')
    if not user_payment.isdigit():
        user_payment = None
    else:
        user_payment = int(user_payment)

    user_not_agreement_payment = input(
        'Показывать объявление с зарплатой "по договаренности" [Да/Нет] \n'
        '(Default = Не показывать)\n')
    if user_not_agreement_payment.lower() == 'да':
        user_not_agreement_payment = False
    else:
        user_not_agreement_payment = True

    user_experience = input('Требуемый стаж работы  (Default = Без опыта)\n')
    if not user_experience.isdigit():
        user_experience = 0
    else:
        user_experience = int(user_experience)

    superjob_api = SuperJobAPI(user_keyword, user_payment, user_experience, user_not_agreement_payment)
    hh_api = HeadHunterAPI(user_keyword, user_payment, user_experience, user_not_agreement_payment)

    response_sj = superjob_api.search_vacancies()
    response_hh = hh_api.search_vacancies()

    list_vacancies_sj = superjob_api.processing_vacancies(response_sj)
    list_vacancies_hh = hh_api.processing_vacancies(response_hh)
    all_vacancies = list_vacancies_sj + list_vacancies_hh

    save_all_vacancies(all_vacancies)

    list_object_vacancies = []
    for vacancy in all_vacancies:
        object_vacancy = Vacancies(vacancy)
        list_object_vacancies.append(object_vacancy)

    sort_list_object_vacancies = Vacancies.sorted_vacancies_salary(list_object_vacancies)

    user_top = input(f'Введите количество вакансий (от 1 до {len(all_vacancies)})'
                     f'для вывода в топ N \n(Default = 10)\n')
    if not user_top.isdigit():
        user_top = 10
    else:
        user_top = int(user_top)

    favorites_vacancies = []
    for vacancy in sort_list_object_vacancies[:user_top]:
        print(vacancy)
        add_vacancy = input('Если хотите добавить в избранное введите "+" \n')
        if add_vacancy == '+':
            favorites_vacancies.append({'profession': vacancy.profession,
                                        'experience': vacancy.experience,
                                        'salary': vacancy.salary,
                                        'link': vacancy.link,
                                        'description': vacancy.description})
    save_favorites_vacancies(favorites_vacancies)
    clear_user_vacancies = input('Очистить список избранных вакансий? [Да/Нет]')
    if clear_user_vacancies.lower() == 'да':
        clear_favorites_vacancies()


if __name__ == "__main__":
    user_interaction()
