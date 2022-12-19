# notepad.py
# Import necessary modules
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, 
		QTextEdit, QMessageBox, QFileDialog, QHBoxLayout, QVBoxLayout)

class Notepad(QWidget):
	def __init__(self):
		super().__init__() # QWidget의 기본 생성자 부름
		self.initializeUI()

	def initializeUI(self):
		"""
		윈도우와 화면에 출력되는 컨텐츠 초기화
		"""
		self.setGeometry(100, 100, 300, 400)
		self.setWindowTitle("메모장")
		self.notepadWidgets()
		self.show()

	def notepadWidgets(self):
		"""
		메모장을 위한 위젯 생성 및 정렬
		"""
		# 편집 메뉴의 푸쉬 버튼
		new_button = QPushButton("New")
		# new_button.move(10, 20)
		new_button.clicked.connect(self.clearText)

		save_button = QPushButton("Save")
		# save_button.move(80, 20)
		save_button.clicked.connect(self.saveText)

		top_h_box = QHBoxLayout()
		top_h_box.addWidget(new_button)
		top_h_box.setSpacing(20)
		top_h_box.addWidget(save_button)


		# 텍스트 에디트 필드 생성
		self.text_field = QTextEdit()
		# self.text_field.resize(280, 330)
		# self.text_field.move(10, 60)

		main_h_box = QHBoxLayout()
		# main_h_box.addStretch()
		main_h_box.addWidget(self.text_field)
		# main_h_box.addStretch()

		v_box = QVBoxLayout()
		v_box.addLayout(top_h_box)
		v_box.addLayout(main_h_box)

		self.setLayout(v_box)

	def clearText(self):
		"""
		new 버튼을 클릭하면, 텍스트 에디트 필드를 정리할지 물어본다
		"""
		answer = QMessageBox.question(self, "Clear Text",
			"텍스트를 정리하시겠습니까?", QMessageBox.No | QMessageBox.Yes,
					QMessageBox.Yes)
		if answer == QMessageBox.Yes:
			self.text_field.clear()
		else:
			pass

	def saveText(self):
		"""
		save 버튼을 클릭하면, 텍스트 파일로 저장할지 지정하는 다이얼로그 표시
		"""
		options = QFileDialog.Options()
		notepad_text = self.text_field.toPlainText()

		file_name, _ = QFileDialog.getSaveFileName(self, "Save File", "", "모든 파일 (*);;텍스트 파일 (*.txt)", options=options)

		if file_name:
			with open(file_name, 'w', encoding='utf-8') as f:
				f.write(notepad_text)

# 프로그램 실행
if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = Notepad()
	sys.exit(app.exec_())