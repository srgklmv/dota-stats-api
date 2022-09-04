import configparser
import os


class Account:

    def __init__(self, name=None, id32=None):
        self.name = name
        self.id32 = id32

    def save_to_config(self):  # TODO rewrite to save only useful data
        """save account attributes to config"""
        config = configparser.ConfigParser()
        attributes = tuple(filter(lambda w: w[0] != '_', dir(self)))
        values = tuple(map(lambda attr: getattr(self, attr), attributes))
        config['ACCOUNT INFO'] = {key: value for key, value in zip(attributes, values)}
        with open(f'configs/{self.name}.ini', 'w') as file:
            config.write(file)

    def load_from_config(self, name):  # with or without ini (account name or file name) TODO
        pass

    def get_match_history(self):  # add restrictions to class object TODO
        pass

    def load_id(self):  # parse from web service TODO
        pass


def create_account():
    name = input('Enter account name (used just for identify in program): ')
    id32 = input('Enter account id in 32-bit format: ')
    account = Account(name, id32)
    account.save_to_config()
    print("Account successfully created.")


def check_for_accounts():
    print('Try to find existing accounts...')
    configs = filter(lambda n: n.endswith('.ini'), os.listdir('configs'))
    if configs:
        print('Accounts were find. Full list here:')
        print(*configs, sep='\n')
    else:
        print("Can't find any existing account. Creating now.")
        create_account()
        super()
