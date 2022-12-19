# labels.py
# Import necessary modules
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap

class HelloWorldWindow(QWidget):
	def __init__(self):
		super().__init__()
		self.initializeUI()

	def initializeUI(self):
		"""
		Initialze the window and display its contents to the screen.
		"""
		self.setGeometry(100, 100, 400, 300)
		self.setWindowTitle("QLabel Example")
		self.displayLabels()
		self.show()

	def displayLabels(self):
		"""
		텍스트, 이미지 표시(QLabel활용)
		이미지가 없으면 예외처리함
		"""
		text = QLabel("안녕하세요", self)
		# text.setText("안녕하세요")
		text.move(105, 15)

		images = "images/world.png"
		try:
			with open(images):
				world_image = QLabel(self)
				pixmap = QPixmap(images)
				world_image.setPixmap(pixmap)
				world_image.move(25, 40)
		except FileNotFoundError:
			print("그런 이미지는 없는데요")


if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = HelloWorldWindow()
	sys.exit(app.exec_())