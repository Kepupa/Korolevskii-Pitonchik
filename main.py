import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel

class ClickerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.click_count = 0

        self.label = QLabel(f"Clicks: {self.click_count}", self)
        self.button = QPushButton("Click me", self)
        
        self.button.clicked.connect(self.increment_clicks)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        
        self.setLayout(layout)
        
        self.setWindowTitle('simple clicker')
        self.setGeometry(100, 100, 300, 200)
        self.show()

    def increment_clicks(self):
        self.click_count += 1
        self.label.setText(f"Clicks: {self.click_count}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ClickerApp()
    sys.exit(app.exec_())