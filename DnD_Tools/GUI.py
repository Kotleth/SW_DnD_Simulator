import copy
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLineEdit, \
    QPushButton, QDialog, QLabel, QComboBox, QCompleter, QTextBrowser, QHBoxLayout
from PySide6.QtCore import Signal, Slot, Qt

from additions import CharacterClassList
from character import UnitList, Unit

# units_by_id_dict: [int, Unit] = {}
team_1_dict: [int, Unit] = {}
team_2_dict: [int, Unit] = {}
team_1_list = []
team_2_list = []
occupied_id = 0


class BattleWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.new_team1_mate = None
        self.new_team2_mate = None

        self.team_1: list[Unit] = []
        self.team_2: list[Unit] = []

        self.setWindowTitle("Battle simulator")
        self.setGeometry(900, 100, 300, 400)

        layout = QVBoxLayout()

        # Create a dialog in the middle
        dialog = QDialog()
        dialog_layout = QVBoxLayout(dialog)

        self.battle_history = QTextBrowser(self)
        dialog_layout.addWidget(self.battle_history)
        self.battle_history.append("BATTLE STATUS:")

        dialog_buttons_layout = QHBoxLayout()

        # Team 1 append button
        append_member_team_1 = QPushButton("Append to team 1")
        dialog_buttons_layout.addWidget(append_member_team_1)
        append_member_team_1.clicked.connect(self.team_1_append)

        # Team 2 append button
        append_member_team_2 = QPushButton("Append to team 2")
        dialog_buttons_layout.addWidget(append_member_team_2)
        append_member_team_2.clicked.connect(self.team_2_append)

        dialog_layout.addLayout(dialog_buttons_layout)
        layout.addWidget(dialog)
        char_lists_layer = QHBoxLayout()

        # Combo box for choosing member for team
        self.team_combo = QComboBox()
        self.team_combo.addItems(list(UnitList.units_dict.keys()))

        start_battle_layout = QHBoxLayout()

        # Create button to start battle
        self.start_battle_button = QPushButton("Start battle")
        dialog_buttons_layout.addWidget(self.start_battle_button)
        self.start_battle_button.clicked.connect(self.start_battle)

        pop_buttons_layout = QHBoxLayout()

        # Team 1 remove button
        self.remove_member_team_1 = QPushButton("Pop team 1")
        dialog_buttons_layout.addWidget(self.remove_member_team_1)
        self.remove_member_team_1.clicked.connect(self.pop_team_1)

        # Team 2 remove button
        self.remove_member_team_2 = QPushButton("Pop team 2")
        dialog_buttons_layout.addWidget(self.remove_member_team_2)
        self.remove_member_team_2.clicked.connect(self.pop_team_2)

        pop_buttons_layout.addWidget(self.remove_member_team_1)
        pop_buttons_layout.addWidget(self.remove_member_team_2)
        dialog_layout.addLayout(pop_buttons_layout)

        char_lists_layer.addWidget(self.team_combo)
        dialog_layout.addLayout(char_lists_layer)

        start_battle_layout.addWidget(self.start_battle_button)
        dialog_layout.addLayout(start_battle_layout)

        self.setLayout(layout)

    def start_battle(self):
        print(team_1_list)
        print(team_2_list)
        print([x.name for x in self.team_1])
        print([x.name for x in self.team_2])

    def pop_team_1(self):
        if team_1_dict:
            self.battle_history.append(f"Remove from team 1: {team_1_dict.pop(max(team_1_dict.keys())).name}")
        else:
            self.battle_history.append("Team 1 is empty!")

    def pop_team_2(self):
        if team_2_dict:
            self.battle_history.append(f"Remove from team 2: {team_2_dict.pop(max(team_2_dict.keys())).name}")
        else:
            self.battle_history.append("Team 2 is empty!")
        # last_element = self.team_1.pop()
        # for key, value in team_1_dict.items():
        #     if
        #     units_by_id_dict[]

    def team_1_choose(self, index):
        self.new_team1_mate = self.team_combo.itemText(index)
        print(f"Selected item: {self.new_team1_mate}")

    def team_1_append(self):
        global occupied_id
        new_unit = copy.copy(UnitList.units_dict[self.team_combo.currentText()])
        self.team_1.append(new_unit)
        team_1_dict[occupied_id] = new_unit
        self.battle_history.append(f"\nAdded to team 1:\nId: {occupied_id}\tName: {team_1_dict[occupied_id].name}")
        team_1_list.append(occupied_id)
        occupied_id += 1

    def team_2_choose(self, index):
        self.new_team2_mate = self.team_combo.itemText(index)
        print(f"Selected item: {self.new_team2_mate}")

    def team_2_append(self):
        global occupied_id
        new_unit = copy.copy(UnitList.units_dict[self.team_combo.currentText()])
        self.team_2.append(new_unit)
        team_2_dict[occupied_id] = new_unit
        self.battle_history.append(f"\nAdded to team 2:\nId: {occupied_id}\tName: {team_2_dict[occupied_id].name}")
        team_2_list.append(occupied_id)
        occupied_id += 1


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
            window.action_browser.append(f"No such class as {self.text_inputs[1].text().lower().title()}")
            print(f"No such class as {self.text_inputs[1].text().lower().title()}")


class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.data_received = []
        self.char_creation_window = None
        self.battle_window = None

        self.setWindowTitle("D&D Simulator")
        self.setGeometry(100, 100, 400, 300)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        # Create a button to open the side window
        open_button = QPushButton("Open Character Creation", self)
        open_button.clicked.connect(self.open_character_creation)
        layout.addWidget(open_button)
        self.action_browser = QTextBrowser(self)
        layout.addWidget(self.action_browser)

        self.log_button = QPushButton("Open Battle Simulator", self)
        self.log_button.clicked.connect(self.log_action)
        layout.addWidget(self.log_button)

        central_widget.setLayout(layout)

    def open_character_creation(self):
        self.action_browser.append("Opened character creation")
        self.char_creation_window = CharacterWindow()
        self.char_creation_window.character_pass.connect(self.receive_character)
        self.char_creation_window.show()

    def log_action(self):
        self.action_browser.append("It's time to D-D-D-D-D-D-D-D-D-Duel!!!")
        self.battle_window = BattleWindow()
        self.battle_window.show()

    def receive_character(self, character_description):
        self.data_received = character_description
        CharacterClassList.character_classes_dict[self.data_received[0]] = self.data_received
        self.action_browser.append(f"Created a character named: {self.data_received[0]}")


def open_app():
    # TODO temporary solution.
    global window
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())
