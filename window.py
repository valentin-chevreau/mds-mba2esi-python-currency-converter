from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QFrame, QLabel, QSplitter, QStyleFactory, QApplication, QComboBox, QLineEdit)
from PyQt5.QtCore import Qt
from currency_converter import CurrencyConverter
from currency_list import list
import sys

class Converter(QWidget):
    
    def __init__(self):
        super().__init__()
        QWidget.__init__(self)
        self.initUI()

    def initUI(self):
        # name of the window program
        self.setWindowTitle('Currency Converter')

        # initialise the currency converter 
        c = CurrencyConverter()

        # display a title at the beginning of the program
        self.lbl = QLabel("Currency Convert", self)

        # create checkbox of currencies
        comboCurrencyLeft = QComboBox()
        comboCurrencyRight = QComboBox()

        # initalize the chexbox positions
        comboCurrencyLeft.move(50, 50)
        comboCurrencyRight.move(200, 50)

        # retrieve
        for key in list.keys():
            # add current currency to checkbox
            comboCurrencyLeft.addItem(key)
            comboCurrencyRight.addItem(key)
        comboCurrencyLeft.setGeometry(50, 50, 50, 50)        
        comboCurrencyRight.setGeometry(50, 50, 50, 50)

        self.firstCurrency = QLineEdit()
        self.secundCurrency = QLineEdit()
        
        # front display: display in horizontal
        hLayout = QHBoxLayout()
        # add widgets needed to displayed
        hLayout.addWidget(self.firstCurrency)
        hLayout.addWidget(comboCurrencyLeft)
        hLayout.addWidget(self.secundCurrency)
        hLayout.addWidget(comboCurrencyRight)
        
        self.setLayout(hLayout)

        # création de l'étiquette
        self.label = QLabel()
        
        # création de l'étiquette
        self.label1 = QLabel()

    
        self.setGeometry(500, 300, 500, 300)
        
        self.show()

app = QApplication.instance() 
if not app:
    app = QApplication(sys.argv)
    
    currency = Converter()
    currency.show()

app.exec_()