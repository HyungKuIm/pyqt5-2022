# drag_drop.py
# Import necessary modules
import sys, os
from PyQt5.QtWidgets import (QApplication, QWidget, 
	QListWidget, QLabel, QGridLayout, QListWidgetItem)
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon

class DragAndDropGui(QWidget):
	def __init__(self):
		super().__init__() # QWidget의 기본 생성자 부름
		self.initializeUI()

	def initializeUI(self):
		"""
		윈도우와 화면에 출력되는 컨텐츠 초기화
		"""
		self.setGeometry(100, 100, 500, 300)
		self.setWindowTitle("파이큐티 기본 창 - drag and drop")

		self.setupWidgets()

		self.show()

	def setupWidgets(self):
		icon_label = QLabel("ICONS", self)
		icon_widget = QListWidget()
		icon_widget.setAcceptDrops(True)
		icon_widget.setDragEnabled(True)
		icon_widget.setViewMode(QListWidget.IconMode)

		image_path = "images"
		for img in os.listdir(image_path):
			list_item = QListWidgetItem()
			list_item.setText(img.split(".")[0])
			list_item.setIcon(QIcon(os.path.join(image_path, "{0}").format(img)))
			icon_widget.setIconSize(QSize(50, 50))
			icon_widget.addItem(list_item)

		list_label = QLabel("LIST", self)
		list_widget = QListWidget()
		list_widget.setAlternatingRowColors(True)

		list_widget.setAcceptDrops(True)
		list_widget.setDragEnabled(True)

		grid = QGridLayout()
		grid.addWidget(icon_label, 0, 0)
		grid.addWidget(list_label, 0, 1)
		grid.addWidget(icon_widget, 1, 0)
		grid.addWidget(list_widget, 1, 1)

		self.setLayout(grid)

# 프로그램 실행
if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = DragAndDropGui()
	sys.exit(app.exec_())