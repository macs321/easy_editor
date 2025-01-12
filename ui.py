# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(804, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setStyleSheet("border: 1px solid black;\n"
"border-radius:5px;")
        self.centralwidget.setObjectName("centralwidget")
        self.image_lb = QtWidgets.QLabel(parent=self.centralwidget)
        self.image_lb.setGeometry(QtCore.QRect(170, 20, 621, 501))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Light")
        font.setPointSize(33)
        self.image_lb.setFont(font)
        self.image_lb.setStyleSheet("background-color: lightgray;")
        self.image_lb.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.image_lb.setObjectName("image_lb")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 520, 781, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.left_btn = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.left_btn.setStyleSheet("background-color: lightgray;\n"
"padding:5px")
        self.left_btn.setObjectName("left_btn")
        self.horizontalLayout.addWidget(self.left_btn)
        self.right_btn = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.right_btn.setStyleSheet("background-color: lightgray;\n"
"padding:5px")
        self.right_btn.setObjectName("right_btn")
        self.horizontalLayout.addWidget(self.right_btn)
        self.mirror_btn = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.mirror_btn.setStyleSheet("background-color: lightgray;\n"
"padding:5px")
        self.mirror_btn.setObjectName("mirror_btn")
        self.horizontalLayout.addWidget(self.mirror_btn)
        self.sharp_btn = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.sharp_btn.setStyleSheet("background-color: lightgray;\n"
"padding:5px")
        self.sharp_btn.setObjectName("sharp_btn")
        self.horizontalLayout.addWidget(self.sharp_btn)
        self.bw_btn = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.bw_btn.setStyleSheet("background-color: lightgray;\n"
"padding:5px")
        self.bw_btn.setObjectName("bw_btn")
        self.horizontalLayout.addWidget(self.bw_btn)
        self.files_list = QtWidgets.QListWidget(parent=self.centralwidget)
        self.files_list.setGeometry(QtCore.QRect(10, 40, 151, 481))
        self.files_list.setStyleSheet("background-color:lightblue;")
        self.files_list.setObjectName("files_list")
        self.choose_dir_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.choose_dir_btn.setGeometry(QtCore.QRect(10, 12, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.choose_dir_btn.setFont(font)
        self.choose_dir_btn.setStyleSheet("background: gray")
        self.choose_dir_btn.setObjectName("choose_dir_btn")
        self.timeEdit = QtWidgets.QTimeEdit(parent=self.centralwidget)
        self.timeEdit.setGeometry(QtCore.QRect(650, 50, 118, 22))
        self.timeEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2025, 1, 13), QtCore.QTime(13, 16, 0)))
        self.timeEdit.setObjectName("timeEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 804, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.image_lb.setText(_translate("MainWindow", "картинка"))
        self.left_btn.setText(_translate("MainWindow", "Вліво"))
        self.right_btn.setText(_translate("MainWindow", "Вправо"))
        self.mirror_btn.setText(_translate("MainWindow", "відзеркалити"))
        self.sharp_btn.setText(_translate("MainWindow", "Різкість"))
        self.bw_btn.setText(_translate("MainWindow", "Ч/Б"))
        self.choose_dir_btn.setText(_translate("MainWindow", "Папка"))
