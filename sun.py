# pyinstaller -w -i logo.ico sun.py

import win32api
from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSlot, Qt, QEvent
from PyQt5.QtGui import QPalette, QBrush, QPixmap
from PyQt5.QtWidgets import QApplication, QWidget
import configparser

from sun_ui import MainWindow


class sun_main_ui(MainWindow):


    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.config = configparser.ConfigParser()  # sun.ini配置文件对象
        self.config.read("sun.ini", encoding="utf-8")

        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.config.get("Settings", "WindowTitle"))
        self.setWindowIcon(QtGui.QIcon('./logo.ico'))

        # self.setWindowFlags(QtCore.Qt.CustomizeWindowHint)  # 去掉标题栏的代码(会留有上边小条可以按住移动窗口)

        # 设置窗体无边框
        if self.config.get("Settings", "UseTitleBar") == "0":
            self.setWindowFlags(Qt.FramelessWindowHint)
        # 设置背景透明
        # self.setAttribute(Qt.WA_TranslucentBackground)

        # 设置窗口背景图片
        self.palette = QPalette()
        self.bg_QPixmap = QPixmap("./interface/bg.jpg")  # 背景图片对象
        self.palette.setBrush(QPalette.Background, QBrush(self.bg_QPixmap))
        self.setPalette(self.palette)

        self.resize(self.bg_QPixmap.width(), self.bg_QPixmap.height())  # 设置主窗口大小
        self.setFixedSize(self.bg_QPixmap.width(), self.bg_QPixmap.height())  # 固定主窗口大小，不允许拉伸

        # 设置进入、退出按钮的背景图片
        self.Enter_QPixmap = QPixmap("./interface/bt_01.png")
        self.pushButton_Enter.resize(self.Enter_QPixmap.width(), self.Enter_QPixmap.height())
        self.pushButton_Enter.setStyleSheet('QPushButton{border-image:url(./interface/bt_01.png)}')
        self.pushButton_Enter.setText("")
        self.pushButton_Enter.move(int(self.config.get("Settings", "EnterButtonPositionX")), int(self.config.get("Settings", "EnterButtonPositionY")))
        self.pushButton_Enter.installEventFilter(self)  # 关联鼠标悬停事件

        self.Exit_QPixmap = QPixmap("./interface/bt_02.png")
        self.pushButton_Exit.resize(self.Exit_QPixmap.width(), self.Exit_QPixmap.height())
        self.pushButton_Exit.setStyleSheet('QPushButton{border-image:url(./interface/bt_02.png)}')
        self.pushButton_Exit.setText("")
        self.pushButton_Exit.move(int(self.config.get("Settings", "ExitButtonPositionX")), int(self.config.get("Settings", "ExitButtonPositionY")))
        self.pushButton_Exit.installEventFilter(self)  # 关联鼠标悬停事件

        # 获取按钮坐标
        self.EnterX = self.pushButton_Enter.x()
        self.EnterY = self.pushButton_Enter.y()

        self.ExitX = self.pushButton_Exit.x()
        self.ExitY = self.pushButton_Exit.y()

    # 鼠标悬停事件
    def eventFilter(self, object, event):
        if object == self.pushButton_Enter:
            if event.type() == QEvent.Enter:
                print("进入按钮悬停")
                self.pushButton_Enter.move(self.EnterX - 2, self.EnterY + 2)
            if event.type() == QEvent.Leave:
                print("移开进入按钮")
                self.pushButton_Enter.move(self.EnterX, self.EnterY)
        if object == self.pushButton_Exit:
            if event.type() == QEvent.Enter:
                print("退出按钮悬停")
                self.pushButton_Exit.move(self.ExitX - 2, self.ExitY + 2)
            if event.type() == QEvent.Leave:
                print("移开进入按钮")
                self.pushButton_Exit.move(self.ExitX, self.ExitY)
        return QWidget.eventFilter(self, object, event)

    # 按Esc退出程序
    def keyPressEvent(self, QKeyEvent):
        super().keyPressEvent(QKeyEvent)
        if (QKeyEvent.key() == Qt.Key_Escape):
            if self.config.get("Settings", "KeyEsc") == "1":
                print('按下ESC')
                self.close()

    @pyqtSlot()
    def on_pushButton_Enter_clicked(self):
        print("Enter")
        # win32api.ShellExecute(0, 'open', '../ck2d/gbase3d.exe', '', '', 1)
        win32api.ShellExecute(0, 'open', r'..\ck2d\gbase3d.exe', '', '', 1)
        if self.config.get("Settings", "EscapeOk") == "1":
            self.close()  # 运行gbase3d.exe后关闭启动界面

    @pyqtSlot()
    def on_pushButton_Exit_clicked(self):
        # self.pushButton_Enter.move(50, 50)
        print("Exit")
        self.close()



if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    QApplication.setQuitOnLastWindowClosed(True)
    w = sun_main_ui()
    w.show()
    sys.exit(app.exec())
