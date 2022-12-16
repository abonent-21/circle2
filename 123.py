import sys

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5.uic import loadUi
from random import randint
from script import Ui_Form


class Example(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.b1.clicked.connect(self.p1)
        self.do_paint = False
        self.diametr = 0

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def draw_flag(self, qp):
        qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        d = self.diametr
        qp.drawEllipse(100, 40, d, d)

    def p1(self):
        self.do_paint = True
        self.diametr = randint(10, 200)
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
