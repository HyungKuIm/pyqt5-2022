# loginUI.py
# Import necessary modules
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, 
	QLabel, QMessageBox, QLineEdit, QPushButton, QCheckBox)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from Registration import CreateNewUser

class LoginUI(QWidget):
	def __init__(self):
		super().__init__()
		self.initializeUI()

	def initializeUI(self):
		"""
		Initialze the window and display its contents to the screen.
		"""
		self.setGeometry(100, 100, 400, 230)
		self.setWindowTitle("3.1 - Login GUI")
		self.loginUserInterface()

		self.show()

	def loginUserInterface(self):
		'''
		로그인 GUI 작성
		'''
		login_label = QLabel(self)
		login_label.setText("로그인")
		login_label.move(180, 10)
		login_label.setFont(QFont('Arial', 20))

		# 사용자 이름과 패스워드 설정
		name_label = QLabel("아이디:", self)
		name_label.move(30, 60)

		self.name_entry = QLineEdit(self)
		self.name_entry.move(110, 60)
		self.name_entry.resize(220, 20)

		password_label = QLabel("비밀번호:", self)
		password_label.move(30, 90)

		self.password_entry = QLineEdit(self)
		#self.password_entry.setEchoMode(QLineEdit.Password)
		self.password_entry.move(110, 90)
		self.password_entry.resize(220, 20)

		# 로그인 푸쉬버튼
		sign_in_button = QPushButton('로그인', self)
		sign_in_button.move(110, 140)
		sign_in_button.resize(200, 40)
		sign_in_button.clicked.connect(self.clickLogin)

		# 비번표시 체크박스
		show_pswd_cb = QCheckBox("비번 표시", self)
		show_pswd_cb.move(110, 115)
		show_pswd_cb.stateChanged.connect(self.showPassword)
		show_pswd_cb.toggle()
		show_pswd_cb.setChecked(False)



		# 회원가입 레이블과 버튼 표시
		not_a_member = QLabel("회원이 아니신가요?", self)
		not_a_member.move(70, 200)

		sign_up = QPushButton("회원가입", self)
		sign_up.move(160, 195)
		sign_up.clicked.connect(self.createNewUser)



	def clickLogin(self):
		users = {} # 사용자 정보를 저장하기 위해 빈 딕셔너리 생성
		# users.txt파일이 있는지 체크하고 없으면 새로 만듦
		try:
			with open("files/users.txt", "r", encoding="utf-8") as f:
				for line in f:
					user_fields = line.split(" ")
					username = user_fields[0]
					password = user_fields[1].strip('\n')
					users[username] = password
		except FileNotFoundError:
			print("파일이 존재하지 않습니다. 새로 만들게요.")
			f = open("files/users.txt", "w")

		username = self.name_entry.text()
		password = self.password_entry.text()
		if (username, password) in users.items():
			QMessageBox.information(self, "로그인 성공!", "로그인에 성공하셨습니다!",
				QMessageBox.Ok, QMessageBox.Ok)
			self.close() # close program
		else:
			QMessageBox.warning(self, "에러 메시지", "아이디나 비번이 틀렸습니다.",
				QMessageBox.Close, QMessageBox.Close)

	def showPassword(self, state):		
		if state == Qt.Checked:
			self.password_entry.setEchoMode(QLineEdit.Normal)
		else:
			self.password_entry.setEchoMode(QLineEdit.Password)

	def createNewUser(self):
		self.create_new_user_dialog = CreateNewUser()
		self.create_new_user_dialog.show()

	def closeEvent(self, event):
		"""
		프로그램을 종료했을 때 QMessageBox를 보여준다.
		"""
		# 메시지 박스 설정
		quit_msg = QMessageBox.question(self, "프로그램 종료",
			"정말로 종료하시겠습니까?", QMessageBox.No | QMessageBox.Yes,
			QMessageBox.Yes)
		if quit_msg == QMessageBox.Yes:
			event.accept() # 이벤트를 받아들여서 프로그램을 종료
		else:
			event.ignore() # 클로즈 이벤트를 무시한다.
		

if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = LoginUI()
	sys.exit(app.exec_())