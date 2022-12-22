# paint_basics.py
# Import necessary modules
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import (QPainter, QPainterPath, QColor, QBrush, QPen, QFont, QPolygon, QLinearGradient)

class Drawing(QWidget):
	def __init__(self):
		super().__init__() # QWidget의 기본 생성자 부름
		self.initializeUI()

	def initializeUI(self):
		"""
		윈도우와 화면에 출력되는 컨텐츠 초기화
		"""
		self.setFixedSize(600, 600)
		self.setWindowTitle("파이큐티 기본 창")
		
		self.black = '#000000'
		self.blue = '#2041F1'
		self.green = '#12A708'
		self.purple = '#6512F0'
		self.red = '#E00C0C'
		self.orange = '#FF930A'

		self.show()

	def paintEvent(self, event):
		pass

# 프로그램 실행
if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = Drawing()
	sys.exit(app.exec_())