import configparser
import os

import service
import rqsts


class Account:

    name = service.Name()
    id32 = service.ID()
    id64 = service.ID()

    def __init__(self, name=None, id32=None, *, id64=None):
        self.name = name
        self.id32 = id32  # for opendota api
        self.id64 = id64  # for steam api

    def get_id(self):
        try:
            self.id64 = rqsts.get_player_info(self.id32)['profile']['steamid']
            return self.id64
        except ValueError:
            print(f"SteamID32 is not set in account '{self.name}'")

    def save_to_config(self):  # TODO rewrite
        """save account attributes to config"""
        config = configparser.ConfigParser()
        attributes = tuple(filter(lambda w: w[0] != '_', dir(self)))
        values = tuple(map(lambda attr: getattr(self, attr), attributes))
        config['ACCOUNT INFO'] = {key: value for key, value in zip(attributes, values)}
        with open(f'configs/{self.name}.ini', 'w') as file:
            config.write(file)

    def create_db(self):  # TODO
        pass


def set_steam_api_key(key):
    os.environ['STEAM_API_KEY'] = key
