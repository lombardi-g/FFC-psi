import sys
from scrape import run
from PySide6 import QtCore, QtWidgets, QtGui

# https://bigfive-test.com/pt-br/result/67b9e889b569922e5e0ab4f4
# result_code = "67b9e889b569922e5e0ab4f4"
# url = f'https://bigfive-test.com/pt-br/result/{result_code}'

class BigFiveMenu(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Big Five Results Reader')
        self.setWindowIcon(QtGui.QIcon("Figueirense.png"))
        self.instructions = QtWidgets.QLabel(f'Results ID:')
        self.url_input_box = QtWidgets.QLineEdit(self)
        self.confirm_button = QtWidgets.QPushButton(text="Confirm")
        self.response = QtWidgets.QLabel('')

        self.image_label = QtWidgets.QLabel(self)
        pixmap = QtGui.QPixmap("Figueirense.png").scaledToHeight(100)
        self.image_label.setPixmap(pixmap)
        # self.image_label.setFixedSize(100,100)
        self.image_label.setAlignment(QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.image_label)
        self.layout.addWidget(self.instructions)
        self.layout.addWidget(self.url_input_box)
        self.layout.addWidget(self.confirm_button, alignment=QtCore.Qt.AlignCenter)
        self.layout.addWidget(self.response)
        # self.setGeometry(500,200,200,200)

        self.confirm_button.clicked.connect(self.assert_and_return)
        self.url_input_box.returnPressed.connect(self.assert_and_return)

        self.show()
        
    @QtCore.Slot()
    def assert_and_return(self):
        try:
            run(self.url_input_box.text())
            self.response.setText("Ok") 
        except:
            self.response.setText("Error")

