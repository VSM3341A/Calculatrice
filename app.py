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
    if deux_chiffres_identiques == 'II':
        return 2
    elif deux_chiffres_identiques == 'VV':
        return 10
    elif deux_chiffres_identiques == 'XX':
        return 20
    elif deux_chiffres_identiques == "LL":
        return 100
    elif deux_chiffres_identiques == 'CC':
        return 200
    elif deux_chiffres_identiques == 'DD':
        return 1000
    elif deux_chiffres_identiques == 'MM':
        return 2000


















