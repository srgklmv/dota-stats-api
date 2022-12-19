class Name:

    @classmethod
    def name_check(cls, name):
        if type(name) == str and len(name) <= 32:
            return True
        elif name is None:
            print("Don't forget to add a name to account instance.")
            return True
        else:
            raise ValueError("Account name must be string and no longer than 32 characters.")

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if self.name_check(value):
            instance.__dict__[self.name] = value


class ID:

    @classmethod
    def id_check(cls, id_):
        if type(id_) in (int, str) and len(str(id_)) <= 17 and str(id_).isdigit():
            return True
        elif id_ is None:
            print("Don't forget to add an IDs to account instance.")
            return True
        else:
            raise ValueError("Account IDs must be integer or string and less or equal to 17 digits.")

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if self.id_check(value):
            instance.__dict__[self.name] = value
