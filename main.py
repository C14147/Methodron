import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui_methodron import Ui_Methodron
from qt_material import apply_stylesheet


class MethodronMainWindow(QMainWindow, Ui_Methodron):
    def __init__(self, parent=None):
        super(MethodronMainWindow, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    methodronWindow = MethodronMainWindow()

    apply_stylesheet(app, theme='dark_blue.xml')
    
    methodronWindow.show()
    
    sys.exit(app.exec_())
