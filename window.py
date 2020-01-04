from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QFrame, QLabel, QSplitter, QStyleFactory, QApplication, QComboBox, QLineEdit, QVBoxLayout, QPushButton)
from PyQt5.QtCore import Qt
import sys

class Converter(QWidget):
    
    def __init__(self):
        super().__init__()
        QWidget.__init__(self)
        self.initUI()

    def initUI(self):      

        # Label displays
        self.lbl = QLabel("App to convert some currencies", self)

        # First checkbox

        hLayout = QHBoxLayout()
        comboCurrencyLeft = QComboBox()
        comboCurrencyLeft.addItem("C")
        comboCurrencyLeft.addItem("C++")

        # self.comboCurrencyLeft = QComboBox(self)
        # self.comboCurrencyLeft.addItem("Valentin")
        # self.comboCurrencyLeft.addItem("Antoine")
        # self.comboCurrencyLeft.addItem("Nicole")
        # self.comboCurrencyLeft.addItem("Michel")

        # Secound Checkbox
        comboCurrencyRight = QComboBox(self)
        comboCurrencyRight.addItem("CHEVREAU")
        comboCurrencyRight.addItem("SAMARCQ")
        comboCurrencyRight.setGeometry(50, 50, 50, 50)

        self.firstCurrency = QLineEdit()
        # champ.show()
        self.secundCurrency = QLineEdit()
        # champ1.show()
        
         # création du gestionnaire de mise en forme
        
        vLayout = QVBoxLayout()
        # ajout de la case à cocher au gestionnaire de mise en forme
        vLayout.addWidget(self.firstCurrency)
        vLayout.addWidget(comboCurrencyLeft)
        vLayout.addWidget(self.secundCurrency)
        vLayout.addWidget(comboCurrencyRight)
        # on fixe le gestionnaire de mise en forme de la fenêtre
        self.setLayout(vLayout)

        # création de l'étiquette
        self.label = QLabel()
        
        # création de l'étiquette
        self.label1 = QLabel()

        comboCurrencyLeft.move(50, 50)
        comboCurrencyRight.move(200, 50)

        self.setGeometry(1000, 600, 1000, 600)

        self.setWindowTitle('Currency Converter')
        self.show()

app = QApplication.instance() 
if not app:
    app = QApplication(sys.argv)
    
currency = Converter()
currency.show()

app.exec_()