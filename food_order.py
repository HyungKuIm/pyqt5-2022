# food_order.py
# import necessary modules
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QTabWidget, QLabel, 
    QButtonGroup, QPushButton, QGridLayout,
    QRadioButton, QGroupBox, QLineEdit, QHBoxLayout, QVBoxLayout)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

style_sheet = """
QWidget {
    background-color: #C92108;
}

QWidget#Tabs {
    background-color: #FCEBCD;
    border-radius: 4px;
}

QWidget#ImageBorder {
    background-color: #FCF9F3;
    border-width: 2px;
    border-style: solid;
    border-radius: 4px;
    border-color: #FABB4C;
}

QWidget#Side {
    background-color: #EFD096;
    border-radius: 4px;
}

QLabel {
    background-color: #EFD096;
    border-width: 2px;
    border-style: solid;
    border-radius: 4px;
    border-color: #EFD096;
}

QLabel#Header {
    background-color: #EFD096;
    border-width: 2px;
    border-style: solid;
    border-radius: 4px;
    border-color: #EFD096;
    padding-left: 10px;
    color: #961A07;
}

QLabel#ImageInfo {
    background-color: #FCF9F3;
    border-radius: 4px;
}

QGroupBox {
    background-color: #FCEBCD;
    color: #961A07;
}

QRadioButton {
    background-color: #FCF9F3;
}

QPushButton {
    background-color: #C92108;
    border-radius: 4px;
    padding: 6px;
    color: #FFFFFF;
}

QPushButton:pressed {
    background-color: #C86354;
    border-radius: 4px;
    padding: 6px;
    color: #DBD8D7;
}
"""

class FoodOrderGUI(QWidget):

    def __init__(self):
        super().__init__()
        self.initializeUI() 

    def initializeUI(self):

        self.setMinimumSize(600, 700)
        self.setWindowTitle('Food Order GUI')

        self.setupTabsAndLayout()

        self.show()

    def setupTabsAndLayout(self):
        """
        Set up tab bar and different tab widgets. Each tab is a QWidget that
        serves as a container for each page. 
        """
        # Create tab bar and different tabs
        self.tab_bar = QTabWidget(self)

        self.pizza_tab = QWidget()
        self.pizza_tab.setObjectName("Tabs")
        self.sidedish_tab = QWidget()
        self.sidedish_tab.setObjectName("Tabs")

        self.tab_bar.addTab(self.pizza_tab, "피자")
        self.tab_bar.addTab(self.sidedish_tab, "사이드디시")

        # Call methods that contain the widgets for each tab
        self.pizzaTab()
        self.sidedishTab()


        # side widget
        self.side_widget = QWidget()
        self.side_widget.setObjectName("Tabs")
        order_label = QLabel("당신의 주문")
        order_label.setObjectName("Header")

        items_box = QWidget()
        items_box.setObjectName("Side")
        pizza_label = QLabel("피자 타입: ")
        self.display_pizza_label = QLabel("")
        toppings_label = QLabel("토핑: ")
        self.display_topping_label = QLabel("")
        extra_label = QLabel("기타 메뉴: ")
        self.display_sidedish_label = QLabel("")

       
        # grid layout (side widget)
        items_grid = QGridLayout()
        items_grid.addWidget(pizza_label, 0, 0, Qt.AlignRight)
        items_grid.addWidget(self.display_pizza_label, 0, 1)
        items_grid.addWidget(toppings_label, 1, 0, Qt.AlignRight)
        items_grid.addWidget(self.display_topping_label, 1, 1)
        items_grid.addWidget(extra_label, 2, 0, Qt.AlignRight)
        items_grid.addWidget(self.display_sidedish_label, 2, 1)

        items_box.setLayout(items_grid)

        side_v_box = QVBoxLayout()
        side_v_box.addWidget(order_label)
        side_v_box.addWidget(items_box)
        side_v_box.addStretch()
        self.side_widget.setLayout(side_v_box)
        
        main_h_box = QHBoxLayout()
        main_h_box.addWidget(self.tab_bar)
        main_h_box.addWidget(self.side_widget)

        self.setLayout(main_h_box)




    def pizzaTab(self):
        tab_pizza_label = QLabel("피자를 선택하세요")
        tab_pizza_label.setObjectName("Header")
        desc_box = QWidget()
        desc_box.setObjectName("ImageBorder")
        pizza_image_path = "images/pizza.jpg"
        pizza_image = self.loadImage(pizza_image_path)
        pizza_desc = QLabel()
        pizza_desc.setObjectName("ImageInfo")
        pizza_desc.setText("기존 피자에 좋아하는 크러스트와 토핑을 추가하세요. 치즈와 소스을 완벽한 맛을 더합니다.")
        pizza_desc.setWordWrap(True)      

        h_box = QHBoxLayout()
        h_box.addWidget(pizza_image)
        h_box.addWidget(pizza_desc)
        desc_box.setLayout(h_box)

        # Create group boc that will contain crust choices
        crust_gbox = QGroupBox()
        crust_gbox.setTitle("크러스트 선택")

        self.crust_group = QButtonGroup()
        gb_v_box = QVBoxLayout()
        crust_list = ["트리플 치즈 버스트 엣지", "더블치즈엣지", "기본"]

        for cr in crust_list:
            crust_rb = QRadioButton(cr)
            gb_v_box.addWidget(crust_rb)
            self.crust_group.addButton(crust_rb)

        crust_gbox.setLayout(gb_v_box)

        # Create group boc that will contain toppings choices
        toppings_gbox = QGroupBox()
        toppings_gbox.setTitle("토핑 선택")

        self.toppings_group = QButtonGroup()
        gb_v_box = QVBoxLayout()

        toppings_list = ["Pinapple", "Cheese", "Olive", "Beef", "Crab", "Tomato"]

        for top in toppings_list:
            toppings_rb = QRadioButton(top)
            gb_v_box.addWidget(toppings_rb)
            self.toppings_group.addButton(toppings_rb)
        self.toppings_group.setExclusive(False)

        toppings_gbox.setLayout(gb_v_box)

        # Create button to add information to side widget
        add_to_order_button1 = QPushButton("Add to Order")
        add_to_order_button1.clicked.connect(self.displayPizzaInOrder)

        # Create layout for pizza tab (Page 1)
        page1_v_box = QVBoxLayout()
        page1_v_box.addWidget(tab_pizza_label)
        page1_v_box.addWidget(desc_box)
        page1_v_box.addWidget(crust_gbox)
        page1_v_box.addWidget(toppings_gbox)
        page1_v_box.addStretch()
        page1_v_box.addWidget(add_to_order_button1, alignment=Qt.AlignRight)

        self.pizza_tab.setLayout(page1_v_box)

    def displayPizzaInOrder(self):
        pass    


    def loadImage(self, img_path):
        try:
            with open(img_path):
                image =QLabel(self)
                image.setObjectName("Image Info")
                pixmap = QPixmap(img_path)
                image.setPixmap(pixmap.scaled(image.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation))
                return image

        except FileNotFoundError:
            print("Image not found.")


    def sidedishTab(self):
        tab_side_label = QLabel("특가로 제공되든 사이드디시")
        tab_side_label.setObjectName("Header")
        desc_box = QWidget()
        desc_box.setObjectName("ImageBorder")
        side_image_path = "images/pasta.jpg"
        side_image = self.loadImage(side_image_path)
        side_desc = QLabel()
        side_desc.setObjectName("ImageInfo")
        side_desc.setText("모든 피자 주문시 모든 사이디디시 반값")
        side_desc.setWordWrap(True)

        h_box = QHBoxLayout()
        h_box.addWidget(side_image)
        h_box.addWidget(side_desc)

        desc_box.setLayout(h_box)

        side_gbox = QGroupBox()
        side_gbox.setTitle("사이드디시를 고르세요")

        self.side_group = QButtonGroup()
        gb_v_box = QVBoxLayout()
        side_list = ["씨푸드 로제 파스타", "웨스턴 핫윙", "허니&갈릭 윙스", "베이컨 까르보나라 페투치니", "치즈 볼로네즈 스파게티"]

        for side in side_list:
            side_rb = QRadioButton(side)
            gb_v_box.addWidget(side_rb)
            self.side_group.addButton(side_rb)

        self.side_group.setExclusive(False)

        side_gbox.setLayout(gb_v_box)

        add_to_order_button2 = QPushButton("Add to Order")
        add_to_order_button2.clicked.connect(self.displaySideInOrder)

        page2_v_box = QVBoxLayout()
        page2_v_box.addWidget(tab_side_label)
        page2_v_box.addWidget(desc_box)
        page2_v_box.addWidget(side_gbox)
        page2_v_box.addStretch()
        page2_v_box.addWidget(add_to_order_button2, alignment=Qt.AlignRight)

        self.sidedish_tab.setLayout(page2_v_box)

    def displaySideInOrder(self):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(style_sheet)
    window = FoodOrderGUI()
    sys.exit(app.exec_())