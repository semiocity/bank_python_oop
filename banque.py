from random import randint

class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
    def __str__(self):
        return "{} {}".format(self.nom, self.prenom)

class CompteSimple:
    _dernier_numero = 10000

    def __init__(self, titulaire, depot):
        self.titulaire = titulaire
        self.__solde = depot
        self.__numero = CompteSimple._dernier_numero + 1
        CompteSimple._dernier_numero += 1

    @property # accès en lecture au solde:
    def solde (self):
        return self.__solde

    @property # accès en lecture au numero de compte:
    def numero (self):
        return self.__numero


    def crediter (self, somme):
        self.__solde += somme

    def debiter (self, somme):
        self.__solde -= somme

    def editer_releve(self):
        print ("Relevé du compte simple numéro {} de {}".format (self.numero, self.titulaire))
        print ("Solde : ",self.solde, "\n")


class CompteCourant(CompteSimple):

    def __init__(self, titulaire, depot):
        super().__init__(titulaire, depot)
        self.historique = []

    def crediter (self, somme):
        super().crediter (somme)
        self.historique.append ("Crédit: {}".format(somme)) 

    def debiter (self, somme):
        super().debiter (somme)
        self.historique.append ("Débit: {}".format(somme))

    def editer_releve(self):
        print ("Relevé du compte courant numéro {} de {}".format (self.numero, self.titulaire))
        for operation in self.historique:
            print (operation)
        print ("Solde : ",self.solde, "\n")



class Banque:
    def __init__ (self):
        self.comptes = []

    def ouvrir_compte_client (self, client, depot):
        compte = CompteSimple(client, depot)
        self.comptes.append(compte)

    def ouvrir_compte_courant (self, client, depot):
        compte_courant = CompteCourant(client, depot)
        self.comptes.append(compte_courant)
    
    def somme_avoirs (self):
        _somme = 0
        for compte in self.comptes:
            _somme += compte.solde
        return _somme

    def prelever_frais (self, prelevement):
        _prelevements = 0
        for compte in self.comptes:
            _prelevements += prelevement
            compte.debiter (prelevement)


# Comme je ne sais pas tester un affichage avec pytest,
# je crée un jeu de valeurs dans le main afin de tester les fonctions correspondant
def main():
    banque = Banque()

    #creation à la main d'une base client
    base_clients = []
    base_clients.append(Personne ("Dziedzic", "Grégory"))
    base_clients.append(Personne ("Smith", "John"))
    base_clients.append(Personne ("Rodriguez", "Eleonora"))
    base_clients.append(Personne ("Léponj", "Bob"))
    base_clients.append(Personne ("Lala", "Angela"))
    base_clients.append(Personne ("Zultron", "Matador"))

    # ouverture de comptes simples ou comptes courants (1 sur 2)
    for i, nouveau_client in enumerate(base_clients):
        if i%2 == 0:
            banque.ouvrir_compte_client(nouveau_client, 1000)
        else:
            banque.ouvrir_compte_courant(nouveau_client, 1000)


    # operations aléatoires sur les comptes
    for i, _ in enumerate(banque.comptes):
        for operation in range (randint(3,8)):
            if operation %2 == 0:
                banque.comptes[i].debiter(randint(1,1000))
            else:
                banque.comptes[i].crediter(randint(1,1000))

    # affichage des relevés
    for compte in banque.comptes:
        compte.editer_releve()

if __name__=="__main__":
    main()
