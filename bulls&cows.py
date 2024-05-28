"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Ján Jankovič
email: jankovic.jan4@gmail.com
discord: jano_15654 
"""

"""
Hi there!
-----------------------------------------------
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
-----------------------------------------------
Enter a number:
-----------------------------------------------
"""
import random

ciara = "-" * 47

# print uvodneho pozdravu uzivatela
def vypis_pozdrav():
    """
    Jednoduchá funkcia, ktorá po zavolaní vypíše
    úvodný pozdrav užívateľa.
    """
    return(
        f"Hi there!\n{ciara}\n"
        f"I've generated a random 4 digit number for you.\n"
        f"Let's play a bulls and cows game.\n{ciara}\n"
        f"Enter a number:\n{ciara}\n"    
    )

def vytvor_nahodne_cislo() -> int:
    """
    Funkcia, ktorá najprv vygeneruje prvé náhodné číslo, ktoré nesmie byť 0.
    Následne pomocou cyklu pridáva ďlašie 3 čísla. Číslo sa nesmie opakovať
    a nesmie byť už uložené v premennej prve_cislo aby sa zabezpečila unikátnosť.
    """
    
    # Vygenerovanie prvej číslice od 1 do 9
    prve_cislo = random.randint(1, 9)

    # Vygenerovanie zvyšných troch číslic od 0 do 9
    zvysne_cisla = []
    while len(zvysne_cisla) < 3:
        cislo = random.randint(0, 9)
        if cislo not in zvysne_cisla and cislo != prve_cislo:
            zvysne_cisla.append(cislo)

    # Spojenie prvej číslice a zvyšných číslic do jedného čísla
    nahodne_cislo = int(str(prve_cislo) + ''.join(map(str, zvysne_cisla)))
    return nahodne_cislo


print(vytvor_nahodne_cislo())







    
#print(vypis_pozdrav())