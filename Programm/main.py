from PyQt5.QtWidgets import QMainWindow, QApplication
from ui import Ui_MainWindow
import sys

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        
        
        super().__init__(parent)
        self.setupUi(self)
        
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())