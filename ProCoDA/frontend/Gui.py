import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "ProCoDa App"
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500
        self.InitUI()

    def InitUI(self):
        self.setWindowTitle(self.title)
        #self.setGeometry(self.top, self.left, self.width, self.height)

        layout_top = QHBoxLayout()
        dv_button = QPushButton('Data Visualization', self)
        dv_button.clicked.connect(self.dv_button_onClick)
        layout_top.addWidget(dv_button)
        self.lineEdit1 = QLineEdit(
            "Type here what you want to transfer for [Window1].", self)
        self.lineEdit1.setGeometry(250, 100, 400, 30)


        da_button = QPushButton('Data Acquisition', self)
        da_button.clicked.connect(self.da_button_onClick)
        layout_top.addWidget(da_button)

        self.lineEdit2 = QLineEdit(
            "Type here what you want to transfer for [Window2].", self)
        self.lineEdit2.setGeometry(250, 200, 400, 30)

        ps_button = QPushButton('Parametric Studies', self)
        ps_button.clicked.connect(self.ps_button_onClick)
        layout_top.addWidget(ps_button)

        self.lineEdit3 = QLineEdit(
            "Type here what you want to transfer for [Window3].", self)
        self.lineEdit3.setGeometry(250, 200, 400, 30)

        layout_bottom = QHBoxLayout()
        label1 = QLabel('Read Data')
        label2 = QLabel('Read Data')
        widget1 = QComboBox()
        widget1.addItems(['Analog Channel', 'Digital Channel', 'Counter Channel'])
        widget2 = QComboBox()
        widget2.addItems(['Analog Channel', 'Digital Channel', 'Counter Channel'])
        spinbox1 = QSpinBox()
        spinbox2 = QSpinBox()
        layout_bottom.addWidget(label1)
        layout_bottom.addWidget(widget1)
        layout_bottom.addWidget(spinbox1)
        layout_bottom.addWidget(label2)
        layout_bottom.addWidget(widget2)
        layout_bottom.addWidget(spinbox2)

        layout = QVBoxLayout()
        layout.addLayout(layout_top)
        layout.addStretch()
        layout.addLayout(layout_bottom)
        layout.addStretch()
        layout.addStretch()

        wid = QWidget(self)
        self.setCentralWidget(wid)
        wid.setLayout(layout)
        self.show()

    @pyqtSlot()
    def dv_button_onClick(self):
        self.statusBar().showMessage("Switched to Data Visualization")
        self.cams = DataVisualization(self.lineEdit1.text())
        self.cams.show()
        self.close()

    @pyqtSlot()
    def da_button_onClick(self):
        self.statusBar().showMessage("Switched to Data Acquisition")
        self.cams = Window2(self.lineEdit1.text())
        self.cams.show()
        self.close()

    @pyqtSlot()
    def ps_button_onClick(self):
        self.statusBar().showMessage("Switched to Parametric Studies")
        self.cams = Window2(self.lineEdit1.text())
        self.cams.show()
        self.close()




class DataVisualization(QDialog):
    def __init__(self, value, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Data Visualization')
        self.setWindowIcon(self.style().standardIcon(
            QStyle.SP_FileDialogInfoView))

        label1 = QLabel(value)
        self.button = QPushButton()
        self.button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.button.setIcon(self.style().standardIcon(QStyle.SP_ArrowLeft))
        self.button.setIconSize(QSize(200, 200))

        layoutV = QVBoxLayout()
        self.pushButton = QPushButton(self)
        self.pushButton.setStyleSheet(
            'background-color: rgb(0,0,255); color: #fff')
        self.pushButton.setText('Click me!')
        self.pushButton.clicked.connect(self.goMainWindow)
        layoutV.addWidget(self.pushButton)

        layoutH = QHBoxLayout()
        layoutH.addWidget(label1)
        layoutH.addWidget(self.button)
        layoutV.addLayout(layoutH)
        self.setLayout(layoutV)

    def goMainWindow(self):
        self.cams = Window()
        self.cams.show()
        self.close()


class Window2(QDialog):
    def __init__(self, value, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Window2')
        self.setWindowIcon(self.style().standardIcon(
            QStyle.SP_FileDialogInfoView))

        label1 = QLabel(value)
        self.button = QPushButton()
        self.button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.button.setIcon(self.style().standardIcon(QStyle.SP_ArrowLeft))
        self.button.setIconSize(QSize(200, 200))

        layoutV = QVBoxLayout()
        self.pushButton = QPushButton(self)
        self.pushButton.setStyleSheet(
            'background-color: rgb(0,0,255); color: #fff')
        self.pushButton.setText('Click me!')
        self.pushButton.clicked.connect(self.goMainWindow)
        layoutV.addWidget(self.pushButton)

        layoutH = QHBoxLayout()
        layoutH.addWidget(label1)
        layoutH.addWidget(self.button)
        layoutV.addLayout(layoutH)
        self.setLayout(layoutV)

    def goMainWindow(self):
        self.cams = Window()
        self.cams.show()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())


