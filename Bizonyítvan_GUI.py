import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem
from PyQt5.QtWidgets import QMainWindow




class Diak:
    def __init__(self, nev, magyar, tortenelem, matematika, idegen_nyelv, igazolt_hianyzas, igazolatlan_hianyzas):
        self.nev = nev
        self.magyar = magyar
        self.tortenelem = tortenelem
        self.matematika = matematika
        self.idegen_nyelv = idegen_nyelv
        self.igazolt_hianyzas = igazolt_hianyzas
        self.igazolatlan_hianyzas = igazolatlan_hianyzas

    def atlag(self):
        return (self.magyar + self.tortenelem + self.matematika + self.idegen_nyelv) / 4.0


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Diákok Adatai")
        self.setGeometry(100, 100, 1900, 400)

        self.table_widget = QTableWidget(self)
        self.table_widget.setGeometry(390, 10, 1470, 380)

        self.show_data()

    def show_data(self):
        diakok = []

        # Első diák hozzáadása
        diak1 = Diak("Kázmér", 3, 2, 5, 5, 10, 0)
        diakok.append(diak1)

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
        except FileNotFoundError:
            print("Az osztaly.txt állomány nem található.")

        self.table_widget.setRowCount(len(diakok))
        self.table_widget.setColumnCount(8)
        self.table_widget.setHorizontalHeaderLabels(
            ["A diák neve", "Magyar", "Történelem", "Matematika", "Idegen Nyelv",
             "Igazolt Hiányzás", "Igazolatlan Hiányzás", "Átlag"])

        for row, diak in enumerate(diakok):
            self.table_widget.setItem(row, 0, QTableWidgetItem(diak.nev))
            self.table_widget.setItem(row, 1, QTableWidgetItem(str(diak.magyar)))
            self.table_widget.setItem(row, 2, QTableWidgetItem(str(diak.tortenelem)))
            self.table_widget.setItem(row, 3, QTableWidgetItem(str(diak.matematika)))
            self.table_widget.setItem(row, 4, QTableWidgetItem(str(diak.idegen_nyelv)))
            self.table_widget.setItem(row, 5, QTableWidgetItem(str(diak.igazolt_hianyzas)))
            self.table_widget.setItem(row, 6, QTableWidgetItem(str(diak.igazolatlan_hianyzas)))
            self.table_widget.setItem(row, 7, QTableWidgetItem(str(diak.atlag())))

        self.table_widget.resizeColumnsToContents()
        self.table_widget.resizeRowsToContents()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()  # MainWindow osztály példányosítása

    window.show()
    sys.exit(app.exec_())