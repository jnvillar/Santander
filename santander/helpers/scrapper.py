import requests
from bs4 import BeautifulSoup as bs

from santander.config import scrapperConfig


def contains(mount, word):
    return str(mount).find(word) == -1


def format_list(unformatted_list):
    for i in range(len(unformatted_list)):
        unformatted_list[i] = unformatted_list[i].find(text=True)
        unformatted_list[i] = unformatted_list[i].strip()
        unformatted_list[i] = unformatted_list[i].replace('(', '-')
        unformatted_list[i] = unformatted_list[i].replace(')', '')
        unformatted_list[i] = unformatted_list[i].replace('.', '')
        unformatted_list[i] = unformatted_list[i].replace(',', '.')
    return unformatted_list


def to_int(to_int_list):
    for i in range(len(to_int_list)):
        to_int_list[i] = float(to_int_list[i])
    return to_int_list


class Scrapper:
    def __init__(self):
        self.url = scrapperConfig.url
        session = requests.session()
        resp = session.get(self.url)
        self.soup = bs(resp.text, "html.parser")

    def get_investment_founds(self):
        investment_found_names = self.soup.find_all('td', {'align': 'left',
                                                           'style': 'border-width:0px; padding: 1px; background-color:transparent;'})
        return format_list(investment_found_names)

    def get_investment_founds_today_values(self):
        values = self.soup.find_all('td', {'align': 'right', 'class': ''})
        values = [value for value in values if contains(value, 'style')]
        format_list(values)
        to_int(values)
        return values

