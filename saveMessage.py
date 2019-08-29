import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class SaveMessage(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        answer = QMessageBox.about(self,"확인","저장되었습니다.")
        print(answer)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SaveMessage()
    sys.exit(app.exec())