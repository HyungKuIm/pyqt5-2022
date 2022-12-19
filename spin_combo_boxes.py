# spin_combo_boxes.py
# Import necessary modules
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QComboBox,
			QSpinBox, QHBoxLayout, QVBoxLayout)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class SelectItems(QWidget):
	def __init__(self):
		super().__init__() # QWidget의 기본 생성자 부름
		self.initializeUI()

	def initializeUI(self):
		"""
		윈도우와 화면에 출력되는 컨텐츠 초기화
		"""
		self.setGeometry(100, 100, 300, 200)
		self.setWindowTitle("ComboBox and SpinBox")
		self.itemsAndPrices()
		self.show()

	def itemsAndPrices(self):
		"""
		아이템을 위한 콤보박스 및 가격을 위한 스핀 박스
		"""
		info_label = QLabel("드실 메뉴와 가격 2가지 선택")
		info_label.setFont(QFont('Arial', 16))
		info_label.setAlignment(Qt.AlignCenter)
		self.display_total_label = QLabel("전체 금액: ₩")
		self.display_total_label.setFont(QFont('Arial', 16))
		self.display_total_label.setAlignment(Qt.AlignRight)

		# 음식 목록
		lunch_list = ["삶은 계란", "토스트", "요구르트", "사과", "바나나", 
			"오렌지", "와플", "빵", "파스타", "크래커", "프레젤"]
		lunch_cb1 = QComboBox()
		lunch_cb1.addItems(lunch_list)
		lunch_cb2 = QComboBox()
		lunch_cb2.addItems(lunch_list)

		self.price_sb1 = QSpinBox()
		self.price_sb1.setRange(0, 10000)
		self.price_sb1.setSingleStep(500)
		self.price_sb1.setPrefix("₩")
		self.price_sb1.valueChanged.connect(self.calculateTotal)

		self.price_sb2 = QSpinBox()
		self.price_sb2.setRange(0, 10000)
		self.price_sb2.setSingleStep(500)
		self.price_sb2.setPrefix("₩")
		self.price_sb2.valueChanged.connect(self.calculateTotal)

		h_box1 = QHBoxLayout()
		h_box2 = QHBoxLayout()

		h_box1.addWidget(lunch_cb1)
		h_box1.addWidget(self.price_sb1)
		h_box2.addWidget(lunch_cb2)
		h_box2.addWidget(self.price_sb2)

		v_box = QVBoxLayout()
		v_box.addWidget(info_label)
		v_box.addLayout(h_box1)
		v_box.addLayout(h_box2)
		v_box.addWidget(self.display_total_label)

		self.setLayout(v_box)



	def calculateTotal(self):
		"""
		토탈 가격 계산 and 표시
		"""
		total = self.price_sb1.value() + self.price_sb2.value()
		self.display_total_label.setText("총 금액: ₩{}".format(str(total)))
	

# 프로그램 실행
if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = SelectItems()
	sys.exit(app.exec_())