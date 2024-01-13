import json


def save_all_vacancies(vacancies):
    """Записывает в файл все найденные вакансии"""
    with open('vacancies.json', 'w', encoding='utf-8') as file:
        json.dump(vacancies, file, indent=1, ensure_ascii=False)


def save_favorites_vacancies(favorites_vacancies):
    """Записывает в файл избранные вакансии"""
    try:
        with open('favorites_vacancies.json') as file:
            read_file = json.load(file)
        with open('favorites_vacancies.json', 'w', encoding='utf-8') as file:
            all_favorites_vacancies = read_file + favorites_vacancies
            json.dump(all_favorites_vacancies, file, indent=1)
    except FileNotFoundError:
        with open('favorites_vacancies.json', 'w', encoding='utf-8') as file:
            json.dump(favorites_vacancies, file, indent=1)

def clear_favorites_vacancies():
    """Стерает из файла все избранные вакансии"""
    with open('favorites_vacancies.json', 'w', encoding='utf-8') as file:
        json.dump('', file, indent=1, ensure_ascii=False)