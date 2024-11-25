from collections import defaultdict

import requests
from bs4 import BeautifulSoup
import csv

url = ("https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D"
       "1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83")


def get_html(page_url):
    page = requests.get(page_url).text
    soup = BeautifulSoup(page, 'lxml')
    return soup


def get_categories(page_url):
    animals = defaultdict(int)
    next_page_url = page_url

    while next_page_url:
        soup = get_html(next_page_url)
        groups = soup.find('div', class_='mw-category mw-category-columns').find_all(
            'div',
            class_='mw-category-group')
        for group in groups:
            current_group_letter = group.find('h3').text
            animal_tags = group.find_all('a')
            animals[current_group_letter] += len(animal_tags)

        new_tag = soup.find("a", string="Следующая страница")
        if new_tag is not None:
            next_page_url = f'https://ru.wikipedia.org{new_tag.get("href")}'
        else:
            next_page_url = None

    return animals


def main():
    animals_groups = get_categories(url)
    with open('beasts.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        for letter, amount in animals_groups.items():
            row = (letter, amount)
            csvwriter.writerow(row)


if __name__ == '__main__':
    main()
