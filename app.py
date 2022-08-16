import configparser
import accinfo


def check_api():
    try:
        config = configparser.ConfigParser()
        config.read('config.ini')
    except FileNotFoundError:
        print('Config file not found.')
        create_app_config()
    else:
        print('Success.')


def create_app_config():
    print('Creating config file...')
    api_key = input('Enter your API key: ')
    with open('config.ini', 'w') as file:
        config = configparser.ConfigParser()
        config['SETTINGS'] = {'api': api_key}
        config.write(file)
    print('Success.')


def create_account():
    name = input('Enter account name (used just for identify in program): ')
    id32 = input('Enter account id in 32-bit format: ')
    account = accinfo.Account(name, id32)
    account.create_config_file()


def use_existing_acc():
    pass
