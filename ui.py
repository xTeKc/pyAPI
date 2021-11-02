from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

def main():
    app = QApplication([])
    window = QWidget()
    window.setWindowTitle("Window Title")
    window.setGeometry(1000, 1000, 1000, 1000)

    # label = QLabel(window)
    # label.setText("Window Label")
    # label.setFont(QFont("Arial", 15))
    # label.move(100, 50)

    layout = QVBoxLayout()

    label = QLabel("Push Button")

    textbox = QTextEdit()
    
    button = QPushButton("PUSH")
    button.clicked.connect(on_click)

    layout.addWidget(label)
    layout.addWidget(textbox)
    layout.addWidget(button)
    
    window.setLayout(layout)

    window.show()
    app.exec_()

def on_click(msg):
    # print("Hello")
    message = QMessageBox()
    message.setText(msg)
    message.exec_()

if __name__ == '__main__':
    main()