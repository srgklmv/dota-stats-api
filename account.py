import configparser
import requests as re
import os
import sqlite3


class Account:

    def __init__(self, name=None, id32=None, vanity_url=None):
        self.name = name
        self.id32 = id32
        self.vanity_url = vanity_url

    def get_id(self):
        """This id is not working in opendota"""
        acc_name = self.vanity_url.rstrip('/ ').split('/')[-1]
        api_key = os.getenv('STEAM_API_KEY')

        params = {
            'key': api_key,
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

    def create_db(self):
        pass


def set_steam_api_key(key):
    os.environ['STEAM_API_KEY'] = key
