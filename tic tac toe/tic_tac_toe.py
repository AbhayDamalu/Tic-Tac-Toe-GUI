# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tictactoe.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(797, 603)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 801, 571))
        self.label.setAcceptDrops(True)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("IMG-20160311-WA0018.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.b01 = QtWidgets.QPushButton(self.centralwidget)
        self.b01.setGeometry(QtCore.QRect(180, 110, 150, 150))
        self.b01.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b01.setAcceptDrops(True)
        self.b01.setAutoFillBackground(False)
        self.b01.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("IMG-20160311-WA0018.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.b01.setIcon(icon)
        self.b01.setIconSize(QtCore.QSize(250, 200))
        self.b01.setCheckable(False)
        self.b01.setAutoDefault(True)
        self.b01.setDefault(False)
        self.b01.setObjectName("b01")
        self.Heading = QtWidgets.QLabel(self.centralwidget)
        self.Heading.setGeometry(QtCore.QRect(140, 20, 471, 71))
        font = QtGui.QFont()
        font.setFamily("Andalus")
        font.setPointSize(48)
        self.Heading.setFont(font)
        self.Heading.setAutoFillBackground(False)
        self.Heading.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Heading.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Heading.setLineWidth(0)
        self.Heading.setMidLineWidth(0)
        self.Heading.setScaledContents(True)
        self.Heading.setObjectName("Heading")
        self.b22 = QtWidgets.QPushButton(self.centralwidget)
        self.b22.setGeometry(QtCore.QRect(330, 410, 150, 150))
        self.b22.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b22.setAcceptDrops(True)
        self.b22.setAutoFillBackground(False)
        self.b22.setText("")
        self.b22.setIcon(icon)
        self.b22.setIconSize(QtCore.QSize(250, 200))
        self.b22.setCheckable(False)
        self.b22.setAutoDefault(True)
        self.b22.setDefault(False)
        self.b22.setObjectName("b22")
        self.b21 = QtWidgets.QPushButton(self.centralwidget)
        self.b21.setGeometry(QtCore.QRect(180, 410, 150, 150))
        self.b21.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b21.setAcceptDrops(True)
        self.b21.setAutoFillBackground(False)
        self.b21.setText("")
        self.b21.setIcon(icon)
        self.b21.setIconSize(QtCore.QSize(250, 200))
        self.b21.setCheckable(False)
        self.b21.setAutoDefault(True)
        self.b21.setDefault(False)
        self.b21.setObjectName("b21")
        self.b12 = QtWidgets.QPushButton(self.centralwidget)
        self.b12.setGeometry(QtCore.QRect(330, 260, 150, 150))
        self.b12.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b12.setAcceptDrops(True)
        self.b12.setAutoFillBackground(False)
        self.b12.setText("")
        self.b12.setIcon(icon)
        self.b12.setIconSize(QtCore.QSize(250, 200))
        self.b12.setCheckable(False)
        self.b12.setAutoDefault(True)
        self.b12.setDefault(False)
        self.b12.setObjectName("b12")
        self.b02 = QtWidgets.QPushButton(self.centralwidget)
        self.b02.setGeometry(QtCore.QRect(330, 110, 150, 150))
        self.b02.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b02.setAcceptDrops(True)
        self.b02.setAutoFillBackground(False)
        self.b02.setText("")
        self.b02.setIcon(icon)
        self.b02.setIconSize(QtCore.QSize(250, 200))
        self.b02.setCheckable(False)
        self.b02.setAutoDefault(True)
        self.b02.setDefault(False)
        self.b02.setObjectName("b02")
        self.b11 = QtWidgets.QPushButton(self.centralwidget)
        self.b11.setGeometry(QtCore.QRect(180, 260, 150, 150))
        self.b11.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b11.setAcceptDrops(True)
        self.b11.setAutoFillBackground(False)
        self.b11.setText("")
        self.b11.setIcon(icon)
        self.b11.setIconSize(QtCore.QSize(250, 200))
        self.b11.setCheckable(False)
        self.b11.setAutoDefault(True)
        self.b11.setDefault(False)
        self.b11.setObjectName("b11")
        self.b20 = QtWidgets.QPushButton(self.centralwidget)
        self.b20.setGeometry(QtCore.QRect(30, 410, 150, 150))
        self.b20.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b20.setAcceptDrops(True)
        self.b20.setAutoFillBackground(False)
        self.b20.setText("")
        self.b20.setIcon(icon)
        self.b20.setIconSize(QtCore.QSize(250, 200))
        self.b20.setCheckable(False)
        self.b20.setAutoDefault(True)
        self.b20.setDefault(False)
        self.b20.setObjectName("b20")
        self.b10 = QtWidgets.QPushButton(self.centralwidget)
        self.b10.setGeometry(QtCore.QRect(30, 260, 150, 150))
        self.b10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b10.setAcceptDrops(True)
        self.b10.setAutoFillBackground(False)
        self.b10.setText("")
        self.b10.setIcon(icon)
        self.b10.setIconSize(QtCore.QSize(250, 200))
        self.b10.setCheckable(False)
        self.b10.setAutoDefault(True)
        self.b10.setDefault(False)
        self.b10.setObjectName("b10")
        self.b00 = QtWidgets.QPushButton(self.centralwidget)
        self.b00.setGeometry(QtCore.QRect(30, 110, 150, 150))
        self.b00.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b00.setAcceptDrops(True)
        self.b00.setAutoFillBackground(False)
        self.b00.setText("")
        self.b00.setIcon(icon)
        self.b00.setIconSize(QtCore.QSize(250, 200))
        self.b00.setCheckable(False)
        self.b00.setAutoDefault(True)
        self.b00.setDefault(False)
        self.b00.setObjectName("b00")
        
        self.reset = QtWidgets.QPushButton(self.centralwidget)
        self.reset.setGeometry(QtCore.QRect(640, 230, 125, 31))
        self.interchange = QtWidgets.QPushButton(self.centralwidget)
        self.interchange.setGeometry(QtCore.QRect(500, 230, 125, 31))
        
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.reset.setFont(font)
        self.reset.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.reset.setAutoDefault(True)
        self.reset.setObjectName("reset")
        self.interchange.setFont(font)
        self.interchange.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.interchange.setAutoDefault(True)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(640, 130, 113, 20))
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(640, 170, 113, 20))
        self.lineEdit_2.setClearButtonEnabled(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.Player_1 = QtWidgets.QLabel(self.centralwidget)
        self.Player_1.setGeometry(QtCore.QRect(530, 120, 91, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.Player_1.setFont(font)
        self.Player_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Player_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Player_1.setScaledContents(True)
        self.Player_1.setObjectName("Player_1")
        self.Player_2 = QtWidgets.QLabel(self.centralwidget)
        self.Player_2.setGeometry(QtCore.QRect(530, 160, 91, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.Player_2.setFont(font)
        self.Player_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Player_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Player_2.setScaledContents(True)
        self.Player_2.setObjectName("Player_2")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(320, 260, 20, 151))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(320, 110, 20, 151))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(320, 410, 20, 151))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(170, 110, 20, 151))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(170, 260, 20, 151))
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(170, 410, 20, 151))
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setGeometry(QtCore.QRect(20, 110, 20, 151))
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.line_9 = QtWidgets.QFrame(self.centralwidget)
        self.line_9.setGeometry(QtCore.QRect(20, 260, 20, 151))
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.line_10 = QtWidgets.QFrame(self.centralwidget)
        self.line_10.setGeometry(QtCore.QRect(20, 410, 20, 151))
        self.line_10.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.line_11 = QtWidgets.QFrame(self.centralwidget)
        self.line_11.setGeometry(QtCore.QRect(470, 110, 20, 151))
        self.line_11.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.line_12 = QtWidgets.QFrame(self.centralwidget)
        self.line_12.setGeometry(QtCore.QRect(470, 260, 20, 151))
        self.line_12.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.line_13 = QtWidgets.QFrame(self.centralwidget)
        self.line_13.setGeometry(QtCore.QRect(470, 410, 20, 151))
        self.line_13.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.line_14 = QtWidgets.QFrame(self.centralwidget)
        self.line_14.setGeometry(QtCore.QRect(30, 100, 151, 16))
        self.line_14.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_14.setObjectName("line_14")
        self.line_15 = QtWidgets.QFrame(self.centralwidget)
        self.line_15.setGeometry(QtCore.QRect(180, 100, 151, 16))
        self.line_15.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_15.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_15.setObjectName("line_15")
        self.line_16 = QtWidgets.QFrame(self.centralwidget)
        self.line_16.setGeometry(QtCore.QRect(330, 100, 151, 16))
        self.line_16.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_16.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_16.setObjectName("line_16")
        self.line_17 = QtWidgets.QFrame(self.centralwidget)
        self.line_17.setGeometry(QtCore.QRect(30, 250, 151, 16))
        self.line_17.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_17.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_17.setObjectName("line_17")
        self.line_18 = QtWidgets.QFrame(self.centralwidget)
        self.line_18.setGeometry(QtCore.QRect(30, 400, 151, 16))
        self.line_18.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_18.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_18.setObjectName("line_18")
        self.line_19 = QtWidgets.QFrame(self.centralwidget)
        self.line_19.setGeometry(QtCore.QRect(180, 250, 151, 16))
        self.line_19.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_19.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_19.setObjectName("line_19")
        self.line_20 = QtWidgets.QFrame(self.centralwidget)
        self.line_20.setGeometry(QtCore.QRect(180, 400, 151, 16))
        self.line_20.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_20.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_20.setObjectName("line_20")
        self.line_21 = QtWidgets.QFrame(self.centralwidget)
        self.line_21.setGeometry(QtCore.QRect(330, 400, 151, 16))
        self.line_21.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_21.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_21.setObjectName("line_21")
        self.line_22 = QtWidgets.QFrame(self.centralwidget)
        self.line_22.setGeometry(QtCore.QRect(330, 250, 151, 16))
        self.line_22.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_22.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_22.setObjectName("line_22")
        self.line_23 = QtWidgets.QFrame(self.centralwidget)
        self.line_23.setGeometry(QtCore.QRect(30, 550, 151, 16))
        self.line_23.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_23.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_23.setObjectName("line_23")
        self.line_24 = QtWidgets.QFrame(self.centralwidget)
        self.line_24.setGeometry(QtCore.QRect(180, 550, 151, 16))
        self.line_24.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_24.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_24.setObjectName("line_24")
        self.line_25 = QtWidgets.QFrame(self.centralwidget)
        self.line_25.setGeometry(QtCore.QRect(330, 550, 151, 16))
        self.line_25.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_25.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_25.setObjectName("line_25")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(500, 120, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setFrameShape(QtWidgets.QFrame.Box)
        self.label_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(500, 160, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setFrameShape(QtWidgets.QFrame.Box)
        self.label_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_5.setObjectName("label_5")
        self.poster = QtWidgets.QLabel(self.centralwidget)
        self.poster.setGeometry(QtCore.QRect(680, 10, 101, 81))
        self.poster.setFrameShape(QtWidgets.QFrame.Box)
        self.poster.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.poster.setText("")
        self.poster.setPixmap(QtGui.QPixmap("images (1).jpg"))
        self.poster.setScaledContents(True)
        self.poster.setObjectName("poster")
        self.dial = QtWidgets.QDial(self.centralwidget)
        self.dial.setGeometry(QtCore.QRect(-10, 20, 161, 64))
        self.dial.setObjectName("dial")
        self.display = QtWidgets.QLabel(self.centralwidget)
        self.display.setGeometry(QtCore.QRect(510, 290, 251, 251))
        self.display.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.display.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.display.setText("")
        self.display.setPixmap(QtGui.QPixmap("unnamed.png"))
        self.display.setScaledContents(True)
        self.display.setAutoFillBackground(True)
        self.display.setObjectName("display")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 797, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(72)
        
        self.l00 = QtWidgets.QLabel(self.centralwidget)
        self.l01 = QtWidgets.QLabel(self.centralwidget)
        self.l02 = QtWidgets.QLabel(self.centralwidget)
        self.l10 = QtWidgets.QLabel(self.centralwidget)
        self.l11 = QtWidgets.QLabel(self.centralwidget)
        self.l12 = QtWidgets.QLabel(self.centralwidget)
        self.l20 = QtWidgets.QLabel(self.centralwidget)
        self.l21 = QtWidgets.QLabel(self.centralwidget)
        self.l22 = QtWidgets.QLabel(self.centralwidget)

        self.l00.setScaledContents(True)
        self.l01.setScaledContents(True)
        self.l02.setScaledContents(True)
        self.l10.setScaledContents(True)
        self.l11.setScaledContents(True)
        self.l12.setScaledContents(True)
        self.l20.setScaledContents(True)
        self.l21.setScaledContents(True)
        self.l22.setScaledContents(True)

        self.b00.clicked.connect(lambda: self.b00_clicked(font))
        self.b01.clicked.connect(lambda: self.b01_clicked(font))
        self.b02.clicked.connect(lambda: self.b02_clicked(font))
        self.b10.clicked.connect(lambda: self.b10_clicked(font))
        self.b11.clicked.connect(lambda: self.b11_clicked(font))
        self.b12.clicked.connect(lambda: self.b12_clicked(font))
        self.b20.clicked.connect(lambda: self.b20_clicked(font))
        self.b21.clicked.connect(lambda: self.b21_clicked(font))
        self.b22.clicked.connect(lambda: self.b22_clicked(font))
        self.reset.clicked.connect(self.resett)
        self.interchange.clicked.connect(self.inter_change)

        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Heading.setText(_translate("MainWindow", "TIC   TAC   TOE"))
        self.reset.setText(_translate("MainWindow", "Reset"))
        self.interchange.setText(_translate("MainWindow", "Interchange"))
        self.Player_1.setText(_translate("MainWindow", "Player 1"))
        self.Player_2.setText(_translate("MainWindow", "Player 2"))
        self.label_4.setText(_translate("MainWindow", "X"))
        self.label_5.setText(_translate("MainWindow", "O"))

    def b00_clicked(self,font):
        global value
        self.l00.setGeometry(QtCore.QRect(40, 110, 131, 141))
        self.l00.setFont(font)
        self.l00.setText(text)
        value[0][0]=text
        self.text_change()

        
    def b01_clicked(self,font):
        global value
        self.l01.setGeometry(QtCore.QRect(190, 110, 131, 141))
        self.l01.setFont(font)
        self.l01.setText(text)
        value[0][1]=text
        self.text_change()

        
    def b02_clicked(self,font):
        global value
        self.l02.setGeometry(QtCore.QRect(340, 110, 131, 141))
        self.l02.setFont(font)
        self.l02.setText(text)
        value[0][2]=text
        self.text_change()

        
    def b10_clicked(self,font):
        global value
        self.l10.setGeometry(QtCore.QRect(40, 260, 131, 141))
        self.l10.setFont(font)
        self.l10.setText(text)
        value[1][0]=text
        self.text_change()
        
        
    def b11_clicked(self,font):
        global value
        self.l11.setGeometry(QtCore.QRect(190, 260, 131, 141))
        self.l11.setFont(font)
        self.l11.setText(text)
        value[1][1]=text
        self.text_change()

        
    def b12_clicked(self,font):
        global value
        self.l12.setGeometry(QtCore.QRect(340, 260, 131, 141))
        self.l12.setFont(font)
        self.l12.setText(text)
        value[1][2]=text
        self.text_change()

        
    def b20_clicked(self,font):
        global value
        self.l20.setGeometry(QtCore.QRect(40, 420, 131, 141))
        self.l20.setFont(font)
        self.l20.setText(text)
        value[2][0]=text
        self.text_change()

        
    def b21_clicked(self,font):
        global value
        self.l21.setGeometry(QtCore.QRect(190, 420, 131, 141))
        self.l21.setFont(font)
        self.l21.setText(text)
        value[2][1]=text
        self.text_change()

        
    def b22_clicked(self,font):
        global value
        self.l22.setGeometry(QtCore.QRect(340, 420, 131, 141))
        self.l22.setFont(font)
        self.l22.setText(text)
        value[2][2]=text
        self.text_change()
        
            
    def text_change(self):
        global count
        global text
        global value
        count+=1
        if count==9:
            self.display_result()
            text=""
        else:      
            if (value[0][0]==value[1][1]==value[2][2]==" X") or (value[0][2]==value[1][1]==value[2][0]==" X") or (value[0][0]==value[0][1]==value[0][2]==" X") or (value[1][0]==value[1][1]==value[1][2]==" X") or (value[2][0]==value[2][1]==value[2][2]==" X") or (value[0][0]==value[1][0]==value[2][0]==" X") or (value[0][1]==value[1][1]==value[2][1]==" X") or (value[0][2]==value[1][2]==value[2][2]==" X"):
                self.display_result()
                text=""
            elif (value[0][0]==value[1][1]==value[2][2]==" O") or (value[0][2]==value[1][1]==value[2][0]==" O") or (value[0][0]==value[0][1]==value[0][2]==" O") or (value[1][0]==value[1][1]==value[1][2]==" O") or (value[2][0]==value[2][1]==value[2][2]==" O") or (value[0][0]==value[1][0]==value[2][0]==" O") or (value[0][1]==value[1][1]==value[2][1]==" O") or (value[0][2]==value[1][2]==value[2][2]==" O"):
                self.display_result()
                text=""
            else:
                if text==" X":
                    text=" O"
                else:
                    text=" X"


    def resett(self):
        global text
        global value
        global count
        value=[[None,None,None],[None,None,None],[None,None,None]]
        count=0
        text=" X"
        self.l00.setGeometry(QtCore.QRect(0,0,0,0))
        self.l01.setGeometry(QtCore.QRect(0,0,0,0))
        self.l02.setGeometry(QtCore.QRect(0,0,0,0))
        self.l10.setGeometry(QtCore.QRect(0,0,0,0))
        self.l11.setGeometry(QtCore.QRect(0,0,0,0))
        self.l12.setGeometry(QtCore.QRect(0,0,0,0))
        self.l20.setGeometry(QtCore.QRect(0,0,0,0))
        self.l21.setGeometry(QtCore.QRect(0,0,0,0))
        self.l22.setGeometry(QtCore.QRect(0,0,0,0))
        self.display.setPixmap(QtGui.QPixmap("unnamed.png"))

    def inter_change(self):
        self.resett()
        player1=self.lineEdit.text()
        player2=self.lineEdit_2.text()
        self.lineEdit.setText(player2)
        self.lineEdit_2.setText(player1)

    def display_result(self):
        global count
        font = QtGui.QFont()
        font.setFamily("Andalus")
        font.setPointSize(48)
        font.setBold(True)
        self.display.setFont(font)
        player1=self.lineEdit.text()
        player2=self.lineEdit_2.text()
        if count==9:
            self.display.setText("DRAW")
        else:
            if text==" X":
                if player1!="":
                    self.display.setText(f"Winner:\n{player1}")
                else:
                    self.display.setText("Winner:\nplayer1")
            elif text==" O":
                if player2!="":
                    self.display.setText(f"Winner:\n{player2}")
                else:
                    self.display.setText("Winner:\nplayer2")
            else:
                count-=1
                

if __name__ == "__main__":
    import sys
    value=[[None,None,None],[None,None,None],[None,None,None]]
    count=0
    text=" X"
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
