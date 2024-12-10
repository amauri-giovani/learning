import os
import re
import shutil
from datetime import date
from time import sleep


def save_file_without_overwriting(filename: str, name: str, count=0) -> bool:
    """
    Save the xlsx file with the customer's name and date. If the file already exists, the name
    will have a number in parentheses to differentiate it and check if the file has been saved
    :param filename: file name to be saved
    :param customer_name: customer name
    :param count: counter to generate a number if the file with the same name exists
    :return: true if saved or false if there is an error
    """
    renamed_file = filename
    basename = f'{name} - {date.today().strftime("%Y-%m-%d")}'
    while os.path.exists(renamed_file):
        count += 1
        if not renamed_file.startswith('Base SLA'):
            name, extension = filename.split('.')
            renamed_file = '.'.join([basename, extension])
            count = 0
        elif re.search(r'\(\d+\)\.', renamed_file):
            renamed_file = re.sub(r'\(\d+\)\.', f'({count}).', renamed_file)
        else:
            name, extension = renamed_file.split('.')
            renamed_file = f'{name} ({count}).{extension}'

    shutil.move(filename, renamed_file)

    check = False
    for number in range(30):
        if not os.path.exists(renamed_file):
            sleep(1)
        else:
            check = True
            break
    return check