import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget,QApplication,QVBoxLayout,QStackedLayout,QFormLayout,QLineEdit,QLabel,QComboBox,QTextEdit,QPushButton

class Window(QWidget):
  def __init__(self) :
    super().__init__()

    self.initUI()

  def initUI(self):
    self.setWindowTitle("Form Layout")
    self.setGeometry(100,100,400,200)

    self.combo_box = QComboBox()
    self.combo_box.addItems(["Label", "Form"])
    self.combo_box.activated.connect(self.switch_pages)

    # Creating Page 1
    label = QLabel("This is a label page")

    # Creating Page 2
    form_layout = QFormLayout()
    page2_containter = QWidget()
    page2_containter.setLayout(form_layout)

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

    # Creating a stacked layout
    self.stacked_layout = QStackedLayout()
    self.stacked_layout.addWidget(label)
    self.stacked_layout.addWidget(page2_containter)

    main_layout = QVBoxLayout()
    main_layout.addWidget(self.combo_box)
    main_layout.addLayout(self.stacked_layout)
    self.setLayout(main_layout)

  def switch_pages(self, index):
    self.stacked_layout.setCurrentIndex(index)
    
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