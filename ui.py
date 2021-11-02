from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

def main():
    app = QApplication([])
    window = QWidget()
    window.setWindowTitle("Window Title")
    window.setGeometry(1000, 1000, 1000, 1000)

    label = QLabel(window)
    label.setText("Window Label")
    label.setFont(QFont("Arial", 15))
    label.move(50, 100)

    window.show()
    app.exec_()

if __name__ == '__main__':
    main()