# -*- UTF-8 -*-
# @author 关宅宅

from PyQt5.QtWidgets import QWidget,QApplication,QLabel,QPushButton,QMessageBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QEvent,QRect, QPropertyAnimation, QEasingCurve, QPoint
import random
import sys

# 布局函数
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        # 标签布局
        self.lb = QLabel('愿意做我女朋友么？', self)
        self.lb.setFont(QFont("Timers", 20))
        self.lb.setStyleSheet("color:red;font-weight:bold")
        self.lb.move(120,100)

        # 按钮1布局（“同意”按钮）
        self.btn1 = QPushButton('同意',self)
        self.btn1.setFont(QFont("Timers", 15))
        self.btn1.setStyleSheet("color:red;font-weight:bold")
        self.btn1.move(200, 200)
        self.btn1.clicked.connect(self.right)

        # 按钮2布局（“不同意”按钮）
        self.btn2 = QPushButton('不同意', self)
        self.btn2.setFont(QFont("Timers", 10))
        self.btn2.setStyleSheet("color:green;font-weight:bold")
        self.btn2.move(200, 300)
        self.btn2.clicked.connect(self.false)

        # 按钮2定义鼠标事件
        self.btn2.setMouseTracking(True)
        self.btn2.installEventFilter(self)

        # 窗体布局
        self.setWindowTitle("嘿嘿")
        self.resize(500, 500)
        self.show()

    # 关闭窗口时触发事件
    def closeEvent(self, event):
            # 弹出对话框
            reply = QMessageBox.question(self,'想跑？',"确定退出么？",QMessageBox.Yes|QMessageBox.No,QMessageBox.No)

            # 对返回的选项进行操作
            if reply == QMessageBox.Yes:
                QMessageBox.warning(self, "搞笑", "你跑的了么 (≖ ‿ ≖)✧")
            else:
                QMessageBox.warning(self, "明智", "哎呦，不错哦 (≖ ‿ ≖)✧")
            event.ignore()

    # 点击按钮“同意时”触发的事件
    def right(self):
        QMessageBox.information(self,'对了嘛',"早这么爽快不就好了么 (≖ ‿ ≖)✧")
        sys.exit()

    # 点击按钮“不同意”时触发的事件
    def false(self):
        QMessageBox.information(self, '可以嘛', "手速不错，我喜欢！不过你还是跑不了 (≖ ‿ ≖)✧")

    # 定义鼠标指向按钮2的事件
    def eventFilter(self, object, event):
        if object == self.btn2:
            if event.type() == QEvent.Enter:
                self.doMove()
        return QWidget.eventFilter(self, object, event)

    # 当鼠标移动到按钮2控件时的事件（动画）
    def doMove(self):
        global x ,y
        if self.btn2.pos() == QPoint(200, 300):
            self.anim = QPropertyAnimation(self.btn2, b"geometry")
            self.anim.setDuration(200)
            self.anim.setStartValue(QRect(200, 300, 70, 20))
            x = random.randint(40, 460)
            y = random.randint(30, 480)
            self.anim.setEndValue(QRect(x, y, 50, 20))
            self.anim.setEasingCurve(QEasingCurve.OutCubic)
            self.anim.start()
        elif self.btn2.pos() == QPoint(x, y):
            self.anim = QPropertyAnimation(self.btn2, b"geometry")
            self.anim.setDuration(200)
            self.anim.setStartValue(QRect(x, y, 50, 20))
            x = random.randint(40, 460)
            y = random.randint(30, 480)
            self.anim.setEndValue(QRect(x, y, 50, 20))
            self.anim.setEasingCurve(QEasingCurve.OutCubic)
            self.anim.start()
# 主函数
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())