from .classid import Id

class Speaker(Id):
    def __init__(self, data):
        super().__init__(data)
        self.firstname = None
        self.lastname = None
        self.description = None
        self.profession = None
        self.statut = None

    def __str__(self):
       return """======================={}  {}: {}
       {}\n{} =================""".format(self.firstname, self.lastname, self.profession, self.description, self.statut)