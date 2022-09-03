
from operator import itemgetter
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
import sys
from tableForm import Ui_MainWindow


class myApp(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(myApp, self).__init__()
    
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_save.clicked.connect(self.saveProduct)

        self.loadProducts()


    def saveProduct(self):
        name = self.ui.txt_name.text()
        price = self.ui.txt_price.text()

        if name and price is not None:
            rowCount = self.ui.tableProducts.rowCount()
            self.ui.tableProducts.insertRow(rowCount)
            self.ui.tableProducts.setItem(rowCount,0, QTableWidgetItem(name))
            self.ui.tableProducts.setItem(rowCount,1, QTableWidgetItem(price))

    
    
    def loadProducts(self):

        products =[
            {'name':'Sony Xperia Z3', 'price': 4000},
            {'name':'Sony Xperia Z4', 'price': 7000},
            {'name':'Sony Xperia Z4 Plus', 'price': 11000},
            {'name':'Sony Xperia Z5', 'price': 12000}
        ]


        self.ui.tableProducts.setRowCount(len(products))
        self.ui.tableProducts.setColumnCount(2)
        self.ui.tableProducts.setHorizontalHeaderLabels(('Name','Price'))
        self.ui.tableProducts.setColumnWidth(0,200)
        self.ui.tableProducts.setColumnWidth(1,100)

        rowIndex = 0

        for product in products:
            self.ui.tableProducts.setItem(rowIndex,0, QTableWidgetItem(product['name']))
            self.ui.tableProducts.setItem(rowIndex,1, QTableWidgetItem(str(product['price'])))


            rowIndex +=1


        # self.ui.tableProducts.setItem(0,1, QTableWidgetItem('5000'))
        # self.ui.tableProducts.setItem(1,0, QTableWidgetItem('Samsung S6'))
        # self.ui.tableProducts.setItem(1,1, QTableWidgetItem('7000'))
        # self.ui.tableProducts.setItem(2,0, QTableWidgetItem('Samsung S9'))
        # self.ui.tableProducts.setItem(2,1, QTableWidgetItem('9000'))















def app():
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())

app()