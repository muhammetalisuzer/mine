from PyQt5 import QtWidgets
import sys
from hesapp import  Ui_MainWindow

class hesap_makinasi(QtWidgets.QMainWindow):
    def __init__(self):
        super(hesap_makinasi, self).__init__()      

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.toplama_btn.clicked.connect(self.toplama)   
        self.ui.cikarma.clicked.connect(self.cikarma)
        self.ui.sifirla.clicked.connect(self.sifirlama)

    def sifirlama(self):
        self.ui.sayi_1.clear()
        self.ui.sayi_2.clear()
        
    
    def cikarma(self):
        sonuc2 = int(self.ui.sayi_1.text()) - int(self.ui.sayi_2.text())    
        self.ui.sonuc.setText('sonuc'+ str(sonuc2))
    def toplama(self):
        sonuc1= int(self.ui.sayi_1.text()) + int(self.ui.sayi_2.text())
        self.ui.sonuc.setText('sonuc'+ str(sonuc1))

def uygulama():
    uygulama = QtWidgets.QApplication(sys.argv)
    ekran = hesap_makinasi()
    ekran.show()
    sys.exit(uygulama.exec_())

uygulama()