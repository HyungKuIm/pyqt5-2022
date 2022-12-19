# Registration.py
# Import necessary modules
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, 
	QLabel, QMessageBox, QLineEdit, QPushButton)
from PyQt5.QtGui import QFont, QPixmap

class CreateNewUser(QWidget):
	def __init__(self):
		super().__init__()
		self.initializeUI()

	def initializeUI(self):
		"""
		Initialze the window and display its contents to the screen.
		"""
		self.setGeometry(100, 100, 400, 400)
		self.setWindowTitle("3.2 - Create New User")
		self.displayWidgetsToCollectInfo()

		self.show()

	def displayWidgetsToCollectInfo(self):
		# 이미지를 위한 레이블 설정
		new_user_image = "images/new_user_icon.png"
		try:
			with open(new_user_image):
				new_user = QLabel(self)
				pixmap = QPixmap(new_user_image)
				new_user.setPixmap(pixmap)
				new_user.move(150, 60)
		except FileNotFoundError:
			print("그런 이미지가 없는데요")

		login_label = QLabel(self)
		login_label.setText("회원 가입")
		login_label.move(110, 20)
		login_label.setFont(QFont('Arial', 20))

		# Username and fullname labels and line edit widgets
		name_label = QLabel("아이디:", self)
		name_label.move(50, 180)

		self.name_entry = QLineEdit(self)
		self.name_entry.move(130, 180)
		self.name_entry.resize(200, 20)

		name_label = QLabel("전체 이름:", self)
		name_label.move(50, 210)

		name_entry = QLineEdit(self)
		name_entry.move(130, 210)
		name_entry.resize(200, 20)

		# 비밀번호와 비밀번호 확인
		pswd_label = QLabel("비밀번호:", self)
		pswd_label.move(50, 240)

		self.pswd_entry = QLineEdit(self)
		self.pswd_entry.setEchoMode(QLineEdit.Password)
		self.pswd_entry.move(130, 240)
		self.pswd_entry.resize(200, 20)

		confirm_label = QLabel("비밀번호 확인:", self)
		confirm_label.move(50, 270)

		self.confirm_entry = QLineEdit(self)
		self.confirm_entry.setEchoMode(QLineEdit.Password)
		self.confirm_entry.move(130, 270)
		self.confirm_entry.resize(200, 20)

		# Create sign up button
		sign_up_button = QPushButton("회원가입", self)
		sign_up_button.move(100, 310)
		sign_up_button.resize(200, 40)
		sign_up_button.clicked.connect(self.confirmSignUp)



	def confirmSignUp(self):
		"""
		When user...
		"""
		pswd_text = self.pswd_entry.text()
		confirm_text = self.confirm_entry.text()

		if pswd_text != confirm_text:
			QMessageBox.warning(self, "에러 메시지",
				"비밀번호가 일치하지 않습니다. 다시 입력해 주세요.", QMessageBox.Close,
				QMessageBox.Close)
		else:
			with open("files/users.txt", "a+") as f:
				f.write(self.name_entry.text() + " ")
				f.write(pswd_text + "\n")
			self.close()
		

	

if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = CreateNewUser()
	sys.exit(app.exec_())