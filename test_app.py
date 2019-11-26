from app import *


def test_decoder_chiffre_romain():
    assert decoder_chiffre_romain('I') == 1
    assert decoder_chiffre_romain('V') == 5
    assert decoder_chiffre_romain('X') == 10
    assert decoder_chiffre_romain('L') == 50
    assert decoder_chiffre_romain('C') == 100
    assert decoder_chiffre_romain('D') == 500
    assert decoder_chiffre_romain('M') == 1000


def test_decoder_deux_chiffres_romains_identiques():
    assert decoder_deux_chiffres_romains_identiques('II') == 2
    assert decoder_deux_chiffres_romains_identiques('VV') == 10
    assert decoder_deux_chiffres_romains_identiques('XX') == 20
    assert decoder_deux_chiffres_romains_identiques('LL') == 100
    assert decoder_deux_chiffres_romains_identiques('CC') == 200
    assert decoder_deux_chiffres_romains_identiques('DD') == 1000
    assert decoder_deux_chiffres_romains_identiques('MM') == 2000