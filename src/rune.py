class Rune:
    """Classe définissant une rune caractérisée par : TODO à compléter"""

    def __init__(self, carac, nom, poids):  # Définition du constructeur
        """TODO à compléter aussi"""
        self.carac = carac
        self.nom = nom
        self.poids = poids  # Plus que le poid, retourne en fait le poid de la rune pour 1 point de caractéristique

    def getCarac(self):
        return self.carac

    def getPoids(self):
        return float(self.poids)


def init_rune_tab():
    tableau = [Rune("Initiative", "Ini", "0.1"),
               Rune("Poids portable", "Pod", "0.25"),
               Rune("Vitalité", "Vi", "0.2"),
               Rune("Force", "Fo", "1"),
               Rune("Intelligence", "Ine", "1"),
               Rune("Chance", "Cha", "1"),
               Rune("Agilité", "Age", "1"),
               Rune("Puissance", "Pui", "2"),
               Rune("Puissance (pièges)", "Pi Per", "2"),
               Rune("Résistance fixe neutre", "Ré Neutre", "2"),
               Rune("Résistance fixe terre", "Ré Terre", "2"),
               Rune("Résistance fixe feu", "Ré Feu", "2"),
               Rune("Résistance fixe eau", "Ré Eau", "2"),
               Rune("Résistance fixe air", "Ré Air", "2"),
               Rune("Résistance fixe poussée", "Ré Pou", "2"),
               Rune("Résistance fixe critique", "Ré Cri", "2"),
               Rune("Résistance en % neutre", "Ré Per Neutre", "6"),
               Rune("Résistance en % terre", "Ré Per Terre", "6"),
               Rune("Résistance en % feu", "Ré Per Feu", "6"),
               Rune("Résistance en % eau", "Ré Per Eau", "6"),
               Rune("Résistance en % air", "Ré Per Air", "6"),
               Rune("Sagesse", "Sa", "3"),
               Rune("Prospection", "Prospe", "3"),
               Rune("Tacle", "Tac", "4"),
               Rune("Fuite", "Fui", "4"),
               Rune("Dommages neutre", "Do Neutre", "5"),
               Rune("Dommages terre", "Do Terre", "5"),
               Rune("Dommages feu", "Do Feu", "5"),
               Rune("Dommages eau", "Do Eau", "5"),
               Rune("Dommages air", "Do Air", "5"),
               Rune("Dommages poussée", "Do Pou", "5"),
               Rune("Dommages critiques", "Do Cri", "5"),
               Rune("Dommages pièges", "Pi", "5"),
               Rune("Dommages", "Do", "20"),
               Rune("Retrait PM", "Ret Pme", "7"),
               Rune("Retrait PA", "Ret Pa", "7"),
               Rune("Résistance PM", "Ré Pme", "7"),
               Rune("Résistance PA", "Ré Pa", "7"),
               Rune("Soin", "So", "10"),
               Rune("Coups critiques", "Cri", "10"),
               Rune("Renvoi de dommage", "Do Ren", "10"),
               Rune("Dommage en % arme", "Do Per Ar", "15"),
               Rune("Dommage en % sort", "Do Per So", "15"),
               Rune("Dommage en % distance", "Do Per Di", "15"),
               Rune("Dommage en % mélée", "Do Per Mé", "15"),
               Rune("Résistance en % distance", "Ré Per Di", "15"),
               Rune("Résistance en % mélée", "Ré Per Mé", "15"),
               Rune("Invocation", "Invo", "30"),
               Rune("Portée", "Po", "51"),
               Rune("PM", "Pme", "90"),
               Rune("PA", "Pa", "100"),
               Rune("Arme de chasse", "Rune de chasse", "5")]

    return tableau

"-91 Vitalité, -1 PA, 10 Sagesse, +reliquat = 122.75"
91*1//5+100