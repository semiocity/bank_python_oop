from banque import *

# class Personne:
#     def __init__(self, nom, prenom):
#         self.nom = nom
#         self.prenom = prenom

# class CompteSimple:
#     _dernier_numero = 10000

#     def __init__(self, titulaire, depot):
#         self.titulaire = titulaire
#         self.__solde = depot
#         self.__numero = CompteSimple._dernier_numero + 1
#         CompteSimple._dernier_numero += 1

#     @property # accès en lecture au solde:
#     def solde (self):
#         return self.__solde

#     @property # accès en lecture au numero de compte:
#     def numero (self):
#         return self.__numero


#     def crediter (self, somme):
#         self.__solde += somme

#     def debiter (self, somme):
#         self.__solde -= somme

#     def editer_releve(self):
#         print (self.solde)


# class CompteCourant(CompteSimple):

#     def __init__(self, titulaire, depot):
#         super().__init__(titulaire, depot)
#         self.historique = []

#     def crediter (self, somme):
#         super().crediter (somme)
#         self.historique.append ("Crédit: {}".format(somme)) 

#     def debiter (self, somme):
#         super().debiter (somme)
#         self.historique.append ("Débit: {}".format(somme))

#     def editer_releve(self):
#         for operation in self.historique:
#             print (operation)
#         super().editer_releve()



# class Banque:
#     def __init__ (self, comptes):
#         self.comptes = []

#     def ouvrir_compte_client (self, client, depot):
#         compte = CompteSimple(client, depot)
#         self.comptes.append(compte)

#     def ouvrir_compte_courant (self, client, depot):
#         compte_courant = CompteCourant(client, depot)
#         self.comptes.append(compte_courant)
    
#     def somme_avoirs (self):
#         _somme = 0
#         for compte in self.comptes:
#             _somme += compte.solde
#         return _somme

#     def prelever_frais (self, prelevement):
#         _prelevements = 0
#         for compte in self.comptes:
#             _prelevements += prelevement
#             compte.debiter (prelevement)
            



import pytest

@pytest.fixture
def personne():
    return Personne ("Dziedzic", "Grégory")

@pytest.fixture
def personne2():
    return Personne ("Smith", "John")

@pytest.fixture
def personne3():
    return Personne ("Rodriguez", "Eleonora")

@pytest.fixture
def personne4():
    return Personne ("Bob", "Léponj")

@pytest.fixture
def personne5():
    return Personne ("Angela", "Lala")



@pytest.fixture
def compte1():
    return CompteSimple(personne4, 0)

@pytest.fixture
def compte2():
    return CompteCourant(personne5, 0)

@pytest.fixture
def banque():
    return Banque()

@pytest.fixture
def banque2():
    return Banque()

@pytest.fixture
def compte_courant():
    return CompteCourant(personne, 0)



def test_numero_de_compte (compte1):
    assert compte1.numero == 10001

def test_numero_de_compte2 (compte2):
    assert compte2.numero == 10002


def test_crediter(compte1):
    compte1.crediter(9000)
    assert compte1.solde == 9000

def test_debiter(compte1):
    compte1.debiter(9000)
    assert compte1.solde == -9000

def test_ouverture_compte (banque, personne):
    banque.ouvrir_compte_client(personne, 1000)
    assert banque.comptes[0].solde == 1000

def test_somme_avoirs (banque):
    banque.ouvrir_compte_client(personne, 1000)
    banque.ouvrir_compte_client(personne2, 8000)
    banque.ouvrir_compte_client(personne3, 2000)
    assert banque.somme_avoirs() ==  11000

def test_prelevements (banque):
    banque.ouvrir_compte_client(personne, 1000)
    banque.ouvrir_compte_client(personne2, 8000)
    banque.ouvrir_compte_client(personne3, 2000)
    banque.prelever_frais(1000)
    assert banque.somme_avoirs() ==  8000

def test_compte_courant (compte_courant):
    compte_courant.crediter(5000)
    compte_courant.debiter(3000)
    assert compte_courant.solde == 2000

def test_somme_avoirs_compte_courant (banque2):
    banque2.ouvrir_compte_client(personne, 1000)
    banque2.ouvrir_compte_client(personne2, 8000)
    banque2.ouvrir_compte_client(personne3, 2000)
    assert banque2.somme_avoirs() ==  11000

def test_prelevements_compte_courants (banque2):
    banque2.ouvrir_compte_client(personne, 1000)
    banque2.ouvrir_compte_client(personne2, 8000)
    banque2.ouvrir_compte_client(personne3, 2000)
    banque2.prelever_frais(1000)
    assert banque2.somme_avoirs() ==  8000


if __name__=="__main__":
    test_main()
