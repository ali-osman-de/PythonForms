
from PyQt5 import QtWidgets
import sys
from msgboxform import Ui_MainWindow


class myApp(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(myApp, self).__init__()
    
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_exit.clicked.connect(self.showDialog)

    def showDialog(self):

        result = QtWidgets.QMessageBox.question(self, 'Close Application', 'Are your sure?', QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel | QtWidgets.QMessageBox.Ignore, QtWidgets.QMessageBox.Cancel)

        if result == QtWidgets.QMessageBox.Ok:
            print('Yes clicked')
            QtWidgets.qApp.quit()
        else:
            print('No clicked')




        # msg = QtWidgets.QMessageBox()

        # msg.setWindowTitle('Close Appliacation')
        # msg.setText('Are you sure?')
        # msg.setIcon(msg.Warning)
        # msg.setStandardButtons(msg.Ok | msg.Cancel | msg.Ignore)
        # msg.setDefaultButton(msg.Cancel)
        # msg.setDetailedText('details...')
        # msg.buttonClicked.connect(self.popup_button)

    #     x = msg.exec_()
        
    # def popup_button(self, i):
    #     print(i.text())

        # if i.text() == 'OK':
        #     QtWidgets.qApp.quit()
        # elif i.text() == 'Cancel':
        #     QtWidgets.qApp.
        # else:
        #     print('Ignore')








def app():
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())

app()