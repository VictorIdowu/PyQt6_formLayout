import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget,QApplication,QFormLayout,QLineEdit,QLabel

class Window(QWidget):
  def __init__(self) :
    super().__init__()

    self.initUI()

  def initUI(self):
    self.setWindowTitle("Form Layout")
    self.setGeometry(100,100,400,200)

    label1 = QLabel("Name")
    name_input = QLineEdit()

    label2 = QLabel("Age")
    age_input = QLineEdit()

    form_layout = QFormLayout()
    self.setLayout(form_layout)
    
    form_layout.addRow(label1,name_input)
    form_layout.addRow(label2,age_input)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())