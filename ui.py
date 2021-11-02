from PyQt5.QtWidgets import *

def main():
    app = QApplication([])
    window = QWidget()

    label = QLabel(window)
    label.setText("Window Label")

    window.show()
    app.exec_()

if __name__ == '__main__':
    main()