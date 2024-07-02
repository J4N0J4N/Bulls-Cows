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

# Vyprintovanie úvodu do hry
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
   
    # Vrátenie unikátneho 4-miestneho čísla
    return nahodne_cislo

def ziskaj_pokus_uzivatela() -> str:
    """
    Získa a vráti pokus od užívateľa ako reťazec na základe modulu vstupna_hodnota.py
    """
    return str(vstupna_hodnota.zadaj_hodnotu())

def vyhodnot_pokus(moje_nahodne_cislo: str, moj_pokus_uhadnut: str) -> (int, int): # type: ignore
    """ 
    Vyhodnotí pokus a vráti počet bulls a cows. Jednotlivé kroky sú
    popisované priebežne.
    """
    spravne_cislice = []
    bull_count = 0

    """
    Cyklus iteruje cez číslo zadané užívateľom. Ak sa niektorá číslica z čísla
    zadaného užívateľom nachádza v náhodne vygenerovanom čísle, pridá ju do zoznamu
    spravne_cislice.
    """
    for cisla in moj_pokus_uhadnut:
        if cisla in str(moje_nahodne_cislo):
            spravne_cislice.append(cisla)
    
    # Po prejdení cyklu funkcia uloží do premennej cow_count počet číslic, ktoré sú v liste spravne_cislice.
    cow_count = len(spravne_cislice)

    """
    zip() spojí čislice z vygenerovaného čísla a čísla od užívateľa do dvojíc.
    enumerate() pridá týmto dvojiciam index a cyklus iteruje v podstate cez trojice 
    číslic. Ak sa dvojica čísel na jednom indexe rovná, pripočíta sa 1 do premennej
    bull_count. V takom prípade sa zároveň odpočíta jedna hodnota z premennej cow_count.
    """

    for index, (cislica_generovana, cislica_pokus) in enumerate(zip(str(moje_nahodne_cislo), moj_pokus_uhadnut)):
        if cislica_generovana == cislica_pokus:
            bull_count += 1
            cow_count -= 1   # odpočíta hodnotu z premennej cow_count v prípade, že hráč uhádne správnu číslicu 
                             # na správnom mieste, teda bull_count += 1

    return bull_count, cow_count
        
def vytvor_vystup(bull_count: int, cow_count: int, guess_count: int) -> None:
    """
    Vytvorí a vyprintuje výstup na základe počtu bulls, cows a počtu pokusov.
    Ak hráč uhádne číslo (bull_count == 4) => funkcia vyhodnocuje koľko pokusov
    na uhádnutie potreboval a hráča na konci hry ohodnotí a vráti True.

    Ak hráč neuhádne celé číslo, v závislosti na počte uhádnutých číslic vyprintuje
    počet bull/bulls a cow/cows v jednotnom alebo množnom čísle a vráti False.
    """
    if bull_count == 4:
        if guess_count == 1:
            print(f"Correct, you've guessed the right number in {guess_count} guess!\nThat's amazing!")
        elif guess_count in range(2, 4):
            print(f"Correct, you've guessed the right number in {guess_count} guesses!\nThat's amazing!")
        elif guess_count in range(4, 11):
            print(f"Correct, you've guessed the right number in {guess_count} guesses!\nThat's average!")
        else:
            print(f"Correct, you've guessed the right number in {guess_count} guesses!\nThat's not so good!")
        return True
    else: # výpis bol upravený o podmienky tak, aby sa správne v rôznych situáciách vypisovalo bull/bulls a cow/cows 
        if bull_count == 1 and cow_count == 1:
            print(f"{bull_count} bull\n{cow_count} cow")
        elif bull_count == 1 and cow_count == 0:
            print(f"{bull_count} bull\n{cow_count} cows")
        elif bull_count == 0 and cow_count == 1:
            print(f"{bull_count} bulls\n{cow_count} cow")
        elif bull_count == 1 and cow_count > 1:
            print(f"{bull_count} bull\n{cow_count} cows")
        elif bull_count > 1 and cow_count == 1:
            print(f"{bull_count} bulls\n{cow_count} cow")
        else:
            print(f"{bull_count} bulls\n{cow_count} cows")
        return False

def vyhodnot_cislo_uzivatela() -> None:
    """
    Funkcia najprv zavolá funkciu vytvor_nahodne_cislo() a uloží ho do premennej
    moje_nahodne_cislo. Potom sa inicializuje cyklus while, ktorý beži až kým
    hráč neuhádne správne číslo. Cyklus zavolá funkciu ziskaj_pokus_uzivatela(), 
    ktorá od hráča získa jeho pokus na uhádnutie čísla a uloží ho do premennej
    moj_pokus_uhadnut. Potom je zavolaná funkcia vyhodnot_pokus() s argumentami
    moje_nahodne_cislo a moj_pokus_uhadnut, ktorá vracia počet bull/bulls a cow/cows
    a ukladá ich do premenných bull_count a cow_count. Do cyklku je vnorená podmienka,
    ktorá volá funkciu vytvor_vystup(). Ak funkcia vráti True (hráč uhádol číslo),
    cyklus sa ukončí. Ak funkcia vráti False, cyklus pokračuje a do premennej guess_count
    sa pripočíta 1 (započíta sa pokus). Premenná guess_count je defaultne nastavená na 1,
    aby sa započítal už prvý pokus.
    """
    moje_nahodne_cislo = vytvor_nahodne_cislo()    
    guess_count = 1

    while True:
        moj_pokus_uhadnut = ziskaj_pokus_uzivatela()
        bull_count, cow_count = vyhodnot_pokus(moje_nahodne_cislo, moj_pokus_uhadnut)
        
        if vytvor_vystup(bull_count, cow_count, guess_count):
            break
        guess_count += 1

    def zapis_statistiky() -> None:
        """
        Vnorená funkcia, ktorá uchováva štatistiku počtu odhadov pre jednotlivé hry.
        Pracuje s premennou guess_count z funkcie vyhodnot_cislo_uzivatela(), do
        ktorej je vnorená.
        """
        with open("statistika.txt", 
                  mode="a", 
                  encoding="UTF-8") as txt_soubor:
            txt_soubor.write(f"\nDuring this round, the number of attemts you needed was {guess_count}")
    zapis_statistiky()

def main(fce: callable) -> None:
    """
    Funkcia, ktorá meria čas v sekundách za ktorý užívateľ uhádne číslo.
    """
    start = time.perf_counter()
    fce()
    stop = time.perf_counter()
    print(f"The time it took you to guess: {stop - start:.2f} sek")

if __name__ == "__main__":
    main(vyhodnot_cislo_uzivatela)
    
