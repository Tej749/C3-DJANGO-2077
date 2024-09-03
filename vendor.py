class Mobile:
    def __init__(self):
        self.model = "sam24"
        self.name = "samsung"

    def showDetails(self):
        print(self.name, self.model)

samMobile = Mobile()
samMobile.showDetails()