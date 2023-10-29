import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLineEdit, \
    QPushButton, QDialog, QLabel, QComboBox
from PySide6.QtCore import Signal, Slot


class SideWindow(QDialog):

    character_pass = Signal(list)

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Character creation")
        self.setGeometry(500, 100, 400, 300)

        layout = QVBoxLayout()

        # Create 9 text input boxes
        char_stats = ['NAME', 'CLASS', 'LVL', 'STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA']
        self.text_inputs = []
        for i in range(9):
            label = QLabel(char_stats[i], self)
            if i in range(2, 10):
                text_input = QComboBox(self)
                self.text_inputs.append(text_input)
                layout.addWidget(label)
                layout.addWidget(text_input)
                if char_stats[i] == 'LVL':
                    for j in range(1, 21):
                        text_input.addItem(str(j))
                else:
                    for j in range(1, 31):
                        text_input.addItem(str(j))
                    text_input.setCurrentText(str(10))
                text_input.setFixedWidth(100)  # Set the width to 200 pixels
                text_input.setFixedHeight(30)
            else:
                text_input = QLineEdit(self)
                self.text_inputs.append(text_input)
                layout.addWidget(label)
                layout.addWidget(text_input)
                text_input.setFixedWidth(200)  # Set the width to 200 pixels
                text_input.setFixedHeight(30)

        # Create a push button
        button = QPushButton("Create", self)
        button.clicked.connect(self.character_create)
        layout.addWidget(button)

        self.setLayout(layout)

    def character_create(self):
        # for i, text_input in enumerate(self.text_inputs):
        #     text = text_input.text()
        #     print(f"Box {i + 1}: {text}")
        self.character_pass.emit([x.text() if type(x) == QLineEdit else x.currentText() for x in self.text_inputs])


class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.data_received = []
        self.side_window = None

        self.setWindowTitle("Main Window")
        self.setGeometry(100, 100, 400, 300)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        # Create a button to open the side window
        open_button = QPushButton("Open Side Window", self)
        open_button.clicked.connect(self.open_side_window)
        layout.addWidget(open_button)

        central_widget.setLayout(layout)

    def open_side_window(self):
        self.side_window = SideWindow()
        self.side_window.character_pass.connect(self.receive_character)
        self.side_window.show()

    def receive_character(self, character_description):
        self.data_received = character_description

        print("XDD")
        print(self.data_received)
        print("XDD")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())
