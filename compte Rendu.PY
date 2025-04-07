    #### TD/TP 1: Introduction à la programmation en Python :Variables, Calculs et Manipulation de Données

### Exercice 1:
##Déclaration des variables
str1="bonjour"
int1= 12
dec1=13.5
# Affichage des types des variables
print(str1, "est de type", type(str1))
print(int1, "est de type", type(int1))
print(dec1, "est de type", type(dec1))


nom,prenom,age=("ali", "adam", 23)
print("le nom est", nom)
print("le prenom est", prenom)
print("l'age est", age)


### Exercice 2:
## Saisie des notes
math= float(input("entrer votre note du math"))
physique=float(input("entrer votre note du physique"))
svt=float(input("entrer votre note du svt"))
anglais=float(input("entrer votre note d'anglais"))
## Saisie des coefficients
coe_math=int(input("entrer le coefficient du matth"))
coe_physique=int(input("entrer le coefficient du physique"))
coe_svt=int(input("entrer le coefficient du svt"))
coe_anglais=int(input("entrer le coefficient d'anglais"))
## Calcul de la moyenne 
somme_notes=math*coe_math+physique*coe_physique+svt*coe_svt+anglais*coe_anglais
somme_coe=coe_math+coe_physique+coe_svt+coe_anglais
moyenne=somme_notes/somme_coe
print( moyenne)


## Saisie votre budget et les achats
budget= float(input("saisie le budget"))
achats=float(input("saisie le montatnt des achats"))
if budget>= achats:
    print("vous avez acheter")
else:
    print("vous ne pouvez pas acheter")


### Exercice 3:
## Demander à l'utilisateur de saisir le rayon et la hauteur
rayon=float(input("entrer le rayon"))
hauteur=float(input("entrer la hauteur"))
## Calcul de volume 
volume=(1/3)*3.14*rayon**2*hauteur
## Afficher le resultat
print("volume", volume)


### Exercice 4:
rg=float(input("entrer le rayon du disque"))
rp=float(input("entrer le rayon du trou"))
if rg>rp:
    s=3.14*rg**2-3.14*rp**2
    print("la surface du disque de coupee est", s)
else:
    print("vous ne pouvez pas de couper le disque")


### Exercice 5:
phrase=input("veuillez saiser la phrase")
longueur=len(phrase)
if longueur%2==0:
    print("le longueur de la phrase est paire")
else:
    print("le longueur de la phrase est impaire")




                      ###   TD/TP2 – Introduction aux structures de données : les listes


#Exercice 1:
Semaine = ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi', 'dimanche']
print(Semaine)
Couleurs = ['rouge', 'bleu', 'vert', 'jaune', 'noir']
print(Couleurs)
valeurs = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7]
print(valeurs[1], valeurs[3], valeurs[5])




#Exrcice 2:
mylist = ['apple', 'banana', 'cherry']
print(mylist[1])  # Résultat : banana
mylist = ['apple', 'banana', 'banana', 'cherry']
print(mylist[2])  # Résultat : banana
thislist = ['apple', 'banana', 'cherry']
print(len(thislist))  # Résultat : 3
mylist = ['apple', 'banana', 'cherry']
print(mylist[-1])  # Résultat : cherry
fruits = ["apple", "banana", "cherry"]
print(fruits[1])  # Résultat : banana
mylist = ['apple', 'banana', 'cherry', 'orange', 'kiwi']
print(mylist[1:4])  # Résultat : ['banana', 'cherry', 'orange']
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])  # Résultat : ['cherry', 'orange', 'kiwi']


#Exrcice 3:
matieres = ['Anglais', 'Physique', 'Maths', 'Svt']
print(matieres)
#Ajouter deux nouvelles matières :
matieres.append('Histoire')
matieres.append('Geographie')
print(matieres)
#Afficher certaines parties de la liste :
#Les 4 premiers :
print(matieres[:4])
#Les 3 derniers :
print(matieres[-3:])
#3éléments depuis l’indice 2 :
print(matieres[2:5])


#Exrcice 4:
mylist = ['apple', 'banana', 'cherry']
mylist[0] = 'kiwi'
print(mylist[1])  # Résultat : banana
#Changer ‘apple’ par ‘kiwi’ :
fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"
#Remplacer un élément via slicing :
mylist = ['apple', 'banana', 'cherry']
mylist[1:2] = ['kiwi', 'mango']
print(mylist[2])  # Résultat : mango
#Insertion au début :
mylist = ['apple', 'banana', 'cherry']
mylist.insert(0, 'orange')
print(mylist[1])  # Résultat : apple
#Ajout avec append :
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
#Ajout à la 2e position :
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")



#Exrcice 5:
Semaine = ['lun', 'mar', 'mer', 'jeu', 'ven', 'sam', 'dim']
Semaine.remove('mer')
#Supprimer avec pop() :
mylist = ['apple', 'banana', 'cherry']
mylist.pop(1)
print(mylist)  # Résultat : ['apple', 'cherry']
#Vider une liste avec clear() :
fruits = ['apple', 'banana', 'cherry']
fruits.clear()


                       ###   TP3 : Manipulation avancée des listes en Python

# Exercice 1:
nombres = [4, 8, 15, 16, 23, 42]

def affListe(liste):
    for element in liste:
        print(element)

affListe(nombres)


# Exercice 2:
def somme_liste(liste):
    return sum(liste)

def moyenne_liste(liste):
    if len(liste) == 0:
        return 0
    return sum(liste) / len(liste)

print("Somme :", somme_liste(nombres))
print("Moyenne :", moyenne_liste(nombres))


# Exercice 3:
def extraire_pairs(liste):
    return [x for x in liste if x % 2 == 0]

print("Nombres pairs :", extraire_pairs(nombres))



# Exercice 4:
def element_existe(liste, element):
    return element in liste

print("15 est dans la liste :", element_existe(nombres, 15))
print("50 est dans la liste :", element_existe(nombres, 50))


# Exercice 5:
def liste_carres(liste):
    return [x**2 for x in liste]

print("Carrés :", liste_carres(nombres))


# Exercice 6:
def trouver_min_max(liste):
    if not liste:
        return None, None
    return min(liste), max(liste)

mini, maxi = trouver_min_max(nombres)
print("Minimum :", mini)
print("Maximum :", maxi)



# Exercice 7:
autres_nombres = [3, 5, 7, 9, 10]

def fusionner_et_trier(liste1, liste2):
    return sorted(liste1 + liste2)

fusion_result = fusionner_et_trier(nombres, autres_nombres)
print("Liste fusionnée et triée :", fusion_result)




# Exercice 8:
def est_palindrome(mot):
    return mot == mot[::-1]

print("radar est un palindrome :", est_palindrome("radar"))
print("python est un palindrome :", est_palindrome("python"))
print("level est un palindrome :", est_palindrome("level"))




                   ###   TP4: Programmation Python — Manipulation de données et introduction à la POO


#Exercice 1:
personnes = {}

while True:
    print("\n1. Ajouter une personne")
    print("2. Afficher l'âge d'une personne")
    print("3. Supprimer une personne")
    print("4. Quitter")

    choix = input("Votre choix : ")

    if choix == "1":
        nom = input("Nom : ")
        age = input("Âge : ")
        personnes[nom] = age
    elif choix == "2":
        nom = input("Nom à rechercher : ")
        if nom in personnes:
            print(f"{nom} a {personnes[nom]} ans.")
        else:
            print("Personne non trouvée.")
    elif choix == "3":
        nom = input("Nom à supprimer : ")
        if nom in personnes:
            del personnes[nom]
            print("Supprimé.")
        else:
            print("Personne non trouvée.")
    elif choix == "4":
        break
    else:
        print("Choix invalide.")




#Exrcice 2:
def fusionner_dicts(d1, d2):
    fusion = d1.copy()
    for k, v in d2.items():
        if k in fusion:
            if isinstance(v, str) and isinstance(fusion[k], str):
                fusion[k] += v
            elif isinstance(v, (int, float)) and isinstance(fusion[k], (int, float)):
                fusion[k] += v
        else:
            fusion[k] = v
    return dict(sorted(fusion.items()))

dict1 = {"a": 5, "b": "Hello", "c": 3}
dict2 = {"a": 7, "b": " World", "d": 10}

resultat = fusionner_dicts(dict1, dict2)
print(resultat)


#Exrcice 3:
# Écriture initiale dans le fichier
with open("personnes.txt", "w") as f:
    f.write("Alice,25\nBob,30\n")

# Lecture et stockage dans un dictionnaire
personnes = {}
with open("personnes.txt", "r") as f:
    for ligne in f:
        nom, age = ligne.strip().split(",")
        personnes[nom] = int(age)

print("Contenu du fichier :", personnes)

# Ajout ou modification
nom = input("Nom : ")
age = input("Âge : ")
personnes[nom] = age

# Réécriture du fichier
with open("personnes.txt", "w") as f:
    for nom, age in personnes.items():
        f.write(f"{nom},{age}\n")


#Exrcice 4:
notes = {}

with open("notes.txt", "r") as f:
    for ligne in f:
        nom, note = ligne.strip().split(",")
        notes[nom] = float(note)

moyenne = sum(notes.values()) / len(notes)
print(f"Moyenne générale : {moyenne:.2f}")

print("Étudiants au-dessus de la moyenne :")
for nom, note in notes.items():
    if note > moyenne:
        print(f"{nom} : {note}")

#Exrcice 5:
class Etudiant:
    def __init__(self, nom, age, note):
        self.nom = nom
        self.age = age
        self.note = note

    def afficher_info(self):
        print(f"Nom : {self.nom}, Âge : {self.age}, Note : {self.note}")

    @staticmethod
    def moyenne_etudiants(etudiants):
        total = sum(e.note for e in etudiants)
        return total / len(etudiants)

# Exemple d'utilisation
etudiants = [
    Etudiant("Alice", 20, 15),
    Etudiant("Bob", 22, 18),
    Etudiant("Charlie", 21, 12)
]

for e in etudiants:
    e.afficher_info()

print("Moyenne : ", Etudiant.moyenne_etudiants(etudiants))


#Exrcice 6:
import json

class CarnetAdresses:
    def __init__(self):
        self.contacts = {}

    def ajouter_contact(self, nom, numero):
        self.contacts[nom] = numero

    def supprimer_contact(self, nom):
        if nom in self.contacts:
            del self.contacts[nom]

    def rechercher_contact(self, nom):
        return self.contacts.get(nom, "Inconnu")

    def sauvegarder(self, fichier):
        with open(fichier, "w") as f:
            json.dump(self.contacts, f)

    def charger(self, fichier):
        try:
            with open(fichier, "r") as f:
                self.contacts = json.load(f)
        except FileNotFoundError:
            self.contacts = {}




#Exrcice 7:
class Livre:
    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur
        self.disponible = True

    def __str__(self):
        statut = "Disponible" if self.disponible else "Emprunté"
        return f"{self.titre} par {self.auteur} - {statut}"

class Bibliotheque:
    def __init__(self):
        self.livres = []

    def ajouter_livre(self, livre):
        self.livres.append(livre)

    def emprunter_livre(self, titre):
        for livre in self.livres:
            if livre.titre == titre and livre.disponible:
                livre.disponible = False
                return True
        return False

    def rendre_livre(self, titre):
        for livre in self.livres:
            if livre.titre == titre and not livre.disponible:
                livre.disponible = True
                return True
        return False

    def afficher_disponibles(self):
        for livre in self.livres:
            if livre.disponible:
                print(livre)





                              ###  TP5 : Manipulation et Calculs avec les Tableaux NumPy
## Exercice 1:
import numpy as np

# Création de tableaux
a = np.array([1, 2, 3])
b = np.array([[1, 2], [3, 4]])
c = np.arange(27).reshape(3, 3, 3)

# Accès et modification
a[0] = 10
b[1, 1] = 9

# Slicing
sous_tableau = c[1, :, :]


## Exercice 2:
# Tableaux de base
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Opérations mathématiques
somme = a + b
produit = a * b
division = b / a

# Fonctions math
angles = np.linspace(0, np.pi, 5)
sinus = np.sin(angles)
exponentielle = np.exp(a)

# Opérations logiques
masque = (a % 2 == 0)
a[masque] = -1



### Exercice 3:
a = np.arange(12)

# Reshape
a2 = a.reshape(3, 4)
a3 = a.reshape(2, 2, 3)

# Transposition
a2_transpose = a2.T

# Swap axes
a_swapped = np.swapaxes(a3, 0, 2)

# Concaténation
b = np.arange(12, 24).reshape(3, 4)
concat_h = np.hstack((a2, b))
concat_v = np.vstack((a2, b))

# Découpage
split = np.hsplit(concat_h, 2)



## Exrecice 4:
np.random.seed(0)
mat = np.random.randint(0, 10, (4, 5))

# Statistiques
moyenne_lignes = np.mean(mat, axis=1)
ecart_type_colonnes = np.std(mat, axis=0)

# Tri
mat_tri = np.sort(mat, axis=1)
indice_max = np.argmax(mat)

# Broadcasting
a = np.array([1, 2, 3])
b = np.array([[10], [20], [30]])
result = a * b



## Exrecice 5:
# Covariance
x = np.random.rand(1000)
y = 2 * x + np.random.rand(1000)
z = np.random.rand(1000)
donnees = np.vstack((x, y, z))
covariance = np.cov(donnees)

# Signal sinusoïdal et FFT
import matplotlib.pyplot as plt
t = np.linspace(0, 1, 500)
signal = np.sin(2 * np.pi * 5 * t)
fft_signal = np.fft.fft(signal)
frequencies = np.fft.fftfreq(len(t), d=(t[1]-t[0]))

# Affichage du spectre
plt.plot(frequencies[:250], np.abs(fft_signal)[:250])
plt.title("Spectre du signal")
plt.xlabel("Fréquence (Hz)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()

# Simulation de lancers de dés
des1 = np.random.randint(1, 7, 1000)
des2 = np.random.randint(1, 7, 1000)
somme = des1 + des2

plt.hist(somme, bins=11, edgecolor='black', align='left')
plt.title("Histogramme des sommes de 2 dés lancés 1000 fois")
plt.xlabel("Somme")
plt.ylabel("Fréquence")
plt.grid(True)
plt.show()



## Exercice 6:
import numpy as np

# 1. Création du tableau de ventes aléatoires
np.random.seed(42)  # pour la reproductibilité
ventes = np.random.randint(100, 1001, size=(12, 3))

# 2. Total annuel des ventes par produit
total_annuel = np.sum(ventes, axis=0)

# 3. Moyenne mensuelle des ventes par produit
moyenne_mensuelle = np.mean(ventes, axis=0)

# 4. Mois avec ventes maximales par produit
mois_max = np.argmax(ventes, axis=0)

# 5. Croissance mensuelle en pourcentage
croissance = np.diff(ventes, axis=0) / ventes[:-1] * 100

# 6. Mois avec la plus forte croissance pour chaque produit
mois_max_croissance = np.argmax(croissance, axis=0) + 1  # +1 pour corriger l'index après diff

# 7. Somme des ventes par mois (tous produits confondus)
somme_mensuelle = np.sum(ventes, axis=1)