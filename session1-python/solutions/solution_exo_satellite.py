class Satellite:
    def __init__(self, nom, masse=100, vitesse=0):
        self.nom, self.masse, self.vitesse = nom, masse, vitesse

    def impulsion(self, force, duree):
        self.vitesse = self.vitesse + force * duree / self.masse

    def energie(self):
        return self.masse * self.vitesse ** 2 / 2

    def affiche_vitesse(self):
        print(
            f"Vitesse du satellite {self.nom} = {self.vitesse} m/s"
        )
