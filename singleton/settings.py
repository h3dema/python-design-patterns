import uuid


class GlobalSettings(object):
    """
        Singleton cria uma instância apenas se não houver nenhuma instância criada
        até o momento; caso contrário, retorna a instância já criada.
    """
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(GlobalSettings, cls).__new__(cls)
            cls._id = uuid.uuid4()
        return cls.instance

    @property
    def id(self):
        return self._id

    def set(self, **kwargs):
        for k, v in kwargs.items():
            self.__dict__[k] = v


singleton = GlobalSettings()
new_singleton = GlobalSettings()

singleton.set(name="H3dema")
singleton.set(url="http://github.com/h3dema")

print("Equal?", singleton is new_singleton)
print("singleton    :", singleton.id)
print("new_singleton:", new_singleton.id)

print("name:", new_singleton.name)
print("url:", new_singleton.url)
