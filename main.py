import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel

class ClickerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Инициализируем количество кликов
        self.click_count = 0

        # Создаем элементы интерфейса
        self.label = QLabel(f"Clicks: {self.click_count}", self)
        self.button = QPushButton("Click me", self)
        
        # Соединяем сигнал от кнопки с функцией увеличения кликов
        self.button.clicked.connect(self.increment_clicks)
        
        # Создаем макет
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        
        self.setLayout(layout)
        
        # Настроим окно
        self.setWindowTitle('simple clicker')
        self.setGeometry(100, 100, 300, 200)
        self.show()

    def increment_clicks(self):
        # Увеличиваем количество кликов и обновляем текст на лейбле
        self.click_count += 1
        self.label.setText(f"Clicks: {self.click_count}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ClickerApp()
    sys.exit(app.exec_())