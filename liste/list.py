from os import remove
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QInputDialog, QLineEdit,QMessageBox
import sys
import mysql.connector 
from numpy import delete
from liste import  Ui_MainWindow

class list_ders(QtWidgets.QMainWindow):
    def __init__(self):
        super(list_ders, self).__init__()
        self.ui= Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.listWidget.setCurrentRow(0)
        self.ui.btn_add.clicked.connect(self.add)
        self.ui.btn_edit.clicked.connect(self.edit)
        self.ui.btn_reomve.clicked.connect(self.remove)
        self.ui.btn_up.clicked.connect(self.up)
        self.ui.btn_down.clicked.connect(self.down)
        self.ui.pushButton_7.clicked.connect(self.sort)
        self.ui.btn_exit.clicked.connect(self.exit)
        self.connection = mysql.connector.connect(host = "localhost", user = "root", password = "9453199a", database = "ogrenciler")
        self.loadStudents()

    def loadStudents(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT ogrenci_isim FROM new_table")
        rows = cursor.fetchall()
        for row in rows:
            self.ui.listWidget.addItem(row[0])

    def add(self):
        text, ok = QInputDialog.getText(self, 'yeni öğrenci ekleme', 'öğrenci adı')
        if ok and text is not None:
            self.ui.listWidget.addItem(text)
            cursor = self.connection.cursor()
            sql = "INSERT INTO new_table(ogrenci_isim) VALUES (%s)"
            values = (text,)
            cursor.execute(sql,values)
            self.connection.commit()

        
    def edit(self):
        index_al = self.ui.listWidget.currentRow()
        item = self.ui.listWidget.item(index_al)

        if item is not None:
            text, ok = QInputDialog.getText(self, "edit student", "student Name", QLineEdit.Normal, item.text())
            if text and ok is not None:
                item.setText(text)
                cursor = self.connection.cursor()
                sql = "UPDATE new_table SET ogrenci_isim = %s WHERE ogrenci_isim = %s"
                values = [text, item.text()]
                cursor.execute(sql, values)
                self.connection.commit()
                loadStudents()

    def remove(self):
        index = self.ui.listWidget.currentRow()
        item = self.ui.listWidget.item(index)

        if item is None:
            return

        q = QMessageBox.question(self, "remove student", "do you want to remove student: "   + item.text(), QMessageBox.Yes | QMessageBox.No)
        if q == QMessageBox.Yes:
            cursor = self.connection.cursor()
            sql = "DELETE FROM new_table WHERE ogrenci_isim = %s"
            values = (item.text(),)
            cursor.execute(sql, values)
            self.connection.commit()

            item = self.ui.listWidget.takeItem(index)
            del item
            self.loadStudents()

    def up(self):
        index = self.ui.listWidget.currentRow()
        if index >= 1:
            item = self.ui.listWidget.takeItem(index)
            self.ui.listWidget.insertItem(index-1, item)
            self.ui.listWidget.setCurrentItem(item)

    def down(self):
        index = self.ui.listWidget.currentRow()
        if index < self.ui.listWidget.count()-1: 
            item = self.ui.listWidget.takeItem(index)
            self.ui.listWidget.insertItem(index+1, item)
            self.ui.listWidget.setCurrentItem(item)
    def exit(self):
        self.loadStudents() 

        quit()
    def sort(self):
        self.ui.listWidget.sortItems()
    def ic():
        pass
def acma():
    acma = QtWidgets.QApplication(sys.argv)
    window = list_ders()
    window.show()
    sys.exit(acma.exec_())

acma()
