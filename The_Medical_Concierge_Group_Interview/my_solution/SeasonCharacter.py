class SeasonCharacter:
    def __init__(self, character='', episodes=0, died=0):
        self._character = character
        self._episodes = episodes
        self._died = died

    def character(self):
        return self._character

    def episodes(self):
        return self._episodes

    def died(self):
        return self._died
