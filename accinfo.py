import configparser


# user class and following methods to create and store user data such as acc id, api key, etc.
class Account:

    def __init__(self, name, id32):
        self.name = name
        self.id32 = id32

    def create_config_file(self):
        config = configparser.ConfigParser()
        attributes = tuple(filter(lambda w: w[0] != '_', dir(self)))
        values = tuple(map(lambda attr: getattr(self, attr), attributes))
        config['ACCOUNT INFO'] = {key: value for key, value in zip(attributes, values)}
        with open(f'configs/{self.name}.ini', 'w') as file:
            config.write(file)


def get_user_data(name, id32):
    acc = Account(name, id32)
    return acc
