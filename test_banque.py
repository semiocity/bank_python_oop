from banque import *
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
