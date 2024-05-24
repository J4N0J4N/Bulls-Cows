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

#print uvodneho pozdravu uzivatela
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

#def vytvor_nahodne_cislo() -> int:
#    nahodne_cislo = randint(1000, 9999)
#    return nahodne_cislo

    
#print(vypis_pozdrav())