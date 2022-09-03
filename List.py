

from operator import index
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QInputDialog, QLineEdit, QMessageBox
import sys
from ListForm import Ui_MainWindow


class myApp(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(myApp, self).__init__()
    
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # load students

        self.loadStudents()

        # add new student

        self.ui.btn_add.clicked.connect(self.addStudent)

        # edit student
        self.ui.btn_edit.clicked.connect(self.editStudent)

        # delete student
        self.ui.btn_remove.clicked.connect(self.removeStudent)
        
        # up student

        self.ui.btn_up.clicked.connect(self.upStudent)

        # down student

        self.ui.btn_down.clicked.connect(self.downStudent)

        # sort student

        self.ui.btn_sort.clicked.connect(self.sortStudents)

        # close list

        self.ui.btn_exit.clicked.connect(self.close)

    def loadStudents(self):
        self.ui.listItems.addItems(['Ali', 'Osman', 'Ali Osman'])
        self.ui.listItems.setCurrentRow(0)

    def addStudent(self):
        text, ok =QInputDialog.getText(self, 'New Student', 'Student Name')

        if ok and text is not None:
            currentIndex = self.ui.listItems.currentRow()
            self.ui.listItems.insertItem(currentIndex, text)
        else:
            pass

    def editStudent(self):
        currentIndex = self.ui.listItems.currentRow()
        item = self.ui.listItems.item(currentIndex)

        if item is not None:
            text, ok = QInputDialog.getText(self, 'Edit Student', 'Student Name', QLineEdit.Normal, item.text())
            if text and ok is not None:
                item.setText(text)


    def removeStudent(self):
        currentIndex = self.ui.listItems.currentRow()
        item = self.ui.listItems.item(currentIndex)
        if item is None:
            return
        
        q = QMessageBox.question(self, 'Remove Student', 'Do you want to remove student ' + item.text() + ' ?',QMessageBox.Yes | QMessageBox.No)

        if q == QMessageBox.Yes:
            item = self.ui.listItems.takeItem(currentIndex)
            del item
    

    def upStudent(self):
        currentIndex = self.ui.listItems.currentRow()
        if currentIndex >= 1:
            item = self.ui.listItems.takeItem(currentIndex)
            self.ui.listItems.insertItem(currentIndex-1, item)
            self.ui.listItems.setCurrentItem(item)


    def downStudent(self):
        currentIndex = self.ui.listItems.currentRow()
        if currentIndex < self.ui.listItems.count() -1:
            item = self.ui.listItems.takeItem(currentIndex)
            self.ui.listItems.insertItem(currentIndex+1, item)
            self.ui.listItems.setCurrentItem(item)

    
    def sortStudents(self):
        self.ui.listItems.sortItems()


    def close(self):
        quit()


def app():
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())

app()