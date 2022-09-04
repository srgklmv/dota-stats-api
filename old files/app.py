import configparser


def create_app_config():
    print('Creating config file...')
    api_key = input('Enter your API key: ')
    with open('../config.ini', 'w') as file:
        config = configparser.ConfigParser()
        config['SETTINGS'] = {'api': api_key}
        config.write(file)
    print('Config file created.')


def check_api():
    try:
        with open('../config.ini', 'r') as file:
            config = configparser.ConfigParser()
            config.read(file)
    except FileNotFoundError:
        print('Config file not found.')
        create_app_config()
    else:
        print('Config file found.')


def action_menu(): # TODO

    actions = {
        '1': 'accounts_management()',
        '2': 'stats_management()',
        '3': 'change_api_key()',
        '4': check_api()
    }

    print('# Action menu #')
    action_key = input()
    actions[action_key]

action_menu()