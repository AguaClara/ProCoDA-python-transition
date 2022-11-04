import sys

from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QComboBox, QCheckBox, QRadioButton, QPushButton, QTableWidget, QLineEdit, QSlider, QProgressBar

app = QApplication([])

window = QWidget()

window.setWindowTitle("ProCoDa App")

window.setGeometry(100, 100, 100, 100)

label = QLabel('This is a label', parent=window)

label.move(50, 20)

window.show()

sys.exit(app.exec())
