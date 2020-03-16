import sys

from PySide2.QtCore import Slot
from PySide2.QtGui import QKeySequence
from PySide2.QtWidgets import QApplication, QLabel, QMainWindow, QAction, QWidget, QTableWidget, QHeaderView, \
    QHBoxLayout, QTableWidgetItem, QLineEdit, QPushButton, QVBoxLayout


class Window(QMainWindow):

    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.setWindowTitle("Otherwhere Generator")
        self.setCentralWidget(parent)

        # menu
        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu("File")

        # Exit
        exit_action = QAction("Exit", self)
        exit_action.setShortcut(QKeySequence.Quit)
        exit_action.triggered.connect(self.exit_app)

        self.file_menu.addAction(exit_action)

    @Slot()
    def exit_app(self, checked):
        QApplication.quit()


class Widget(QWidget):

    def __init__(self):
        super().__init__()
        self.items = 0

        # Example data
        self._data = {"Water": 24.5, "Electricity": 55.1, "Rent": 850.0,
                      "Supermarket": 230.4, "Internet": 29.99, "Bars": 21.85,
                      "Public transportation": 60.0, "Coffee": 22.45, "Restaurants": 120}

        # Left
        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["Description", "Price"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # QWidget Layout
        self.layout = QHBoxLayout()

        # self.table_view.setSizePolicy(size)
        self.layout.addWidget(self.table)

        # Set the layout to the QWidget
        self.setLayout(self.layout)

        # Fill example data
        self.fill_table()

        # Right
        self.description = QLineEdit()
        self.price = QLineEdit()
        self.add = QPushButton("Add")
        self.clear = QPushButton("Clear")
        self.quit = QPushButton("Quit")

        self.right = QVBoxLayout()
        self.right.setMargin(10)
        self.right.addWidget(QLabel("Description"))
        self.right.addWidget(self.description)
        self.right.addWidget(QLabel("Price"))
        self.right.addWidget(self.price)
        self.right.addWidget(self.add)
        self.right.addStretch()
        self.right.addWidget(self.clear)
        self.right.addWidget(self.quit)

        self.layout.addLayout(self.right)

    def fill_table(self, data=None):
        data = self._data if not data else data
        for desc, price in data.items():
            self.table.insertRow(self.items)
            self.table.setItem(self.items, 0, QTableWidgetItem(desc))
            self.table.setItem(self.items, 1, QTableWidgetItem(str(price)))
            self.items += 1


app = QApplication(sys.argv)
widget = Widget()
window = Window(widget)

window.resize(800, 600)
window.show()

sys.exit(app.exec_())
