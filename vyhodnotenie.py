hodnota = 1234

vloz = input("Vloz cislo:")

"""zoznam = [
    cisla 
    for cisla in vloz 
    if cisla in str(hodnota)
]"""

zoznam = []



bull_count = 0


for cisla in vloz:
    if cisla in str(hodnota):
        zoznam.append(cisla)

for index, (f, u) in enumerate(zip(str(hodnota), vloz)):
    if f == u:
        bull_count += 1



"""for index, prvok in enumerate(str(hodnota)):
    indexy.append(f"{index}: {prvok}")

for index, prvok in enumerate(vloz):
    indexy_vstup.append(f"{index}: {prvok}")

print(indexy)
print(indexy_vstup)
"""
vystup = len(zoznam)
#vystup1 = len(indexy)

if bull_count == 1:
    print(f"{bull_count} bull")
else:
    print(f"{bull_count} bulls")

if vystup == 1:
    print(f"{vystup} cow")
else:
    print(f"{vystup} cows")


