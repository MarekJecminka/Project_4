"""
projekt_4.py: čtvrtý projekt do Engeto Online Python Akademie

author: Marek Ječmínka
email: jecminkam@seznam.cz
"""

def pridat_ukol():
    while True:
        nazev_ukolu = input("Zadejte název úkolu:")
        if nazev_ukolu == "":
            print("Zadali jste prázdný vstup. Zadejte znovu název úkolu:")
        else:
            break

    while True:
        popis_ukolu = input("Zadejte popis úkolu:")
        if popis_ukolu == "":
            print("Zadali jste prázdný vstup. Zadejte znovu popis úkolu:")
        else:
            break   

    print("Úkol '" + nazev_ukolu + "' byl přidán.")

    return (nazev_ukolu, popis_ukolu)

def zobrazit_ukoly(def_ukoly):
    for i, ukol in enumerate(def_ukoly):
        for nazev, popis in ukol:
            print(i+1 + ". " + nazev + " - " + popis)

def odstranit_ukol(def_ukoly):
    while True:
        for i, ukol in enumerate(def_ukoly):
            for nazev, popis in ukol:
                print(i+1 + ". " + nazev + " - " + popis)

        odpoved_na_smazat = input("Zadejte číslo úkolu, který chcete odstranit:")

        if int(odpoved_na_smazat) not in (1, str(len(def_ukoly))):
            print("Vybral jste neexistující úkol. Zadejte znovu číslo úkolu.")
        else:
            break

    puvodni_ukoly = def_ukoly
    odstraneny_ukol = []
    for i, ukol in enumerate(puvodni_ukoly):
        for nazev, popis in ukol:
            if i+1 == odpoved_na_smazat:
                puvodni_ukoly.pop(ukol)
                odstraneny_ukol.append(ukol)
    
    aktualizoavane_ukoly = puvodni_ukoly

    print("Úkol '" + odstraneny_ukol[0] + "' byl odstraněn.")

    return aktualizoavane_ukoly

def hlavni_menu():
    while True:
        ukoly = []
        odpoved = input(
            "Správce úkolů - Hlavní menu",
            "1. Přidat nový úkol",
            "2. Zobrazit všechny úkoly",
            "3. Odstranit úkol"
            "4. Konec programu",
            "Vyberte možnost (1-4):",
            sep = "\n")

        if odpoved not in range(1,4):
            print("Neplatný vstup. Zadej číslo od 1 do 4")
        elif odpoved == "1":
            ukoly.append(pridat_ukol())
        elif odpoved == "2":
            zobrazit_ukoly(ukoly)
        elif odpoved == "3":
            ukoly = odstranit_ukol(ukoly)
        elif odpoved == "4":
            print("Konec programu.")
            break

if "__name__" == "__main__":
    hlavni_menu()
