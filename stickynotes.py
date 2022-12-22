# stickynotes.py
# Import necessary modules
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QAction, QTextEdit)
from PyQt5.QtCore import QSize

class StickyNotes(QMainWindow):

	# Static variables
	note_id = 1
	notes = []

	def __init__(self, note_ref=str()):
		super().__init__() # QWidget의 기본 생성자 부름

		self.note_ref = note_ref
		StickyNotes.notes.append(self)

		self.initializeUI()

	def initializeUI(self):
		"""
		윈도우와 화면에 출력되는 컨텐츠 초기화
		"""
		# self.setGeometry(100, 100, 400, 300)
		self.setMinimumSize(QSize(250, 250))
		self.setWindowTitle("Sticky Notes : note_ref = " + self.note_ref)

		self.central_widget = QTextEdit()
		self.setCentralWidget(self.central_widget)

		self.createMenu()
		self.createClipboard()

		self.show()

	def createMenu(self):
		self.new_note_act = QAction('New Note', self)
		self.new_note_act.setShortcut('Ctrl+N')
		self.new_note_act.triggered.connect(self.newNote)

		self.close_act = QAction('Quit', self)
		self.close_act.setShortcut('Ctrl+W')
		self.close_act.triggered.connect(self.clearNote)

		self.quit_act = QAction('Quit', self)
		self.quit_act.setShortcut('Ctrl+Q')
		self.quit_act.triggered.connect(self.close)

		self.yellow_act = QAction('Yellow', self)
		self.yellow_act.triggered.connect(lambda: self.changeBackground(self.yellow_act.text()))

		self.blue_act = QAction('Blue', self)
		self.blue_act.triggered.connect(lambda: self.changeBackground(self.blue_act.text()))

		self.green_act = QAction('Green', self)
		self.green_act.triggered.connect(lambda: self.changeBackground(self.green_act.text()))	

		self.paste_act = QAction('Paste', self)
		self.paste_act.setShortcut('Ctrl+V')
		self.paste_act.triggered.connect(self.pasteToClipboard)

		# Create menubar
		menu_bar = self.menuBar()
		menu_bar.setNativeMenuBar(False)

		file_menu = menu_bar.addMenu('File')
		file_menu.addAction(self.new_note_act)
		file_menu.addAction(self.close_act)
		file_menu.addAction(self.quit_act)

		color_menu = menu_bar.addMenu('Color')
		color_menu.addAction(self.yellow_act)
		color_menu.addAction(self.blue_act)
		color_menu.addAction(self.green_act)

		paste_menu = menu_bar.addMenu('Paste')
		paste_menu.addAction(self.paste_act)

	def createClipboard(self):
		
		self.clipboard = QApplication.clipboard()
		self.clipboard.dataChanged.connect(self.copyToClipboard)

	def newNote(self):
		self.note_ref = str("note_%d" % StickyNotes.note_id)
		StickyNotes(self.note_ref).show()
		StickyNotes.note_id += 1

	def clearNote(self):
		self.central_widget.clear()


	def copyToClipboard(self):
		return self.clipboard.text()

	def pasteToClipboard(self):
		text = self.copyToClipboard()
		self.central_widget.insertPlainText(text + '\n')

	def changeBackground(self, color_text):
		if color_text == 'Yellow':
			self.central_widget.setStyleSheet("background-color: rgb(248, 253, 145)")
		elif color_text == 'Blue':
			self.central_widget.setStyleSheet("background-color: rgb(145, 253, 251)")
		elif color_text == 'Green':
			self.central_widget.setStyleSheet("background-color: rgb(148, 253, 145)")

# 프로그램 실행
if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = StickyNotes()
	sys.exit(app.exec_())