import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow,QWidget,QApplication,QVBoxLayout,QStackedLayout,QFormLayout,QMenuBar,QMenu,QLineEdit,QLabel,QComboBox,QTextEdit,QPushButton,QFileDialog,QInputDialog
from PyQt6.QtGui import QAction,QIcon,QTextCursor,QColor

class Window(QMainWindow):
  def __init__(self) :
    super().__init__()

    self.initUI()

  def initUI(self):
    self.setWindowTitle("Notepad")
    self.setGeometry(100,100,400,300)

    self.current_file = None

    self.edit_field = QTextEdit()
    self.setCentralWidget(self.edit_field)

    # Create a menubar
    self.menu_bar = QMenuBar()
    self.setMenuBar(self.menu_bar)

    # Create a file menu
    self.file_menu = QMenu("File", self)
    self.menu_bar.addMenu(self.file_menu)

    # Create actions
    new_action = QAction("New", self)
    self.file_menu.addAction(new_action)
    new_action.triggered.connect(self.new_file)

    open_action = QAction("Open", self)
    self.file_menu.addAction(open_action)
    open_action.triggered.connect(self.open_file)

    save_action = QAction("Save", self)
    self.file_menu.addAction(save_action)
    save_action.triggered.connect(self.save_file)

    save_as_action = QAction("Save as", self)
    self.file_menu.addAction(save_as_action)
    save_as_action.triggered.connect(self.save_as_file)

    # Create a edit menu
    self.edit_menu = QMenu("Edit", self)
    self.menu_bar.addMenu(self.edit_menu)

    undo_action = QAction("Undo", self)
    self.edit_menu.addAction(undo_action)
    undo_action.triggered.connect(self.edit_field.undo)

    redo_action = QAction("Redo", self)
    self.edit_menu.addAction(redo_action)
    redo_action.triggered.connect(self.edit_field.redo)

    cut_action = QAction("Cut", self)
    self.edit_menu.addAction(cut_action)
    cut_action.triggered.connect(self.edit_field.cut)

    copy_action = QAction("Copy", self)
    self.edit_menu.addAction(copy_action)
    copy_action.triggered.connect(self.edit_field.copy)

    paste_action = QAction("Paste", self)
    self.edit_menu.addAction(paste_action)
    paste_action.triggered.connect(self.edit_field.paste)

    find_action = QAction("Find", self)
    self.edit_menu.addAction(find_action)
    find_action.triggered.connect(self.find_text)
    


  def new_file(self):
    self.edit_field.clear()
    self.current_file = None

  def open_file(self):
    file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "All Files(*);; Python File(*.py)")
    if file_path:
      with open(file_path, "r") as file:
        text = file.read()
        self.edit_field.setText(text)
        self.current_file = file_path

  def save_file(self):
    if self.current_file:
      with open(self.current_file, "w") as file:
        file.write(self.edit_field.toPlainText())
    else:
      self.save_as_file()

  def save_as_file(self):
    file_path, _ = QFileDialog.getSaveFileName(self,"Save file", "", "All Files(*);; Python File(*.py)")
    if file_path:
      with open(file_path, "w") as file:
        file.write(self.edit_field.toPlainText())
      self.current_file = file_path
  
  def find_text(self):
    query, ok = QInputDialog.getText(self, "Find text", "Search for")
    if ok:
      all_words=[]
      self.edit_field.moveCursor(QTextCursor.MoveOperation.Start)
      highlight_color = QColor(Qt.GlobalColor.red)
      
      while(self.edit_field.find(query)):
        selection = QTextEdit.ExtraSelection()
        selection.format.setBackground(highlight_color)

        selection.cursor = self.edit_field.textCursor()
        all_words.append(selection)
      
      self.edit_field.setExtraSelections(all_words)
    



app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())