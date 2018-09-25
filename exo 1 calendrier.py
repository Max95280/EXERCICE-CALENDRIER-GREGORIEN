# Fonction pour étape 1, 2 et 3
def Caculexo(Value1, Value2, ):
    result = int(Value1 / 4)
    Fresult = Value1 + result
    Fresult = Value2 + Fresult
    return Fresult

# Fonction pour étape 4
def addmois(Value3):
    Fresult = 0
    if Value3 == 1:
        Fresult = Fresult + 0
    elif Value3 == 2:
        Fresult = Fresult + 3
    elif Value3 == 3:
        Fresult = Fresult + 3
    elif Value3 == 4:
        Fresult = Fresult + 6
    elif Value3 == 5:
        Fresult = Fresult + 1
    elif Value3 == 6:
        Fresult = Fresult + 4
    elif Value3 == 7:
        Fresult = Fresult + 6
    elif Value3 == 8:
        Fresult = Fresult + 2
    elif Value3 == 9:
        Fresult = Fresult + 5
    elif Value3 == 10:
        Fresult = Fresult + 0
    elif Value3 == 11:
        Fresult = Fresult + 3
    elif Value3 == 12:
        Fresult = Fresult + 5
    return Fresult

# Fonction pour étape 5
def bissextile(Value4, Value5):
    bissextile = False
    if Value4 % 400 == 0:  # Si l'année est divisible par 400
        bissextile = True
    elif Value4 % 100 == 0:  # Si l'année est divisible par 100
        bissextile = False
    elif Value4 % 4 == 0:  # Si l'années est divisible par 4
        bissextile = True
    if bissextile == True:
        if Value5 == 1 or Value5 == 2:
            return -1
        else:
            return 0
    else:
        return 0

# Fonction pour étape 6
def siecle(Value6):
    if Value6 == 16:
        return 6
    elif Value6 == 15:
        return 0
    elif Value6 == 17:
        return 4
    elif Value6 == 18:
        return 2
    elif Value6 == 19:
        return 0
    elif Value6 == 20:
        return 6
    elif Value6 == 21:
        return 4

# Fonction pour étape 7 et 8
def reste(Value7):
    result = Value7 % 7
    if result == 0:
        return "Dimanche"
    elif result == 1:
        return "Lundi"
    elif result == 2:
        return "Mardi"
    elif result == 3:
        return "Mercredi"
    elif result == 4:
        return "Jeudi"
    elif result == 5:
        return "Vendredi"
    elif result == 6:
        return "Samedi"


# Explication du programme
print("###########################################################")
print("#   Ce programme permet de savoir le jour de la semaine   #\n#   pour une date donnée dans le calendrier grégorien     #\n#   à partir du 1er novembre 1582                         #")
print("###########################################################\n")

# Saisie de la date
DATE = input("jj/MM/AAAA : ")

# Construction des variables pour effectuées les calcules

Yearint = int(DATE[6:10])  # donnée pour etape 5
pJour = int(DATE[0:2])  # donnée pour etape 3
pMois = int(DATE[3:5])  # donnée pour etape 4
psiecle = int(DATE[6:8])  # donnée pour etape 6
pAnnée = int(DATE[8:10])  # donnée pour etape 2

# Filtre pour avoir un date correct
while Yearint < 1582 or Yearint > 2199:
    print("Votre Année est INCORRECT recomencer")
    DATE = input("jj/MM/AAAA : ")
    Yearint = int(DATE[6:10])
    pJour = int(DATE[0:2])
    pMois = int(DATE[3:5])
    psiecle = int(DATE[6:8])
    pAnnée = int(DATE[8:10])
while pMois < 1 or pMois > 12:
    print("Votre Mois est INCORRECT")
    DATE = input("jj/MM/AAAA : ")
    Yearint = int(DATE[6:10])
    pJour = int(DATE[0:2])
    pMois = int(DATE[3:5])
    psiecle = int(DATE[6:8])
    pAnnée = int(DATE[8:10])
while pJour < 1 or pJour > 31:
    print("Votre Jours est INCORECT ")
    DATE = input("jj/MM/AAAA : ")
    Yearint = int(DATE[6:10])
    pJour = int(DATE[0:2])
    pMois = int(DATE[3:5])
    psiecle = int(DATE[6:8])
    pAnnée = int(DATE[8:10])
while Yearint == 1582 and pMois < 11:
    print("DATE INCORRECTE")
    DATE = input("jj/MM/AAAA : ")
    Yearint = int(DATE[6:10])
    pJour = int(DATE[0:2])
    pMois = int(DATE[3:5])
    psiecle = int(DATE[6:8])
    pAnnée = int(DATE[8:10])

# Calcule via foction
Finalresult = Caculexo(pAnnée, pJour)
Finalresult = Finalresult + (addmois(pMois))
Finalresult = Finalresult + (bissextile(Yearint, pMois))
Finalresult = Finalresult + (siecle(psiecle))
Finalresult = reste(Finalresult)

# Résultat
print("\n################################")
print("#   votre jour est un",Finalresult,"  #")
print("################################")
