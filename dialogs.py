# dialogs.py
# Import necessary modules
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, 
	QLabel, QMessageBox, QLineEdit, QPushButton)
from PyQt5.QtGui import QFont


class DisplayMessageBox(QWidget):
	def __init__(self):
		super().__init__()
		self.initializeUI()

	def initializeUI(self):
		"""
		Initialze the window and display its contents to the screen.
		"""
		self.setGeometry(100, 100, 400, 200)
		self.setWindowTitle("QMessageBox Example")
		self.displayWidgets()

		self.show()

	def displayWidgets(self):
		'''
		위젯 초기화
		'''
		catalogue_label = QLabel("저자 정보", self)
		catalogue_label.move(20, 20)	
		catalogue_label.setFont(QFont('Arial', 20))

		auth_label = QLabel("검색하실 저자 이름을 입력하세요:", self)
		auth_label.move(40, 60)

		# Create author label and line edit widgets
		author_name = QLabel("이름:", self)
		author_name.move(50, 90)

		self.auth_entry = QLineEdit(self)
		self.auth_entry.move(95, 90)
		self.auth_entry.setPlaceholderText("이름 성")

		# Create search button
		search_button = QPushButton("검색", self)
		search_button.move(125, 130)
		search_button.resize(150, 40)
		search_button.clicked.connect(self.displayMessageBox)

	def displayMessageBox(self):
		# authors.txt 파일이 존재하는지 체크
		try:
			with open("files/authors.txt", "r", encoding="utf-8") as f:
				authors = [line.rstrip('\n') for line in f]
		except FileNotFoundError:
			print("파일이 없어요")


		not_found_msg = QMessageBox()

		if self.auth_entry.text() in authors:
			QMessageBox().information(self, "저자 검색됨", "저자가 검색되었어요",
				QMessageBox.Ok, QMessageBox.Ok)
		else:
			not_found_msg = QMessageBox.question(self, "그런 저자가 없어요",
				"데이터베이스에 저자가 없습니다.\n계속하시겠어요?",
				QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

		if not_found_msg == QMessageBox.No:
			print("프로그램 종료.")
			self.close()
		else:
			pass
	


if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = DisplayMessageBox()
	sys.exit(app.exec_())