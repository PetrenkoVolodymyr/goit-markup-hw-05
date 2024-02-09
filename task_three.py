import os
import sys
import pathlib
import re
from datetime import datetime
from collections import Counter

def load_logs(adress):
    if os.path.exists(adress):
        with open(adress, 'r', encoding='utf-8-sig') as f:
            lines = f.readlines()
            return lines
    else:
        print('The specified file does NOT exist')


def parse_log_line(lines: str):
    list = []
    for line in lines:
        dict ={}

        date_string = re.search(r'\d+\-\d+\-\d+',line).group()
        date_date = datetime.strptime(date_string, "%Y-%m-%d").date()

        time_string = re.search(r'\d+[:]\d+[:]\d+',line).group()
        date_time = datetime.strptime(time_string, "%H:%M:%S").time()

        error_type = re.search(r'[A-Z]+',line).group()

        error_disc = re.search(r'[A-Z][a-z]\D+[^\n]',line).group()

        dict['date'] = date_date
        dict['time'] = date_time
        dict['type'] = error_type
        dict['discription'] = error_disc
        
        list.append(dict)
    return list


def count_logs_by_level(list):
    errors_dict = Counter([d['type'] for d in list])
    return(errors_dict)


def display_log_counts(errors_dict):
    print(f'Рівень логування | Кількість')
    print('_ _ _ _ _ _ _ _ _| _ _ _ _ _ ') 
    for key, value in errors_dict.items():
        print(f'{key}\t\t | {value}')


def filter_logs_by_level(list, level):
    print(f'Деталі логів для рівня {level}:')
    for item in list:
        if item['type']==level:
            print(f'{item['date']} {item['time']} - {item['discription']}')



try:
    input = sys.argv[1]
    adress= pathlib.Path(input)
    lines = load_logs(adress)
    dict_lines = parse_log_line(lines)
    conuted_logs = count_logs_by_level(dict_lines)
    display_log_counts(conuted_logs)

    log_level = sys.argv[2]
    if log_level.upper() in conuted_logs.keys():
        filter_logs_by_level(dict_lines, log_level.upper())
    else:
        print('Некоректний параметр логування')
except:
    pass
