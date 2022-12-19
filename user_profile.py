# user_profile.py
# Import necessary modules
import sys, os.path
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap, QFont

class UserProfile(QWidget):
	def __init__(self):
		super().__init__()
		self.initializeUI()

	def initializeUI(self):
		"""
		Initialze the window and display its contents to the screen.
		"""
		self.setGeometry(50, 50, 250, 400)
		self.setWindowTitle("2.1 - User Profile GUI")
		self.displayImages()
		self.displayUserInfo()

		self.show()

	def displayImages(self):
		"""
		배경 이미지와 프로필 이미지 표시
		이미지가 없으면 예외처리함
		"""
		background_image = "images/skyblue.jpg"
		profile_image = "images/profile_image.jpg"

		try:
			with open(background_image):
				background = QLabel(self)
				pixmap = QPixmap(background_image)
				background.setPixmap(pixmap)
		except FileNotFoundError:
			print("그런 이미지는 없는데요.")

		try:
			with open(profile_image):
				user_image = QLabel(self)
				pixmap = QPixmap(profile_image)
				user_image.setPixmap(pixmap)
				user_image.move(80, 20)
		except FileNotFoundError:
			print("그런 이미지는 없는데요.")			

	def displayUserInfo(self):
		"""
		사용자 프로필을 표시하기 위한 프로필 만듦
		"""
		user_name = QLabel(self)
		user_name.setText("HyungKu Im")
		user_name.move(45, 140)
		user_name.setFont(QFont('Arial', 20))
		bio_title = QLabel(self)
		bio_title.setText("Biography")
		bio_title.move(15, 170)
		bio_title.setFont(QFont('Arial', 17))

		about = QLabel(self)
		about.setText("저는 개발자입니다. 잘 부탁드립니다 경력은 20년입니다.")
		about.setWordWrap(True)
		about.move(15,200)

		skills_title = QLabel(self)
		skills_title.setText("Skills")
		skills_title.move(15, 250)
		skills_title.setFont(QFont('Arial', 17))

		skills = QLabel(self)
		skills.setText("Python | Java | Oracle")
		skills.move(15, 280)

		experience_title = QLabel(self)
		experience_title.setText("Experience")
		experience_title.move(15, 300)
		experience_title.setFont(QFont('Arial', 17))

		experience = QLabel(self)
		experience.setText("지스펙 오라클자바 교육학원")
		experience.move(15, 330)

		dates = QLabel(self)
		dates.setText("2012년 2월 - 현재")
		dates.move(15, 340)
		dates.setFont(QFont('Arial', 10))

		experience = QLabel(self)
		experience.setText("모 대기업 물류관리시스템 개발")
		experience.move(15, 360)

		dates = QLabel(self)
		dates.setText("2001년 10월 - 2012년 1월")
		dates.move(15, 370)
		dates.setFont(QFont('Arial', 10))


if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = UserProfile()
	sys.exit(app.exec_())