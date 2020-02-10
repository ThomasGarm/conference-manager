from .classid import Id

class Conference(Id):
    def __init__(self, data):
        super().__init__(data)
        self.titre = None
        self.resume = None
        self.date = None
        self.hour = None
        self.creation_date = None
        self.speaker_id = None