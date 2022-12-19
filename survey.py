# survey.py
# Import necessary modules
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, 
		QLabel, QCheckBox, QButtonGroup, QHBoxLayout, QVBoxLayout)
from PyQt5.QtGui import QFont

class DisplaySurvey(QWidget):
	def __init__(self):
		super().__init__() # QWidget의 기본 생성자 부름
		self.initializeUI()

	def initializeUI(self):
		"""
		윈도우와 화면에 출력되는 컨텐츠 초기화
		"""
		self.setGeometry(100, 100, 400, 230)
		self.setWindowTitle("설문조사")
		self.surveyWidgets()
		self.show()

	def surveyWidgets(self):
		"""
		설문조사를 위한 위젯 생성 및 정렬
		"""
		# 레이블과 버튼 위젯
		title = QLabel("구로구 호텔", self)
		title.setFont(QFont('Arial', 17))
		question = QLabel("오늘 서비스는 어떠셨나요?", self)

		title_h_box = QHBoxLayout()
		title_h_box.addStretch()
		title_h_box.addWidget(title)
		title_h_box.addStretch()

		ratings = ["불만족", "보통", "만족"]

		rating_h_box = QHBoxLayout()
		rating_h_box.setSpacing(60)
		rating_h_box.addStretch()
		for rating in ratings:
			rate_label = QLabel(rating, self)
			rating_h_box.addWidget(rate_label)
		rating_h_box.addStretch()

		cb_h_box = QHBoxLayout()
		cb_h_box.setSpacing(100)

		scale_bg = QButtonGroup(self)
		
		cb_h_box.addStretch()
		for cb in range(len(ratings)):
			scale_cb = QCheckBox(str(cb), self)
			cb_h_box.addWidget(scale_cb)
			scale_bg.addButton(scale_cb)
		cb_h_box.addStretch()

		scale_bg.buttonClicked.connect(self.checkboxClicked)

		close_button = QPushButton("Close", self)
		close_button.clicked.connect(self.close)

		v_box = QVBoxLayout()
		v_box.addLayout(title_h_box)
		v_box.addWidget(question)
		v_box.addStretch(1)
		v_box.addLayout(rating_h_box)
		v_box.addLayout(cb_h_box)
		v_box.addStretch(2)
		v_box.addWidget(close_button)

		self.setLayout(v_box)



	def checkboxClicked(self, cb):
		"""
		체크박스에서 선택한 텍스트를 출력한다
		"""
		print("{} Selected.".format(cb.text()))

	
# 프로그램 실행
if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = DisplaySurvey()
	sys.exit(app.exec_())