# HW_Lesson4_Task4-utils
import requests
from decimal import *
from datetime import datetime


def currency_rates(code_val):
    code_val = code_val.upper()
    all_xml = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text

    if code_val not in all_xml:
        return f'Указанной валюты нет в списке ответа!'

    desired_val = all_xml[all_xml.find('<Value>', all_xml.find(code_val)) + 7:
                          all_xml.find('</Value>', all_xml.find(code_val))]
    search_date = all_xml[all_xml.find('Date="') + 6:all_xml.find('Date="') + 16].split('.')
    day, month, year = map(int, search_date)
    return f"На {datetime(day=day, month=month, year=year).date()}:\n1 {code_val} = " \
           f"{Decimal(desired_val.replace(',', '.'))} руб"


if __name__ == '__main__':
    code_val = input('L4_T4-utils\nВведи код валюты:\n')
    print(currency_rates(code_val))