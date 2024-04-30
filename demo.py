import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow,QWidget,QApplication,QVBoxLayout,QStackedLayout,QFormLayout,QLineEdit,QLabel,QComboBox,QTextEdit,QPushButton
from PyQt6.QtGui import QAction

class Window(QMainWindow):
  def __init__(self) :
    super().__init__()

    self.initUI()

  def initUI(self):
    self.setWindowTitle("Menu")
    self.setGeometry(100,100,400,300)

    # Step 1 Create a menubar
    menubar = self.menuBar()

    # Creating menu items
    file_menu = menubar.addMenu("File")

    # Creating an action
    self.new_action = QAction("New")
    # Adding action to the menu
    file_menu.addAction(self.new_action)

    # Adding a seperator
    file_menu.addSeparator()

    # Creating exit action
    self.exit_action = QAction("Exit")
    # Adding action to the menu
    file_menu.addAction(self.exit_action)
    
    # Creating edit menu
    edit_menu = menubar.addMenu("Edit")

    

    self.copy_action = QAction("Copy")
    edit_menu.addAction(self.copy_action)
    edit_menu.addSeparator()
    
    self.cut_action = QAction("Cut")
    edit_menu.addAction(self.cut_action)
    edit_menu.addSeparator()
    
    self.paste_action = QAction("Paste")
    edit_menu.addAction(self.paste_action)
     

    

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())