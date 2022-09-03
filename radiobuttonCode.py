

import sys
from PyQt5 import QtWidgets
from radioButton import Ui_MainWindow

class myApp(QtWidgets.QMainWindow):

    def __init__(self):
        super(myApp,self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_tr.setChecked(True)
        self.ui.edu_pri.setChecked(True)

        self.ui.btn_tr.toggled.connect(self.onClickedCountry)
        self.ui.btn_ge.toggled.connect(self.onClickedCountry)
        self.ui.btn_de.toggled.connect(self.onClickedCountry)
        self.ui.btn_fr.toggled.connect(self.onClickedCountry)

        self.ui.edu_middle.toggled.connect(self.onClickedEdu)
        self.ui.edu_pri.toggled.connect(self.onClickedEdu)
        self.ui.edu_hgh.toggled.connect(self.onClickedEdu)
        self.ui.edu_col.toggled.connect(self.onClickedEdu)

        self.ui.btn_SelectedCt.clicked.connect(self.getSelectedCountry)
        self.ui.btn_SelectedEdu.clicked.connect(self.getSelectedEdu)


    def onClickedCountry(self):
        rb = self.sender()
        # if rb.isChecked():
        #     print('seçilen radio: '+ rb.text())


    def onClickedEdu(self):
        rb = self.sender()
        # if rb.isChecked():
        #     print('Seçilen eğitim: '+ rb.text())


    def getSelectedCountry(self):
        items = self.ui.groupBoxCountry.findChildren(QtWidgets.QRadioButton)
        for rb in items:
            if rb.isChecked():
                self.ui.lblUlke.setText('You choosed '+ rb.text().title())

    def getSelectedEdu(self):
        items = self.ui.groupBoxEdu.findChildren(QtWidgets.QRadioButton)
        for rb in items:
            if rb.isChecked():
                self.ui.lblEgitim.setText('You choosed '+ rb.text().title())


def app():
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())

app()