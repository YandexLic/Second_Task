import sys
import random
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnPaint = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnPaint.sizePolicy().hasHeightForWidth())
        self.btnPaint.setSizePolicy(sizePolicy)
        self.btnPaint.setObjectName("btnPaint")
        self.verticalLayout.addWidget(self.btnPaint)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.horizontalLayout.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Yellow окружности"))
        self.btnPaint.setText(_translate("MainWindow", "Click сюда"))


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.circles = []
        self.setupUi(self)

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.widget.paintEvent = self.paintEventDeco
        self.btnPaint.clicked.connect(self.gen_circles)

    def paintEventDeco(self, d_matter: QtGui.QPaintEvent) -> None:
        painter = QtGui.QPainter()
        painter.begin(self.widget)
        self.draw_circles(painter)
        painter.end()

    def draw_circles(self, painter):
        painter.translate(self.widget.pos())
        for center, r, collor in self.circles:
            painter.setBrush(QtGui.QColor(233, 237, 0))
            painter.drawEllipse(QtCore.QPoint(*center), r, r)

    def gen_circles(self):
        circles = [((random.randint(0, self.widget.width()),
                     random.randint(0, self.widget.height())),
                    random.randint(10, self.widget.width() // 2),
                    [random.randint(0, 255) for _ in range(3)])
                   for _ in range(random.randint(3, 20))]
        self.circles = circles
        self.update()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()