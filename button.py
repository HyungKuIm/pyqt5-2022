# user_profile.py
# Import necessary modules
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton


class ButtonWindow(QWidget):
	def __init__(self):
		super().__init__()
		self.initializeUI()

	def initializeUI(self):
		"""
		Initialze the window and display its contents to the screen.
		"""
		self.setGeometry(100, 100, 200, 150)
		self.setWindowTitle("QPushButton Widget")
		self.displayButton()

		self.show()

	def displayButton(self):
		'''
		버튼 위젯을 위한 설정
		'''
		name_label = QLabel(self)
		name_label.setText("Dont push the button.")
		name_label.move(60, 30) # 레이블 이등

		button = QPushButton(self)
		button.setText("Push me")
		button.clicked.connect(self.buttonClicked)
		button.move(80, 70) # 버튼 이등


	def buttonClicked(self):
		'''
		터미널에 메시지 출력
		그후 창을 닫는다.
		'''
		print("창이 닫혔습니다.")
		self.close()
	


if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = ButtonWindow()
	sys.exit(app.exec_())