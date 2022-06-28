from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QWidget, QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from create_db import create_db
import database


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.title_to_play = ""
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 799)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(55, 111, 351, 421))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.itemDoubleClicked.connect(self.to_play)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(330, 70, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.get_all)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(440, 40, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        #self.pushButton_2.clicked.connect(self.get_by_artist)

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(440, 190, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        #self.pushButton_3.clicked.connect(self.get_by_album)

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(440, 340, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        #self.pushButton_4.clicked.connect(self.get_by_genre)

        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(440, 500, 75, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        #self.pushButton_5.clicked.connect(self.get_by_year)

        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(110, 640, 75, 23))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.play)

        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(270, 640, 75, 23))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(self.pause)

        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(50, 40, 91, 23))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(self.getDirectory)

        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(540, 40, 221, 131))
        self.listWidget_2.setObjectName("listWidget_2")
        self.listWidget_2.addItems(database.get_all("artist"))
        self.listWidget_2.itemDoubleClicked.connect(self.get_by_artist)

        self.listWidget_3 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_3.setGeometry(QtCore.QRect(540, 190, 221, 131))
        self.listWidget_3.setObjectName("listWidget_3")
        self.listWidget_3.addItems(database.get_all("album"))
        self.listWidget_3.itemDoubleClicked.connect(self.get_by_album)

        self.listWidget_4 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_4.setGeometry(QtCore.QRect(540, 340, 221, 131))
        self.listWidget_4.setObjectName("listWidget_4")
        self.listWidget_4.addItems(database.get_all("genre"))
        self.listWidget_4.itemDoubleClicked.connect(self.get_by_genre)

        self.listWidget_5 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_5.setGeometry(QtCore.QRect(540, 500, 221, 131))
        self.listWidget_5.setObjectName("listWidget_5")
        self.listWidget_5.addItems(database.get_all("year"))
        self.listWidget_5.itemDoubleClicked.connect(self.get_by_year)

        self.player = QMediaPlayer()
        self.player.setVolume(10)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 600, 401, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(190, 560, 81, 16))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "All"))
        self.pushButton_2.setText(_translate("MainWindow", "Artist"))
        self.pushButton_3.setText(_translate("MainWindow", "Album"))
        self.pushButton_4.setText(_translate("MainWindow", "Genre"))
        self.pushButton_5.setText(_translate("MainWindow", "Year"))
        self.pushButton_6.setText(_translate("MainWindow", "Play"))
        self.pushButton_7.setText(_translate("MainWindow", "Stop"))
        self.pushButton_8.setText(_translate("MainWindow", "Select Folder"))
        self.label.setText(_translate("MainWindow", "SongName"))
        self.label_2.setText(_translate("MainWindow", "Now playing"))

    def getDirectory(self):
        path= QFileDialog.getExistingDirectory(
            self, caption="Select a folder"
        )
        create_db(path)
        database.to_sql()
        
    def get_all(self):
        self.listWidget.clear()
        res = database.get_all("all")
        self.listWidget.addItems(res)

    def get_by_artist(self, item):
        self.listWidget.clear()
        res = database.get_by_artist(item.text())
        self.listWidget.addItems(res)
    
    def get_by_album(self, item):
        self.listWidget.clear()
        res = database.get_by_album(item.text())
        self.listWidget.addItems(res)
    
    def get_by_genre(self, item):
        self.listWidget.clear()
        res = database.get_by_genre(item.text())
        self.listWidget.addItems(res)

    def get_by_year(self, item):
        self.listWidget.clear()
        res = database.get_by_year(item.text())
        self.listWidget.addItems(res)

    def to_play(self, item):
        text =  item.text()
        self.label.setText(text)
        splited_text = text.split(" - ")
        self.title_to_play = splited_text[1]
        print(self.title_to_play)

    def play(self):
        print(self.title_to_play)
        
        path = database.to_play(self.title_to_play)
        print(path)
        url = QUrl.fromLocalFile(path)
        content = QMediaContent(url)
        self.player.setMedia(content)
        self.player.play()
    
    def pause(self):
        self.player.pause()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
