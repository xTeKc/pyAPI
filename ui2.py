# # -*- coding: utf-8 -*-


# from PySide2.QtCore import *
# from PySide2.QtGui import *
# from PySide2.QtWidgets import *


# class Ui_MainWindow(object):
#     def setupUi(self, MainWindow):
#         if not MainWindow.objectName():
#             MainWindow.setObjectName(u"MainWindow")
#         MainWindow.resize(640, 480)
#         self.centralwidget = QWidget(MainWindow)
#         self.centralwidget.setObjectName(u"centralwidget")
#         self.commandLinkButton = QCommandLinkButton(self.centralwidget)
#         self.commandLinkButton.setObjectName(u"commandLinkButton")
#         self.commandLinkButton.setGeometry(QRect(460, 70, 171, 41))
#         self.pushButton = QPushButton(self.centralwidget)
#         self.pushButton.setObjectName(u"pushButton")
#         self.pushButton.setGeometry(QRect(540, 130, 88, 34))
#         self.listWidget = QListWidget(self.centralwidget)
#         self.listWidget.setObjectName(u"listWidget")
#         self.listWidget.setGeometry(QRect(10, 130, 511, 301))
#         MainWindow.setCentralWidget(self.centralwidget)
#         self.menubar = QMenuBar(MainWindow)
#         self.menubar.setObjectName(u"menubar")
#         self.menubar.setGeometry(QRect(0, 0, 640, 30))
#         self.menuFile = QMenu(self.menubar)
#         self.menuFile.setObjectName(u"menuFile")
#         MainWindow.setMenuBar(self.menubar)
#         self.statusbar = QStatusBar(MainWindow)
#         self.statusbar.setObjectName(u"statusbar")
#         MainWindow.setStatusBar(self.statusbar)

#         self.menubar.addAction(self.menuFile.menuAction())

#         self.retranslateUi(MainWindow)

#         QMetaObject.connectSlotsByName(MainWindow)
#     # setupUi

#     def retranslateUi(self, MainWindow):
#         MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#         self.commandLinkButton.setText(QCoreApplication.translate("MainWindow", u"Run", None))
#         self.pushButton.setText(QCoreApplication.translate("MainWindow", u"STOP", None))
#         self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
#     # retranslateUi

