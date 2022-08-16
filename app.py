import configparser
import accinfo


def check_api():
    try:
        config = configparser.ConfigParser()
        config.read()
    except:
        pass
    else:
        pass
    finally:
        pass


def create_account():
    name = input('Enter account name (used just for identify in program): ')
    id32 = input('Enter account id in 32-bit format: ')
    account = accinfo.Account(name, id32)
    account.create_config_file()


def use_existing_acc():
    pass
