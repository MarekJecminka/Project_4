"""
projekt_4.py: čtvrtý projekt do Engeto Online Python Akademie

author: Marek Ječmínka
email: jecminkam@seznam.cz
"""

def pridat_ukol():
    while True:
        nazev_ukolu = input("\nZadejte název úkolu:")
        if nazev_ukolu == "":
            print("\nZadali jste prázdný vstup. Zadejte znovu název úkolu:")
        else:
            break

    while True:
        popis_ukolu = input("Zadejte popis úkolu:")
        if popis_ukolu == "":
            print("\nZadali jste prázdný vstup. Zadejte znovu popis úkolu:")
        else:
            break   

    print("\nÚkol '" + nazev_ukolu + "' byl přidán.\n")

    return (nazev_ukolu, popis_ukolu)

def zobrazit_ukoly(def_ukoly):
    print("\n")
    for i, ukol in enumerate(def_ukoly):
        print(str(i+1) + ". " + ukol[0] + " - " + ukol[1])

def odstranit_ukol(def_ukoly):
    while True:
        for i, ukol in enumerate(def_ukoly):
            print(str(i+1) + ". " + ukol[0] + " - " + ukol[1])

        odpoved_na_smazat = int(input("\nZadejte číslo úkolu, který chcete odstranit:"))

        if int(odpoved_na_smazat) not in range(1, str(len(def_ukoly))):
            print("\nVybral jste neexistující úkol. Zadejte znovu číslo úkolu.")
        else:
            break

    puvodni_ukoly = def_ukoly
    odstraneny_ukol = []
    for i, ukol in enumerate(puvodni_ukoly):
        if i+1 == int(odpoved_na_smazat):
            puvodni_ukoly.pop(i)
            odstraneny_ukol.append(ukol)
    
    aktualizoavane_ukoly = puvodni_ukoly

    print("\nÚkol '" + odstraneny_ukol[0] + "' byl odstraněn.")

    return aktualizoavane_ukoly

def hlavni_menu():
    ukoly = []
    while True:
        print(
            "",
            "Správce úkolů - Hlavní menu:",
            "1. Přidat nový úkol",
            "2. Zobrazit všechny úkoly",
            "3. Odstranit úkol",
            "4. Konec programu",
            sep = "\n")

        odpoved = input("\nVyberte možnost (1-4): ")

        if int(odpoved) not in range(1,4):
            print("\nNeplatný vstup. Zadej číslo od 1 do 4.")
        elif odpoved == "1":
            ukoly.append(pridat_ukol())
        elif odpoved == "2":
            zobrazit_ukoly(ukoly)
        elif odpoved == "3":
            ukoly = odstranit_ukol(ukoly)
        elif odpoved == "4":
            print("\nKonec programu.")
            break

if __name__ == "__main__":
    hlavni_menu()
