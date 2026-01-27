import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout,
    QGroupBox, QSpacerItem, QSizePolicy
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
import requests


class PersonaApp(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Persona App")
        self.resize(800, 800)

        # Enable styled backgrounds so the wallpaper actually shows
        self.setObjectName("MainWindow")
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        # Main layout container
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(40, 40, 40, 40)
        main_layout.setSpacing(30)

        # Apply Persona-themed stylesheet
        self.setStyleSheet("""
        #MainWindow {
            background-image: url(bck.png);
            background-repeat: no-repeat;
            background-position: center;
        }

        QGroupBox {
            background-color: rgba(0, 0, 0, 80);   /* dark translucent panel */
            color: white;
            border: 2px solid #ff003c;
            border-radius: 10px;
            margin-top: 20px;
            font-size: 18px;
            font-weight: bold;
        }

        QGroupBox:title {
            subcontrol-origin: margin;
            left: 10px;
            padding: 4px 8px;
            background-color: rgba(0, 0, 0, 180);
            border-radius: 4px;
        }

        QLabel {
            background-color: transparent;
            color: white;
            font-size: 16px;
        }

        QLineEdit {
            background-color: rgba(255, 255, 255, 10);  /* semi-transparent */
            color: white;
            border: 2px solid #ff003c;
            border-radius: 6px;
            padding: 6px;
            font-size: 16px;
            font-weight: bold;
        }

        QTextEdit {
            background-color: rgba(255, 255, 255, 10);  /* semi-transparent */
            color: white;
            border: 2px solid #ff003c;
            border-radius: 6px;
            padding: 6px;
            font-size: 16px;
            font-weight: bold;
        }

        QTextEdit QWidget {
            background: transparent;
        }

        QPushButton {
            background-color: #ff003c;
            color: white;
            border-radius: 8px;
            padding: 10px 20px;
            font-size: 18px;
            font-weight: bold;
        }

        QPushButton:hover {
            background-color: #ff335c;
        }

        QPushButton:pressed {
            background-color: #cc002f;
        }
        """)

        # Title
        title = QLabel("Persona Comparison Tool")
        title.setFont(QFont("Arial", 24, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(title)

        # --- Input Group ---
        input_group = QGroupBox("Input Personas")
        input_layout = QVBoxLayout()
        input_layout.setSpacing(20)

        # Persona 1
        p1_row = QHBoxLayout()
        p1_label = QLabel("Persona 1:")
        p1_label.setFont(QFont("Arial", 14))
        self.persona1_input = QLineEdit()
        self.persona1_input.setFont(QFont("Arial", 14))
        p1_row.addWidget(p1_label)
        p1_row.addWidget(self.persona1_input)

        # Persona 2
        p2_row = QHBoxLayout()
        p2_label = QLabel("Persona 2:")
        p2_label.setFont(QFont("Arial", 14))
        self.persona2_input = QLineEdit()
        self.persona2_input.setFont(QFont("Arial", 14))
        p2_row.addWidget(p2_label)
        p2_row.addWidget(self.persona2_input)

        input_layout.addLayout(p1_row)
        input_layout.addLayout(p2_row)
        input_group.setLayout(input_layout)

        main_layout.addWidget(input_group)

        # Submit button
        self.submit_button = QPushButton("Submit")
        self.submit_button.setFont(QFont("Arial", 16))
        self.submit_button.setFixedHeight(50)
        self.submit_button.clicked.connect(self.on_submit)
        main_layout.addWidget(self.submit_button, alignment=Qt.AlignmentFlag.AlignCenter)

        # --- Result Group ---
        result_group = QGroupBox("Result")
        result_layout = QVBoxLayout()

        self.result_output = QTextEdit()
        self.result_output.setFont(QFont("Arial", 14))
        self.result_output.setReadOnly(True)

        # Make the internal viewport transparent
        self.result_output.viewport().setStyleSheet("background: transparent;")

        result_layout.addWidget(self.result_output)
        result_group.setLayout(result_layout)
        main_layout.addWidget(result_group)

        # Add stretch to center content vertically
        main_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        self.setLayout(main_layout)


    def on_submit(self):
        p1 = self.persona1_input.text()
        p2 = self.persona2_input.text()
        url = "http://127.0.0.1:5000/persona_fusion_calculator"
        params = { "persona1": p1, "persona2": p2 }
        response = requests.get(url, params=params)
        data = response.json()
        data = data["result"]
        # --- PLACEHOLDER FOR YOUR API CALL ---
        # Example:
        # response = requests.post("http://127.0.0.1:8000/endpoint", json={"p1": p1, "p2": p2})
        # result_text = response.json()["result"]

        result_text = (
            f"{data}\n"
        )

        self.result_output.setText(result_text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PersonaApp()
    window.show()
    sys.exit(app.exec())
