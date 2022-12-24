import subprocess
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    @staticmethod
    def shutdown(*args):
        # Use subprocess.run to call the shutdown command with the given arguments
        subprocess.run(['powershell', 'shutdown'] + list(args))

    def init_ui(self):
        # Create a horizontal layout
        layout = QHBoxLayout()

        # Create four buttons
        button1 = QPushButton('10 minutes', self)
        button2 = QPushButton('30 minutes', self)
        button3 = QPushButton('60 minutes', self)
        button4 = QPushButton('Cancel', self)

        # Connect buttons with logic
        button1.clicked.connect(lambda: self.shutdown('-s', '-t', '600'))
        button2.clicked.connect(lambda: self.shutdown('-s', '-t', '1800'))
        button3.clicked.connect(lambda: self.shutdown('-s', '-t', '3600'))
        button4.clicked.connect(lambda: self.shutdown('-a'))

        # Add the buttons to the layout
        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)
        layout.addWidget(button4)

        # Set the layout as the central widget of the window
        self.setLayout(layout)

        # Set the window properties
        self.setGeometry(300, 300, 250, 50)
        self.setWindowTitle('Shutdown App')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    ex = MyApp()
    sys.exit(app.exec_())
