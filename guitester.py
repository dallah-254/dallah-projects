import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget

app = QApplication(sys.argv)
window = QWidget()

window.setWindowTitle("Hello PyQt!")
window.setGeometry(100, 100, 280, 80)

label = QLabel("Hello, PyQt!", window)
window.show()

sys.exit(app.exec_())
