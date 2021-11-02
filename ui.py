from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

def main():
    app = QApplication([])
    window = QWidget()

    label = QLabel(window)
    label.setText("Window Label")
    label.setFont()

    window.show()
    app.exec_()

if __name__ == '__main__':
    main()