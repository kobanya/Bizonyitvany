class Diak:
    def __init__(self, nev, magyar, tortenelem, matematika, idegen_nyelv, igazolt_hianyzas, igazolatlan_hianyzas):
        self.nev = nev
        self.magyar = magyar
        self.tortenelem = tortenelem
        self.matematika = matematika
        self.idegen_nyelv = idegen_nyelv
        self.igazolt_hianyzas = igazolt_hianyzas
        self.igazolatlan_hianyzas = igazolatlan_hianyzas

    def Adatsor(self):
        print(f"Név: {self.nev}")
        print(f"Magyar: {self.magyar}")
        print(f"Történelem: {self.tortenelem}")
        print(f"Matematika: {self.matematika}")
        print(f"Idegen Nyelv: {self.idegen_nyelv}")
        print(f"Igazolt Hiányzás: {self.igazolt_hianyzas}")
        print(f"Igazolatlan Hiányzás: {self.igazolatlan_hianyzas}")

    def atlag(self):
        return (self.magyar + self.tortenelem + self.matematika + self.idegen_nyelv) / 4.0


def main():
    diakok = []

    # Első diák hozzáadása
    diak1 = Diak("Kázmér", 3, 2, 5, 5, 10, 0)
    diakok.append(diak1)
    print("Első diák adatai:")
    diak1.Adatsor()

    # További diákok beolvasása az osztaly.txt állományból
    try:
        with open("osztaly.txt", "r") as file:
            for sor in file:
                adatok = sor.strip().split(",")
                nev = adatok[0]
                magyar = int(adatok[1])
                tortenelem = int(adatok[2])
                matematika = int(adatok[3])
                idegen_nyelv = int(adatok[4])
                igazolt_hianyzas = int(adatok[5])
                igazolatlan_hianyzas = int(adatok[6])

                diak = Diak(nev, magyar, tortenelem, matematika, idegen_nyelv, igazolt_hianyzas, igazolatlan_hianyzas)
                diakok.append(diak)
    except FileNotFoundError:                   # hibakezelés
        print("Az osztaly.txt állomány nem található.")

    # Diákok átlagának kiíratása
    print('-----------------------------------------\nDiákok átlaga:\n')
    for diak in diakok:
       print(f"{diak.nev} átlaga: {diak.atlag()}")

    print("\nDiákok adatai:")
    print(f"{'A diák neve':20} {'Magyar':6} {'Történelem':10} {'Matematika':12}{'Idegen Nyelv':15}"
          f"{'Igazolt Hiányzás':15}  {'Igazolatlan Hiányzás':20}  {'Átlag':12}")


    for diak in diakok:
        print(f'{diak.nev :20} {diak.magyar :5}  {diak.tortenelem :8} {diak.matematika :8} {diak.idegen_nyelv :11}'
              f' {diak.igazolt_hianyzas :12} óra {diak.igazolt_hianyzas :12} óra{diak.atlag():19} ')

if __name__ == "__main__":
    main()
