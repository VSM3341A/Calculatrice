result_temp1=0
result_temp2=0
result=0




def decoder_chiffre_romain(chiffre):
    if chiffre == 'I':
        return 1
    elif chiffre=='V':
        return 5
    elif chiffre=='X':
        return 10
    elif chiffre=="L":
        return 50
    elif chiffre=='C':
        return 100
    elif chiffre=='D':
        return 500
    elif chiffre=='M':
        return 1000

def decoder_deux_chiffres_romains_identiques(deux_chiffres_identiques):
    i=0
    if deux_chiffres_identiques[i] == 'I':
        return decoder_chiffre_romain(deux_chiffres_identiques[i])*2
    elif deux_chiffres_identiques[i] == 'V':
         return decoder_chiffre_romain(deux_chiffres_identiques[i])*2
    elif deux_chiffres_identiques[i] == 'X':
         return decoder_chiffre_romain(deux_chiffres_identiques[i])*2
    elif deux_chiffres_identiques[i] == "L":
        return decoder_chiffre_romain(deux_chiffres_identiques[i])*2
    elif deux_chiffres_identiques[i] == 'C':
        return decoder_chiffre_romain(deux_chiffres_identiques[i])*2
    elif deux_chiffres_identiques[i] == 'D':
        return decoder_chiffre_romain(deux_chiffres_identiques[i])*2
    elif deux_chiffres_identiques[i] == 'M':
        return decoder_chiffre_romain(deux_chiffres_identiques[i])*2


def decoder_n_chiffres_romains_identiques(n_chiffres_identiques):
    i=0
    longueur_chiffre=len(n_chiffres_identiques)

    if n_chiffres_identiques[i] == 'I':
        return decoder_chiffre_romain(n_chiffres_identiques[i])*longueur_chiffre

    elif n_chiffres_identiques[i] == 'V':
         return decoder_chiffre_romain(n_chiffres_identiques[i])*longueur_chiffre

    elif n_chiffres_identiques[i] == 'X':
         return decoder_chiffre_romain(n_chiffres_identiques[i])*longueur_chiffre

    elif n_chiffres_identiques[i] == "L":
        return decoder_chiffre_romain(n_chiffres_identiques[i])*longueur_chiffre

    elif n_chiffres_identiques[i] == 'C':
        return decoder_chiffre_romain(n_chiffres_identiques[i])*longueur_chiffre

    elif n_chiffres_identiques[i] == 'D':
        return decoder_chiffre_romain(n_chiffres_identiques[i])*longueur_chiffre

    elif n_chiffres_identiques[i] == 'M':
        return decoder_chiffre_romain(n_chiffres_identiques[i])*longueur_chiffre



def conversion_nombre_romain(nombre_romain):
    longueur_nombre=len(nombre_romain)
    result = 0

    for index in range (0, longueur_nombre):
        Chiffre_index=decoder_chiffre_romain(nombre_romain[index])

        if index < longueur_nombre-1:
            Chiffre_index_suivant = decoder_chiffre_romain(nombre_romain[index + 1])

            if Chiffre_index_suivant > Chiffre_index:
                Chiffre_index-= 2 * Chiffre_index

        result = result + Chiffre_index

    return result

def addition_nombres_romains(nombre_romain1, nombre_romain2):
    nombre_entier1 = conversion_nombre_romain(nombre_romain1)
    nombre_entier2 = conversion_nombre_romain(nombre_romain2)

    resultat = nombre_entier1 + nombre_entier2

    return resultat



def soustraction_nombres_romains(nombre_romain1, nombre_romain2):
    nombre_entier1 = conversion_nombre_romain(nombre_romain1)
    nombre_entier2 = conversion_nombre_romain(nombre_romain2)

    resultat = nombre_entier1 - nombre_entier2

    return resultat


def multiplication_nombres_romains(nombre_romain1, nombre_romain2):
    nombre_entier1 = conversion_nombre_romain(nombre_romain1)
    nombre_entier2 = conversion_nombre_romain(nombre_romain2)

    resultat = nombre_entier1 * nombre_entier2

    return resultat


def division_nombres_romains(nombre_romain1, nombre_romain2):
    nombre_entier1 = conversion_nombre_romain(nombre_romain1)
    nombre_entier2 = conversion_nombre_romain(nombre_romain2)

    resultat = nombre_entier1 // nombre_entier2

    return resultat


def calculatrice_nombres_romains(operateur, nombre_romain1, nombre_romain2):
    if operateur == '+':
        return addition_nombres_romains(nombre_romain1, nombre_romain2)
    elif operateur == '-':
        return soustraction_nombres_romains(nombre_romain1, nombre_romain2)
    elif operateur == '*':
        return multiplication_nombres_romains(nombre_romain1, nombre_romain2)
    elif operateur == '/':
        return division_nombres_romains(nombre_romain1, nombre_romain2)





##############################################################################################




def decoder_chiffre_en_romain(chiffre):
    if chiffre == 1:
        return 'I'
    elif chiffre == 2:
        return 'II'
    elif chiffre == 3:
        return 'III'
    elif chiffre == 4:
        return 'IV'
    elif chiffre == 5:
        return 'V'
    elif chiffre == 6:
        return 'VI'
    elif chiffre == 7:
        return 'VII'
    elif chiffre == 8:
        return 'VIII'
    elif chiffre == 9:
        return 'IX'
    elif chiffre == 10:
        return 'X'
    elif chiffre == 50:
        return 'L'
    elif chiffre == 100:
        return 'C'
    elif chiffre == 500:
        return 'D'
    elif chiffre == 1000:
        return 'M'













