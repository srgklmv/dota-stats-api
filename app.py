import configparser
import accinfo
import os


def create_app_config():
    print('Creating config file...')
    api_key = input('Enter your API key: ')
    with open('config.ini', 'w') as file:
        config = configparser.ConfigParser()
        config['SETTINGS'] = {'api': api_key}
        config.write(file)
    print('Config file created.')


def check_api():
    try:
        with open('config.ini', 'r') as file:
            config = configparser.ConfigParser()
            config.read(file)
    except FileNotFoundError:
        print('Config file not found.')
        create_app_config()
    else:
        print('Config file found.')


def create_account():
    name = input('Enter account name (used just for identify in program): ')
    id32 = input('Enter account id in 32-bit format: ')
    account = accinfo.Account(name, id32)
    account.create_config_file()
    print("Account succesfuly created.")


def check_for_accounts():
    print('Try to find existing accounts...')
    configs = filter(lambda n: n.endswith('.ini'), os.listdir('configs'))
    if configs:
        print('Accounts were find. Full list here:')
        print(*configs, sep='\n')
        # action_menu() TODO
    else:
        print("Can't find any existing account. Creating now.")
        create_account()


def use_existing_acc():
    pass
