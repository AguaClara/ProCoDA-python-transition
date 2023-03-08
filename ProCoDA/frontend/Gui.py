from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QComboBox, QLabel, QSpinBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette
#from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QWidget, QComboBox, QCheckBox, QRadioButton, QPushButton, QTableWidget, QLineEdit, QSlider, QProgressBar
# from matplotlib.figure import Figure
# from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
# import sys
# import matplotlib
# matplotlib.use('Qt5Agg')


# class MplCanvas(FigureCanvasQTAgg):

#     def __init__(self, parent=None, width=5, height=4, dpi=100):
#         fig = Figure(figsize=(width, height), dpi=dpi)
#         self.axes = fig.add_subplot(111)
#         super(MplCanvas, self).__init__(fig)


# class MainWindow(QMainWindow):

#     def __init__(self, *args, **kwargs):
#         super(MainWindow, self).__init__(*args, **kwargs)

#         # Create the maptlotlib FigureCanvas object,
#         # which defines a single set of axes as self.axes.
#         # sc = MplCanvas(self, width=5, height=4, dpi=100)
#         # sc.axes.plot([0, 1, 2, 3, 4], [10, 1, 20, 3, 40])
#         self.button1 = QPushButton(self)
#         self.button1.setText("Generate Graph of Data")
#         self.button1.clicked.connect(self.button1_clicked)
#         self.button1.setGeometry(1800, 1650, 100, 100)

#         self.setWindowTitle("ProCoDa App")

#         self.show()

#     def button1_clicked(self):
#         sc = MplCanvas(self, width=5, height=4, dpi=100)
#         sc.axes.plot([0, 1, 2, 3, 4], [10, 1, 20, 3, 40])
#         self.setCentralWidget(sc)


# app = QApplication(sys.argv)
# w = MainWindow()
# sys.exit(app.exec())

app = QApplication([])
app.setStyle('Fusion')
# palette = QPalette()
# palette.setColor(QPalette.Button, Qt.green)
# app.setPalette(palette)

window = QWidget()

layout_top = QHBoxLayout()
layout_top.addWidget(QPushButton('Data Visualization'))
layout_top.addWidget(QPushButton('Data Acquisition'))
layout_top.addWidget(QPushButton('Parametric Studies'))

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
window.setLayout(layout)
window.setWindowTitle('ProCoDa App')
window.show()
app.exec()
