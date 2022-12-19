import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
	def __init__(self):
		super().__init__()
		# Add a title
		self.setWindowTitle("Hello World!")

		# Set Vertical layout
		self.setLayout(qtw.QVBoxLayout())

		# Create a label
		self.my_label = qtw.QLabel("Hello World! What's Your Name?")

		# Change the font size of label
		self.my_label.setFont(qtg.QFont('Helvetica', 18))



		self.layout().addWidget(self.my_label)

		# Create an entry box

		self.my_entry = qtw.QLineEdit()
		self.my_entry.setObjectName("name_field")
		self.my_entry.setText("")
		self.layout().addWidget(self.my_entry)

		# Create a button
		# my_button = qtw.QPushButton("Press Me!",
		# 	clicked = lambda: press_it())
		my_button = qtw.QPushButton("Press Me!", self)
		my_button.clicked.connect(self.press_it)
		self.layout().addWidget(my_button)


		# Show the app
		self.show()


	def press_it(self):
		# Add name to label
		self.my_label.setText(f'Hello {self.my_entry.text()}!')
		# Clear the entry box
		self.my_entry.setText("")



app = qtw.QApplication([])
mw = MainWindow()


# Run the app
app.exec_()