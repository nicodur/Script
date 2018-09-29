# Code écrit par Nicolas Durand

def calculmois(moi):
    var1 = ['0', '3', '3', '6', '1', '4', '6', '2', '5', '0', '3', '5'] #retourne une valeur selon le mois en cour
    return var1[moi-1] # -1 car var1 commence a 1

def bissext(annee,moi):
    moi = int(moi)
    annee = int(annee)
    bissextile = False
    if annee % 400 == 0: # Si l'année est divisible par 400
        bissextile = True
    elif annee % 100 == 0: # Si l'année est divisible par 100
        bissextile = False
    elif annee % 4 == 0: # Si l'années est divisible par 4
        bissextile = True
    if bissextile and (moi == '01' or moi == '02'): # Si l'année est bissextile et que le mois est janvier ou fevrier cela retourne 1
        return 1
    else:
        return 0

def siecle(var):
    var = int(var/100)
    var = var *100
    if var == 1600:
        return 6
    elif var == 1700:
        return 4
    elif var == 1800:
        return 2
    elif var == 1900:
        return 0
    elif var == 2000:
        return 6
    elif var == 1100:
        return 4

def day(var):
    var= var%7
    tab_jour=["Dimanche","Lundi","Mardi","Mercredi","Jeudi","Vendredi","Samedi"]
    return tab_jour[var]


somme=0
while True:
    anne = input("Entrez la date comprise au plus tot le 1er novembre 1582 sous la forme DD/MM/YYYY: ")
    if (int(anne[6:10]) <1582 ):
        print ("date incorrect")
    elif (len(anne) >10 ):
        print("date incorrect")
    elif (len(anne) < 10): # on test diffente erreurs possible pour pas que l'utilisateur entre une date incorrect
        print("date incorrect")
    else:
        break
annee = int(anne[6:10])
mois = int(anne[3:5])
jour = int(anne[0:2])


deux_annee= annee%100 # On garde seulement les deux derniers chiffres
div = int(deux_annee /4) # on garde que la partie entiere de div
somme= deux_annee + div + jour + int(calculmois(mois)) - int(bissext(annee,mois)) + int (siecle(annee))

jour = day(somme) # On récupère le jour dans la fonction day

print("""Ce jour la, je m'en souviens c'était un""",jour)








