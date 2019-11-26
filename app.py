result_temp1=0
result_temp2=0
result_temp3=0
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
    Chiffre_index = 0
    Chiffre_index_suivant = 0
    result = 0

    for i in range (0, longueur_nombre):
        Chiffre_index=decoder_chiffre_romain(nombre_romain[i])

        if i < longueur_nombre-1:
            Chiffre_index_suivant = decoder_chiffre_romain(nombre_romain[i + 1])

            if Chiffre_index_suivant > Chiffre_index:
                Chiffre_index-= 2 * Chiffre_index

        result = result + Chiffre_index

    return result















