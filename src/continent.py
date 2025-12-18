class Continent:
    _instance = None 

    def __new__(cls, nom="Zootopia"):
        if cls._instance is None:
            cls._instance = super(Continent, cls).__new__(cls)
            cls._instance._nom = nom
            cls._instance._pays = []
        return cls._instance

    def __init__(self, nom="Zootopia"):
        # L'initialisation est gérée par __new__ pour le Singleton
        pass

    def get_nom(self):
        return self._nom

    def add_country(self, pays):
        if pays not in self._pays:
            self._pays.append(pays)