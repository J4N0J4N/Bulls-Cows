def zadaj_hodnotu() -> int:

    """zapracovat try/except/else
       napisat cez cyklus while?
       doplniť kontrolu duplicít
    """

    
    cislo_uzivatela = input(">>> ")

    try:

        cislo_int = int(cislo_uzivatela)

    except ValueError:
        print("hodnota nie je cislo")
        zadaj_hodnotu()

    else:

        if len(cislo_uzivatela) != 4:
            print("Your number has to contain exactly 4 digits!")
            zadaj_hodnotu()

        if cislo_uzivatela[0] == "0":
            print("Your number can't start with zero")
            zadaj_hodnotu()


        return(cislo_int)
    


