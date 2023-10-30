import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLineEdit, \
    QPushButton, QDialog, QLabel, QComboBox, QCompleter
from PySide6.QtCore import Signal, Slot, Qt
from additions import CharacterClassList


class CharacterWindow(QDialog):

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
                text_input.setFixedWidth(100)
                text_input.setFixedHeight(30)
            else:
                text_input = QLineEdit(self)
                if i == 1:
                    class_completer = QCompleter(CharacterClassList.character_classes_dict.keys())
                    class_completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
                    text_input.setCompleter(class_completer)
                self.text_inputs.append(text_input)
                layout.addWidget(label)
                layout.addWidget(text_input)
                text_input.setFixedWidth(200)
                text_input.setFixedHeight(30)

        button = QPushButton("Create", self)
        button.clicked.connect(self.character_create)
        layout.addWidget(button)

        self.setLayout(layout)

    def character_create(self):
        if self.text_inputs[1].text().lower() in CharacterClassList.character_classes_dict.keys():
            self.character_pass.emit([x.text() if type(x) == QLineEdit else x.currentText() for x in self.text_inputs])
        else:
            print(f"No such class as {self.text_inputs[1].text().lower().title()}")


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
        open_button.clicked.connect(self.open_character_creation)
        layout.addWidget(open_button)

        central_widget.setLayout(layout)

    def open_character_creation(self):
        self.side_window = CharacterWindow()
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
