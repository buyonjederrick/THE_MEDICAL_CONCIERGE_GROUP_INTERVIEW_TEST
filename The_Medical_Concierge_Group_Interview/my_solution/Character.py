class Character:
    def __init__(self, name='', mother='Unidentified', father='Unidentified', district='', registrationDate=0):
        self._name = name
        self._mother = mother
        self._father = father
        self._district = district
        self._registrationDate = registrationDate

    def name(self):
        return self._name

    def mother(self):
        if self._mother == '':
            return 'Unidentified'
        return self._mother

    def father(self):
        if self._father == '':
            return 'Unidentified'
        return self._father

    def district(self):
        return self._district

    def registrationDate(self):
        return self._registrationDate
