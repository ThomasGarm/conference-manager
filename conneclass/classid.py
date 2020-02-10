#mother class with hydratation method

class Id():
    def __init__(self, data=False):
        self.id = None

        if data:
            self.hydratation(data)


    def hydratation(self,data):
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)

    