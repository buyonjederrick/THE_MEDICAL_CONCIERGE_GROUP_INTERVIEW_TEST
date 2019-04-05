class Season:
    def __init__(self, season=0, characters=None):
        if characters is None:
            characters = dict()
        self._season = season
        self._characters = characters

    def season(self):
        return self._season

    def characters(self):
        return self._characters
