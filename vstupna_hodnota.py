def zadaj_hodnotu() -> int:
    """
    Vráť celé číslo, zadané užívateľom, ktoré nezačína nulou, obsahuje presne 4 hodnoty
    a je unikátne.
    
    Cyklus beží, kým užívateľ nezadá správnu hodnotu, napríklad "1234".
    
    :Príklady zle zadanej hodnoty:
    >>> cislo_uzivatela = 0123
    >>> cislo_uzivatela = 123
    >>> cislo_uzivatela = 12345
    >>> cislo_uzivatela = 12as
    >>> cislo_uzivatela = 1223
    >>> cislo_uzivatela = 1.23
    """

    while True:

        # Vstupná hodnota od užívateľa
        cislo_uzivatela = input(">>> ")

        try:

            # Ak je hodnotu od užívateľa možné zmeniť na integer, 
            # po splnení podmienok vráti zadanú hodnotu ako typ integer
            cislo_int = int(cislo_uzivatela)

            # Kontrola dĺžky
            if len(cislo_uzivatela) != 4:
                print("Your number must contain exactly 4 digits!")
                continue

            # Kontrola, či číslo nezačína nulou
            if cislo_uzivatela[0] == "0":
                print("Your number can't start with zero")
                continue

            # Kontrola duplicít
            # Ak sa v set() vyskytujú rovnaké znaky, vráti iba jeden z nich,
            # tým pádom počet prvkov != 4 a vstup obsahuje duplikované znaky
            if len(set(cislo_uzivatela)) != 4:
                print("Your number must not contain duplicate digits!")
                continue

            return cislo_int

        # Upozornenie v prípade, že vstup od užívateľa nie je možné zmeniť na integer
        except ValueError:
            print("Your input must be an integer")
