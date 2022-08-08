import accinfo


def init(): # getting user info
    user = accinfo.get_user_data('Sergey', '000000000')
    print(user.name, user.account_id)


if __name__ == '__main__':
    init()
