# user class and following methods to create and store user data such as acc id, api key, etc.
class Account:

    def __init__(self, name, id32):
        self.name = name
        self.account_id = id32


def get_user_data(name, id32):
    acc = Account(name, id32)
    return acc
