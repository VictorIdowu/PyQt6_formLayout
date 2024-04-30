import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow,QWidget,QApplication,QVBoxLayout,QStackedLayout,QFormLayout,QLineEdit,QLabel,QComboBox,QTextEdit,QPushButton
from PyQt6.QtGui import QAction,QIcon

class Window(QMainWindow):
  def __init__(self) :
    super().__init__()

    self.initUI()

  def initUI(self):
    self.setWindowTitle("Menu")
    self.setGeometry(100,100,400,300)

    toolbar = self.addToolBar("Main Toolbar")

    self.new_action = QAction(QIcon("icons/new_file.png"),"New")
    toolbar.addAction(self.new_action)

    toolbar.addSeparator()

    self.open_action = QAction(QIcon("icons/open.png"),"Open")
    toolbar.addAction(self.open_action)

    toolbar.addSeparator()

    self.save_action = QAction(QIcon("icons/save.png"),"Save")
    toolbar.addAction(self.save_action)
    

    
     

    

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())