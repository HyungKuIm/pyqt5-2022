# clipboard_ex.py
# Import necessary modules
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton,
	QTextEdit, QDockWidget, QVBoxLayout, QFrame)
from PyQt5.QtCore import Qt, QSize

class ClipboardEx(QMainWindow):
	def __init__(self):
		super().__init__() # QWidget의 기본 생성자 부름
		self.initializeUI()

	def initializeUI(self):
		"""
		윈도우와 화면에 출력되는 컨텐츠 초기화
		"""
		# self.setGeometry(100, 100, 400, 300)
		self.setMinimumSize(QSize(500, 300))
		self.setWindowTitle("파이큐티 기본 창")

		self.central_widget = QTextEdit()
		self.setCentralWidget(self.central_widget)

		self.createClipboard()

		self.show()

	def createClipboard(self):
		clipboard_dock = QDockWidget();
		clipboard_dock.setWindowTitle("Display Clipboard Contents")
		clipboard_dock.setAllowedAreas(Qt.TopDockWidgetArea)

		dock_frame = QFrame()
		self.cb_text = QTextEdit()
		paste_button = QPushButton("Paste")
		paste_button.clicked.connect(self.pasteText)

		dock_v_box = QVBoxLayout()
		dock_v_box.addWidget(self.cb_text)
		dock_v_box.addWidget(paste_button)

		dock_frame.setLayout(dock_v_box)
		clipboard_dock.setWidget(dock_frame)

		self.addDockWidget(Qt.TopDockWidgetArea, clipboard_dock)

		self.clipboard = QApplication.clipboard()
		self.clipboard.dataChanged.connect(self.copyFromClipboard)

	def copyFromClipboard(self):
		mime_data = self.clipboard.mimeData()
		if mime_data.hasText():
			self.cb_text.setText(mime_data.text())

	def pasteText(self):
		self.central_widget.paste()

# 프로그램 실행
if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = ClipboardEx()
	sys.exit(app.exec_())