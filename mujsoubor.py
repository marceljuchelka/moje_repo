class Ingredience:
    def __init__(self, nazev, mnozstvi, jednotka):
        self.nazev = nazev
        self.mnozstvi = mnozstvi
        self.jednotka = jednotka

    def __str__(self):
        return f"{self.nazev}: {self.mnozstvi} {self.jednotka}"


class Recept:
    def __init__(self, nazev, cas_pripravy, ingredience):
        self.nazev = nazev
        self.cas_pripravy = cas_pripravy
        self.ingredience = ingredience

    def zobraz_recept(self, pocet_porci=1):
        print(f"\nRecept na {self.nazev} pro {pocet_porci} porcí:")
        print(f"Čas přípravy: {self.cas_pripravy} minut")
        print("Ingredience:")
        for ingredience in self.ingredience:
            celkove_mnozstvi = ingredience.mnozstvi * pocet_porci
            print(f"- {ingredience.nazev}: {celkove_mnozstvi} {ingredience.jednotka}")


def pridat_recept():
    # Zadání základních informací o receptu
    nazev = input("Zadejte název receptu: ")
    cas_pripravy = int(input("Zadejte čas přípravy (v minutách): "))

    ingredience = []
    print("\nPřidávání ingrediencí (pro ukončení zadejte prázdný název):")

    # Přidávání ingrediencí
    while True:
        nazev_ingredience = input("Název ingredience: ")
        if not nazev_ingredience:  # Ukončení, pokud je název prázdný
            break
        mnozstvi = float(input(f"Množství {nazev_ingredience}: "))
        jednotka = input(f"Jednotka (g, ml, ks, špetka) pro {nazev_ingredience}: ")
        ingredience.append(Ingredience(nazev_ingredience, mnozstvi, jednotka))

    # Vytvoření receptu
    novy_recept = Recept(nazev, cas_pripravy, ingredience)
    return novy_recept


# Seznam receptů
recepty = []

# Hlavní program
print("Vítejte v programu pro správu receptů!")
while True:
    print("\nMožnosti:")
    print("1 - Přidat nový recept")
    print("2 - Zobrazit všechny recepty")
    print("3 - Ukončit")
    volba = input("Vyberte možnost: ")

    if volba == "1":
        recepty.append(pridat_recept())
    elif volba == "2":
        if not recepty:
            print("\nŽádné recepty nejsou uloženy.")
        else:
            for i, recept in enumerate(recepty, start=1):
                print(f"\nRecept {i}:")
                recept.zobraz_recept()
    elif volba == "3":
        print("Program ukončen. Děkujeme za použití!")
        break
    else:
        print("Neplatná volba, zkuste to znovu.")