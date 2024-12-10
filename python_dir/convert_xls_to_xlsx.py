import os
import subprocess


dirname = ''

def convert_xls_to_xlsx() -> None:
    """
    Convert xls file to xlsx
    :param file_xls: xls file name to be converted to xlsx
    :return: xlsx file if converted or xls file if error
    """
    os.chdir('')

    for file_xls in os.listdir():
        try:
            if file_xls.endswith('xls'):
                subprocess.run(['libreoffice', '--convert-to', 'xlsx', f'{file_xls}', '--headless'])

        except:
            continue
    check_convert_files()


def check_convert_files():
    os.chdir(dirname)
    # TODO fazer essa lógica
    for filename in os.listdir():
        if f'{filename}.xlsx' in os.listdir():
            if f'{filename}.xls' in os.listdir():
                os.unlink(f'{filename}.xls')
