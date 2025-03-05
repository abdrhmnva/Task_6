from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMenuBar, QMenu
from PyQt6.QtGui import QAction  # Переносим импорт QAction сюда
from PyQt6.QtGui import QAction, QFont  # Добавляем QFont

class BMICalculator(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("BMI Calculator")
        self.setGeometry(100, 100, 300, 200)

        # Главное окно
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Поля ввода
        self.weight_label = QLabel("Weight (kg):")
        self.weight_input = QLineEdit()

        self.height_label = QLabel("Height (m):")
        self.height_input = QLineEdit()

        # Кнопка расчета
        self.calculate_button = QPushButton("Calculate BMI")
        self.calculate_button.clicked.connect(self.calculate_bmi)

        # Вывод результата
        self.result_label = QLabel("")
        self.result_label.setFont(QFont("Arial", 12))

        # Размещение элементов
        layout = QVBoxLayout()
        layout.addWidget(self.weight_label)
        layout.addWidget(self.weight_input)
        layout.addWidget(self.height_label)
        layout.addWidget(self.height_input)
        layout.addWidget(self.calculate_button)
        layout.addWidget(self.result_label)

        self.central_widget.setLayout(layout)

        # Меню
        self.create_menu()

    def create_menu(self):
        menubar = self.menuBar()

        # Меню File
        file_menu = menubar.addMenu("File")

        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        clear_action = QAction("Clear", self)
        clear_action.triggered.connect(self.clear_fields)
        file_menu.addAction(clear_action)

        # Меню Help
        help_menu = menubar.addMenu("Help")

        help_action = QAction("How to use", self)
        help_action.triggered.connect(self.show_help)
        help_menu.addAction(help_action)

    def calculate_bmi(self):
        try:
            weight = float(self.weight_input.text())
            height = float(self.height_input.text())

            if height <= 0:
                self.result_label.setText("Height must be > 0")
                return

            bmi = weight / (height ** 2)
            status = self.get_bmi_status(bmi)

            self.result_label.setText(f"BMI: {bmi:.2f} ({status})")

        except ValueError:
            self.result_label.setText("Invalid input")

    def get_bmi_status(self, bmi):
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 25:
            return "Normal"
        elif 25 <= bmi < 30:
            return "Overweight"
        else:
            return "Obese"

    def clear_fields(self):
        self.weight_input.clear()
        self.height_input.clear()
        self.result_label.clear()

    def show_help(self):
        self.result_label.setText("Enter weight in kg and height in meters.\nClick 'Calculate BMI'.")

