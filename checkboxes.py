# checkboxes.py
# Import necessary modules
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, 
	QLabel, QCheckBox)
from PyQt5.QtCore import Qt


class CheckBoxWindow(QWidget):
	def __init__(self):
		super().__init__()
		self.initializeUI()

	def initializeUI(self):
		"""
		Initialze the window and display its contents to the screen.
		"""
		self.setGeometry(100, 100, 250, 250)
		self.setWindowTitle("QCheckBox Widget")
		self.displayCheckBoxes()

		self.show()

	def displayCheckBoxes(self):
		'''
		체크박스와 다른 위젯을 초기화한다.
		'''
		header_label = QLabel(self)
		header_label.setText("하루중 언제 일하실 수 있나요? (가능한 시간대 모두 표시)")
		header_label.setWordWrap(True)
		header_label.move(10, 10)
		header_label.resize(230, 60)

		# Set up checkboxes
		morning_cb = QCheckBox("오전 파트 [8 AM-2 PM]", self) # text, parent
		morning_cb.move(20, 80)
		morning_cb.toggle()
		morning_cb.stateChanged.connect(self.printToTerminal)

		after_cb = QCheckBox("오후 파트 [1 PM-8 PM]", self)
		after_cb.move(20, 100)
		after_cb.stateChanged.connect(self.printToTerminal)

		night_cb = QCheckBox("저녁 파트 [7 PM-3 AM]", self)
		night_cb.move(20, 120)
		night_cb.stateChanged.connect(self.printToTerminal)

	def printToTerminal(self, state):
		'''
		체크 박스의 상태를 점검하는 간단한 메서드
		'''
		sender = self.sender()
		if state == Qt.Checked:
			print("{} Selected.".format(sender.text()))
		else:
			print("{} Deselected.".format(sender.text()))
	


if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = CheckBoxWindow()
	sys.exit(app.exec_())