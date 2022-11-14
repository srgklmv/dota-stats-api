import configparser
import requests as re


class Account:

    API_KEY = None

    def __init__(self, name=None, id32=None, vanity_url=None):
        self.name = name
        self.id32 = id32
        self.vanity_url = vanity_url

    def get_id(self):
        acc_name = self.vanity_url.rstrip('/ ').split('/')[-1]

        params = {
            'key': self.API_KEY,
            'vanityurl': acc_name
        }

        request = re.get('https://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/',
                         params=params)

        self.id32 = request.json()['response']['steamid']

    def save_to_config(self):  # TODO rewrite to save only useful data
        """save account attributes to config"""
        config = configparser.ConfigParser()
        attributes = tuple(filter(lambda w: w[0] != '_', dir(self)))
        values = tuple(map(lambda attr: getattr(self, attr), attributes))
        config['ACCOUNT INFO'] = {key: value for key, value in zip(attributes, values)}
        with open(f'configs/{self.name}.ini', 'w') as file:
            config.write(file)

    @classmethod
    def set_steam_api_key(cls, key):
        cls.API_KEY = key


def create_account():
    name = input('Enter account name (used just for identify in program): ')
    id32 = input('Enter account id in 32-bit format: ')
    account = Account(name, id32)
    account.save_to_config()
    print("Account successfully created.")
