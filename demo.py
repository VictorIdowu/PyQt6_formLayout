import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget,QApplication,QFormLayout,QLineEdit,QLabel,QComboBox,QTextEdit,QPushButton

class Window(QWidget):
  def __init__(self) :
    super().__init__()

    self.initUI()

  def initUI(self):
    self.setWindowTitle("Form Layout")
    self.setGeometry(100,100,400,200)

    form_layout = QFormLayout()
    self.setLayout(form_layout)

    # Labels and inputs
    self.name_input = QLineEdit()
    self.email_input = QLineEdit()
    self.phone_input = QLineEdit()

    self.subject_combo = QComboBox()
    self.subject_combo.addItems(["Select Subject", "Personal", "Business"])

   
    self.message_input = QTextEdit()

    submit_button = QPushButton("Submit")
    submit_button.clicked.connect(self.submit_clicked)

    
    form_layout.addRow(QLabel("Name"),self.name_input)
    form_layout.addRow(QLabel("Email"),self.email_input)
    form_layout.addRow(QLabel("Phone number"),self.phone_input)
    form_layout.addRow(QLabel("Subject"),self.subject_combo)
    form_layout.addRow(QLabel("Message"),self.message_input)
    form_layout.addRow(submit_button)


  def submit_clicked(self):
    name = self.name_input.text()
    email = self.email_input.text()
    phone = self.phone_input.text()
    subject = self.subject_combo.currentText()
    message = self.message_input.toPlainText()
    print(f"Name: {name}\nEmail: {email}\nPhone: {phone}\nSubject: {subject}\nMessage: {message}")
    self.name_input.setText("")
    self.email_input.setText("")
    self.phone_input.setText("")
    self.subject_combo.setCurrentIndex(0)
    self.message_input.setText("")

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())