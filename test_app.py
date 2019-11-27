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


def test_decoder_n_chiffres_romains_identiques():
    assert decoder_n_chiffres_romains_identiques('III') == 3
    assert decoder_n_chiffres_romains_identiques('VVV') == 15
    assert decoder_n_chiffres_romains_identiques('XXX') == 30
    assert decoder_n_chiffres_romains_identiques('LLL') == 150
    assert decoder_n_chiffres_romains_identiques('CCC') == 300
    assert decoder_n_chiffres_romains_identiques('DDD') == 1500
    assert decoder_n_chiffres_romains_identiques('MMMMM') == 5000



def test_conversion_nombre_romain():
    assert conversion_nombre_romain('IV') == 4
    assert conversion_nombre_romain('IX') == 9
    assert conversion_nombre_romain('VIII') == 8
    assert conversion_nombre_romain('XXV') == 25
    assert conversion_nombre_romain('CD') == 400
    assert conversion_nombre_romain('MMXIX') == 2019
    assert conversion_nombre_romain('MCMXLIV') == 1944


def test_addition_nombres_romains():
    assert addition_nombres_romains('X', 'V') == 15
    assert addition_nombres_romains('IX', 'I') == 10
    assert addition_nombres_romains('C', 'L') == 150
    assert addition_nombres_romains('XIV', 'M') == 1014
    assert addition_nombres_romains('XX', 'V') == 25
    assert addition_nombres_romains('I', 'MMXIX') == 2020
    assert addition_nombres_romains('C', 'CD') == 500


def test_soustraction_nombres_romains():
    assert soustraction_nombres_romains('X', 'V') == 5
    assert soustraction_nombres_romains('IX', 'I') == 8
    assert soustraction_nombres_romains('C', 'L') == 50
    assert soustraction_nombres_romains('XIV', 'M') == -986
    assert soustraction_nombres_romains('XX', 'V') == 15
    assert soustraction_nombres_romains('I', 'MMXIX') == -2018
    assert soustraction_nombres_romains('C', 'CD') == -300


def test_multiplication_nombres_romains():
    assert multiplication_nombres_romains('X', 'V') == 50
    assert multiplication_nombres_romains('IX', 'I') == 9
    assert multiplication_nombres_romains('C', 'L') == 5000
    assert multiplication_nombres_romains('XIV', 'M') == 14000
    assert multiplication_nombres_romains('XX', 'V') == 100
    assert multiplication_nombres_romains('I', 'MMXIX') == 2019
    assert multiplication_nombres_romains('C', 'CD') == 40000


def test_division_nombres_romains():
    assert division_nombres_romains('X', 'V') == 2
    assert division_nombres_romains('IX', 'I') == 9
    assert division_nombres_romains('C', 'L') == 2
    assert division_nombres_romains('M', 'X') == 100
    assert division_nombres_romains('XX', 'V') == 4
    assert division_nombres_romains('MMXIX', 'IV') == 504
    assert division_nombres_romains('CD', 'C') == 4



def test_calculatrice_nombres_romains():
    assert calculatrice_nombres_romains('+', 'X', 'V') == 15
    assert calculatrice_nombres_romains('+', 'XIV', 'M') == 1014
    assert calculatrice_nombres_romains('-', 'X', 'V') == 5
    assert calculatrice_nombres_romains('-', 'XIV', 'M') == -986
    assert calculatrice_nombres_romains('*', 'X', 'V') == 50
    assert calculatrice_nombres_romains('*', 'XX', 'VI') == 120
    assert calculatrice_nombres_romains('/', 'X', 'V') == 2
    assert calculatrice_nombres_romains('/', 'IX', 'III') == 3



######################################################################################




def test_decoder_chiffre_en_romain():
    assert decoder_chiffre_en_romain(1) == 'I'
    assert decoder_chiffre_en_romain(2) == 'II'
    assert decoder_chiffre_en_romain(3) == 'III'
    assert decoder_chiffre_en_romain(4) == 'IV'
    assert decoder_chiffre_en_romain(5) == 'V'
    assert decoder_chiffre_en_romain(6) == 'VI'
    assert decoder_chiffre_en_romain(7) == 'VII'
    assert decoder_chiffre_en_romain(8) == 'VIII'
    assert decoder_chiffre_en_romain(9) == 'IX'
    assert decoder_chiffre_en_romain(10) == 'X'

    assert decoder_chiffre_en_romain(50) == 'L'
    assert decoder_chiffre_en_romain(100) == 'C'
    assert decoder_chiffre_en_romain(500) == 'D'
    assert decoder_chiffre_en_romain(1000) == 'M'












