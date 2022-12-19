class Name:

    @classmethod
    def name_check(cls, name):
        if type(name) == str and len(name) <= 32:
            return name
        else:
            raise ValueError("Account name must be string and no longer than 32 characters.")

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if self.name_check(value):
            instance.__dict__[self.name] = value
