from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.Qt import *
from PyQt5.QtCore import QProcess
import pyautogui as p
import locale
import inspect
import os
import sys
import time
import subprocess
import requests

lang = locale.getdefaultlocale()[0]
print(f'lang = {lang}')  #


def get_script_dir(follow_symlinks=True):
    if getattr(sys, 'frozen', False):  # py2exe, PyInstaller, cx_Freeze
        path = os.path.abspath(sys.executable)
    else:
        path = inspect.getabsfile(get_script_dir)
    if follow_symlinks:
        path = os.path.realpath(path)
    return os.path.dirname(path)


script_dir = get_script_dir()


class Ui_tbWidget(object):
    def setupUi(self, tbWidget):
        tbWidget.setObjectName("tbWidget")
        tbWidget.resize(600, 40)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(tbWidget.sizePolicy().hasHeightForWidth())
        tbWidget.setSizePolicy(sizePolicy)
        tbWidget.setMinimumSize(QtCore.QSize(0, 40))
        tbWidget.setMaximumSize(QtCore.QSize(16777215, 40))

        self.verticalLayout = QtWidgets.QVBoxLayout(tbWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.tbWidget_2 = QtWidgets.QWidget(tbWidget)
        self.tbWidget_2.setMinimumSize(QtCore.QSize(0, 40))
        self.tbWidget_2.setMaximumSize(QtCore.QSize(16777215, 40))
        self.tbWidget_2.setStyleSheet("QWidget#tbWidget_2{\n"
                                      "    background-color: #009688;\n"
                                      "}")
        self.tbWidget_2.setObjectName("tbWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tbWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tbWidget_5 = QtWidgets.QWidget(self.tbWidget_2)
        self.tbWidget_5.setMinimumSize(QtCore.QSize(0, 40))
        self.tbWidget_5.setMaximumSize(QtCore.QSize(16777215, 40))
        self.tbWidget_5.setObjectName("tbWidget_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tbWidget_5)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tbLabel_6 = QtWidgets.QLabel('Objection.lol', self.tbWidget_5,
                                          alignment=QtCore.Qt.AlignCenter)
        self.tbLabel_6.setObjectName("tbLabel_6")
        self.tbLabel_6.setStyleSheet(
            "#tbLabel_6 {color: #FFFFFF; font-size: 22px;}")

        self.verticalLayout_3.addWidget(self.tbLabel_6)
        self.horizontalLayout_2.addWidget(self.tbWidget_5)
        self.tbWidget_3 = QtWidgets.QWidget(self.tbWidget_2)
        self.tbWidget_3.setMinimumSize(QtCore.QSize(90, 40))
        self.tbWidget_3.setMaximumSize(QtCore.QSize(90, 40))
        self.tbWidget_3.setStyleSheet("QPushButton{\n"
                                      "    background-color:rgba(0, 0, 0, 0);\n"
                                      "    color:rgb(255, 255, 255);\n"
                                      "    border-radius:1px;\n"
                                      "    font-size:18px;\n"


                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "    background-color:rgb(49, 48, 53);\n"
                                      "}\n"
                                      "QPushButton#closeButton:hover{\n"
                                      "    background-color:rgb(232, 17, 35);\n"
                                      "}\n"
                                      "QPushButton:pressed{\n"
                                      "    padding-top:5px;\n"
                                      "    padding-left:5px;\n"
                                      "}")
        self.tbWidget_3.setObjectName("tbWidget_3")
        self.gridLayout = QtWidgets.QGridLayout(self.tbWidget_3)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")

        self.closeButton = QtWidgets.QPushButton(self.tbWidget_3)

        font = QtGui.QFont()
        font.setFamily("Webdings")
        self.closeButton.setFont(font)

        self.closeButton.setMinimumSize(QtCore.QSize(30, 30))
        self.closeButton.setMaximumSize(QtCore.QSize(30, 30))
        self.closeButton.setObjectName("closeButton")
        self.gridLayout.addWidget(self.closeButton, 0, 2, 1, 1)

        self.buttonMaximum = QtWidgets.QPushButton(self.tbWidget_3)
        self.buttonMaximum.setMinimumSize(QtCore.QSize(30, 30))
        self.buttonMaximum.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Webdings")
        self.buttonMaximum.setFont(font)
        self.buttonMaximum.setObjectName("buttonMaximum")
        self.gridLayout.addWidget(self.buttonMaximum, 0, 1, 1, 1)

        # !!! +++
        self.buttonNormal = QtWidgets.QPushButton(self.tbWidget_3)  # +++
        self.buttonNormal.setMinimumSize(QtCore.QSize(30, 30))
        self.buttonNormal.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Webdings")
        self.buttonNormal.setFont(font)
        self.buttonNormal.setObjectName("buttonNormal")
        self.gridLayout.addWidget(self.buttonNormal, 0, 1, 1, 1)

        self.buttonMinimum = QtWidgets.QPushButton(self.tbWidget_3)
        self.buttonMinimum.setMinimumSize(QtCore.QSize(30, 30))
        self.buttonMinimum.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Webdings")
        self.buttonMinimum.setFont(font)
        self.buttonMinimum.setObjectName("buttonMinimum")  # buttonMinimum tbPushButton
        self.gridLayout.addWidget(self.buttonMinimum, 0, 0, 1, 1)

        self.horizontalLayout_2.addWidget(self.tbWidget_3)
        self.verticalLayout.addWidget(self.tbWidget_2)

        self.retranslateUi(tbWidget)
        QtCore.QMetaObject.connectSlotsByName(tbWidget)

    def retranslateUi(self, tbWidget):
        _translate = QtCore.QCoreApplication.translate
        tbWidget.setWindowTitle(_translate("tbWidget", "Form"))

        self.buttonMinimum.setText(_translate("tbWidget", "0"))
        self.closeButton.setText(_translate("tbWidget", "r"))
        self.buttonMaximum.setText(_translate("tbWidget", "1"))
        self.buttonNormal.setText(_translate("tbWidget", "2"))  # +++


class TitleBar(QtWidgets.QWidget, Ui_tbWidget):
    def __init__(self, parent=None):
        super(TitleBar, self).__init__(parent)

        self.setupUi(self)

        self.buttonNormal.setVisible(False)
        self.parent = parent  # +++
        self.buttonMinimum.setFocusPolicy(QtCore.Qt.NoFocus)
        self.buttonMaximum.setFocusPolicy(QtCore.Qt.NoFocus)
        self.buttonNormal.setFocusPolicy(QtCore.Qt.NoFocus)
        self.closeButton.setFocusPolicy(QtCore.Qt.NoFocus)

        self.buttonMinimum.clicked.connect(self.parent.showMinimized)
        self.buttonMaximum.clicked.connect(self.parent.showMaximized)
        self.buttonNormal.clicked.connect(self.parent.showNormal)
        self.closeButton.clicked.connect(self.parent.close)

        self.parent.installEventFilter(self)

    def eventFilter(self, target, event):
        if isinstance(event, QWindowStateChangeEvent):
            if self.parent.isVisible() and not self.parent.isMinimized():
                # Скрыть кнопку максимизации, если ток максимален
                self.buttonMaximum.setVisible(not self.parent.isMaximized())
                self.buttonNormal.setVisible(self.parent.isMaximized())
        return super(TitleBar, self).eventFilter(target, event)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setObjectName("centralwidget")
        self.setCentralWidget(self.centralwidget)
        self.resize(1400, 900)

        def _downloadRequested(item):
            p.alert(f'Download your file at {item.path()}',
                    'Request to download file', button='OK')
            item.accept()

        self.browser = QWebEngineView()
        self.browser.page().profile().downloadRequested.connect(_downloadRequested)
        self.browser.setUrl(QUrl("https://objection.lol"))
        self.browser.loadFinished.connect(self.update_title)

        # self.height = self.screenRect.height()
        # self.width = self.screenRect.width()

        # востановите
        self.setWindowFlags(  # QtCore.Qt.WindowStaysOnTopHint |
            QtCore.Qt.FramelessWindowHint)
        self.setWindowIcon(QIcon('objection.png'))
        # +++
        self.titleBar = TitleBar(self)

        layout = QtWidgets.QVBoxLayout(self.centralwidget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        layout.addWidget(self.titleBar)
        layout.addWidget(self.browser)

        self.oldPos = self.pos()

        # !!! +++
        self.langs = ['ru_RU', 'uk_UK', 'be_BE', 'kz_KZ']  # !!! +++

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        if event.pos().y() > 40:
            return

        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    # +++ vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
    def update_title(self):
        title = self.browser.page().title()
        if title == "Ace Attorney Objection Maker":
            self.setWindowTitle(title)
        elif title == "Objection!":
            self.setWindowTitle(title)
        #else:
         #   self.browser.setUrl(QUrl("https://objection.lol"))

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_F10:
            self.url_start = self.browser.history().backItem()
            print(f'self.url_start       = {self.url_start}')
            print(f'self.url_start.url() = {self.url_start.url()}')

        #    def keyPressEvent(self, event):
        #        # если нажата клавиша F11
        #        if event.key() == QtCore.Qt.Key_F11:
        # ----> vvvv
        elif event.key() == QtCore.Qt.Key_F11:
            # если в полный экран
            if self.isFullScreen():
                # вернуть прежнее состояние
                self.showNormal()
            else:
                # иначе во весь экран
                self.showFullScreen()
        # ----> vvvv
        elif event.key() == QtCore.Qt.Key_F6:
            QProcess.startDetached("letter.exe")
        #        event.accept()

        # +++
        #    def keyPressEvent(self, event):
        #        if lang == 'ru_RU' or 'uk_UK' or 'be_BE' or 'kz_KZ':
        # ----> vvvvvvvvvvvvvvvvvvvvv
        if lang in self.langs:  # !!!
            if event.key() == QtCore.Qt.Key_F2:
                self.showMinimized()
                objectionid = p.prompt("Введи айди сцены (Например: 4177334)", "Введи айди сцены.")
                if objectionid == None:
                    p.alert('Objection id is none', 'None')
                    self.showMaximized()
                else:
                    self.browser.setUrl(QUrl(f"https://objection.lol/objection/{objectionid}"))
                    self.showMaximized()
            # --------> vvvv
            elif event.key() == QtCore.Qt.Key_F3:
                self.showMinimized()
                objectionid = p.prompt("Введи айди кейса (Например: 5do5wuim)", "Введи айди кейса.")
                if objectionid == None:
                    p.alert('Введенный айди кейса не имеет никакого значения', 'Нету значения')
                    time.sleep(3)
                    self.showMaximized()
                else:
                    self.browser.setUrl(QUrl(f"https://objection.lol/case/{objectionid}"))
                    self.showMaximized()
                # --------> vvvv
            elif event.key() == QtCore.Qt.Key_F8:
                im1 = p.screenshot()
                im1.save('objectionlol_screenshot.png')
                time.sleep(2)
                os.system(f"{script_dir}\objectionlol_screenshot.png")
            elif event.key() == QtCore.Qt.Key_F7:
                self.browser.setUrl(QUrl("https://objection.lol"))
            elif event.key() == QtCore.Qt.Key_F1:
                import webbrowser
                webbrowser.open('http://objection.ga')
        else:
            if event.key() == QtCore.Qt.Key_F2:
                self.showMinimized()
                objectionid = p.prompt("Enter Objection id (Example: 4177334)", "Enter Objection id.")
                if objectionid == None:
                    p.alert('Введенный айди сцены не имеет никакого значения', 'Нету значения')
                    time.sleep(3)
                    self.showMaximized()
                else:
                    self.browser.setUrl(QUrl(f"https://objection.lol/objection/{objectionid}"))
                    self.showMaximized()
            # --------> vvvv
            elif event.key() == QtCore.Qt.Key_F3:
                self.showMinimized()
                objectionid = p.prompt("Enter Objection case id (Example: 5do5wuim)", "Enter Objection case id.")
                if objectionid == None:
                    p.alert('Objection case id is none', 'None')
                    time.sleep(3)
                    self.showMaximized()
                else:
                    self.browser.setUrl(QUrl(f"https://objection.lol/case/{objectionid}"))
                    self.showMaximized()
            # --------> vvvv
            elif event.key() == QtCore.Qt.Key_F8:
                im1 = p.screenshot()
                im1.save('objectionlol_screenshot.png')
                time.sleep(2)
                os.system(f"{script_dir}\objectionlol_screenshot.png")
            elif event.key() == QtCore.Qt.Key_F7:
                self.browser.setUrl(QUrl("https://objection.lol"))
            elif event.key() == QtCore.Qt.Key_F1:
                import webbrowser
                webbrowser.open('http://objection.ga')

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())
