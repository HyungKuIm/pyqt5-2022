# listwidget_ex.py
# Import necessary modules
import sys, os
from PyQt5.QtWidgets import (QApplication, QWidget, 
	QListWidget, QPushButton, QLabel, QGridLayout, QListWidgetItem,
	QHBoxLayout, QVBoxLayout, QInputDialog)
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon

class DangunGui(QWidget):
	def __init__(self):
		super().__init__() # QWidget의 기본 생성자 부름
		self.initializeUI()

	def initializeUI(self):
		"""
		윈도우와 화면에 출력되는 컨텐츠 초기화
		"""
		self.setGeometry(100, 100, 500, 300)
		self.setWindowTitle("QListWidget Example")

		self.setupWidgets()

		self.show()

	def setupWidgets(self):
		self.list_widget = QListWidget()
		self.list_widget.setAlternatingRowColors(True)

		dangun_list = ["갤럭시4워치", "Z 플립4 커버링", "i5-6500", "i5-2500", "액토 무선 마우스", "xps17", "스카이 폴더폰"]
		for item in dangun_list:
			list_item = QListWidgetItem()
			list_item.setText(item)
			self.list_widget.addItem(list_item)

		add_button = QPushButton("Add")
		add_button.clicked.connect(self.addListItem)

		insert_button = QPushButton("Insert")
		insert_button.clicked.connect(self.insertItemInList)

		remove_button = QPushButton("Remove")
		remove_button.clicked.connect(self.removeOneItem)

		clear_button = QPushButton("Clear")
		clear_button.clicked.connect(self.list_widget.clear)

		right_v_box = QVBoxLayout()
		right_v_box.addWidget(add_button)
		right_v_box.addWidget(insert_button)
		right_v_box.addWidget(remove_button)
		right_v_box.addWidget(clear_button)

		left_h_box = QHBoxLayout()
		left_h_box.addWidget(self.list_widget)
		left_h_box.addLayout(right_v_box)

		self.setLayout(left_h_box)

	def addListItem(self):
		text, ok = QInputDialog.getText(self, "New Item", "Add Item:")

		if ok and text != "":
			list_item = QListWidgetItem()
			list_item.setText(text)
			self.list_widget.addItem(list_item)

	def insertItemInList(self):
		text, ok = QInputDialog.getText(self, "Insert Item", "Insert Item:")

		if ok and text != "":
			row = self.list_widget.currentRow()
			row += 1
			new_item = QListWidgetItem()
			new_item.setText(text)
			self.list_widget.insertItem(row, new_item)

	def removeOneItem(self):
		row = self.list_widget.currentRow()
		self.list_widget.takeItem(row)	
		

# 프로그램 실행
if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = DangunGui()
	sys.exit(app.exec_())