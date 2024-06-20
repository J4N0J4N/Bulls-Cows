"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Ján Jankovič
email: jankovic.jan4@gmail.com
discord: jano_15654 
"""

import random
import vstupna_hodnota 
import time

ciara = "-" * 47

# print uvodneho pozdravu uzivatela
def vypis_pozdrav():
    """
    Jednoduchá funkcia, ktorá po zavolaní vypíše
    úvodný pozdrav užívateľa.
    """
    print(
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

#moje_nahodne_cislo = vytvor_nahodne_cislo()

"""def main(fce: callable): #-> None:
    start = time.perf_counter()
    fce()
    stop = time.perf_counter()
    print(f"Celkem: {stop - start:.2f} sek")"""

def vyhodnot_cislo_uzivatela():

    moje_nahodne_cislo = vytvor_nahodne_cislo()
    print(moje_nahodne_cislo)
    
    guess_count = 1

    while True:
        moj_pokus_uhadnut = str((vstupna_hodnota.zadaj_hodnotu()))
        
        zoznam = []
        
        bull_count = 0

        for cisla in moj_pokus_uhadnut:
            if cisla in str(moje_nahodne_cislo):
                zoznam.append(cisla)

        for index, (f, u) in enumerate(zip(str(moje_nahodne_cislo), moj_pokus_uhadnut)):
            if f == u:
                bull_count += 1

        cow_count = len(zoznam)

        
        if bull_count == 4:
            if guess_count == 1:
                print(f"Correct, you've guessed the right number in {guess_count} guess!"
                      f"\n{ciara}\nThat's amazing!")
            elif guess_count in range(2, 4):
                print(f"Correct, you've guessed the right number in {guess_count} guesses!"
                      f"\n{ciara}\nThat's amazing!")
            elif guess_count in range(4, 11):
                print(f"Correct, you've guessed the right number in {guess_count} guesses!"
                      f"\n{ciara}\nThat's average!")
            else:
                print(f"Correct, you've guessed the right number in {guess_count} guesses!"
                      f"\n{ciara}\nThat's not so good!")
            break

        else:
            if bull_count and cow_count == 1:
                print(f"{bull_count} bull"
                      f"\n{cow_count} cow")
                guess_count += 1
            
            elif bull_count == 0 and cow_count == 1:
                print(f"{bull_count} bulls"
                      f"\n{cow_count} cow")
                guess_count += 1

            elif bull_count == 1 and cow_count > 1:
                print(f"{bull_count} bull"
                      f"\n{cow_count} cows")
                guess_count += 1

            else:
                print(f"{bull_count} bulls"
                      f"\n{cow_count} cows")
                guess_count += 1


        





#print(vytvor_nahodne_cislo())
vypis_pozdrav()
#print(vstupna_hodnota.zadaj_hodnotu())
vyhodnot_cislo_uzivatela()
#main(vyhodnot_cislo_uzivatela)