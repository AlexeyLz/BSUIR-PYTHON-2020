
class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


first_singleton = Singleton()
print("Object created", first_singleton)
second_singleton = Singleton()
print("Object created", second_singleton)