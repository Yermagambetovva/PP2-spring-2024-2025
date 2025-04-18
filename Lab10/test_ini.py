from configparser import ConfigParser
import os

def load_config(filename='database.ini', section='postgresql'):
    print("Текущая директория:", os.getcwd())
    print("Ожидается ini-файл:", os.path.abspath(filename))

    parser = ConfigParser()
    parser.read(filename)

    print("parser.read вернул:", parser.sections())  #покажет найденные секции

    if parser.has_section(section):
        return {param[0]: param[1] for param in parser.items(section)}
    else:
        raise Exception(f'Section {section} not found in the {filename} file')

load_config()
