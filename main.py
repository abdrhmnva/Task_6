import sys
from PyQt6.QtWidgets import QApplication
from BMICalculator import BMICalculator

if __name__ == "__main__":
    print("Starting the application...")
    app = QApplication(sys.argv)
    bmi_calculator = BMICalculator()
    bmi_calculator.show()  # Показываем окно
    print("Window should be visible now.")
    sys.exit(app.exec())   # Запуск главного цикла

