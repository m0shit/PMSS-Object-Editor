from PySide6.QtWidgets import (
    QApplication, QWidget, QPushButton, QVBoxLayout, QFileDialog, QListWidget, QLineEdit, QLabel, QHBoxLayout
)
import sys

class ObjectEditor(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sticker Star Object Editor")
        self.setGeometry(100, 100, 600, 400)

        # GUI elements
        self.layout = QVBoxLayout()
        self.load_button = QPushButton("Load Level File")
        self.object_list = QListWidget()
        self.x_input = QLineEdit()
        self.y_input = QLineEdit()
        self.save_button = QPushButton("Save Changes")

        # Layout
        self.layout.addWidget(self.load_button)
        self.layout.addWidget(self.object_list)
        
        coord_layout = QHBoxLayout()
        coord_layout.addWidget(QLabel("X:"))
        coord_layout.addWidget(self.x_input)
        coord_layout.addWidget(QLabel("Y:"))
        coord_layout.addWidget(self.y_input)
        self.layout.addLayout(coord_layout)

        self.layout.addWidget(self.save_button)
        self.setLayout(self.layout)

        # Connections
        self.load_button.clicked.connect(self.load_level_file)
        self.save_button.clicked.connect(self.save_changes)

    def load_level_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Level File", "", "All Files (*)")
        if file_path:
            print(f"Loaded file: {file_path}")
            # TODO: Parse level file and list objects
            self.object_list.addItem("ExampleObject1 (X: 10, Y: 20)")
            self.object_list.addItem("ExampleObject2 (X: 30, Y: 40)")

    def save_changes(self):
        # TODO: Save edited values back to the file
        print("Saving changes...")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    editor = ObjectEditor()
    editor.show()
    sys.exit(app.exec())
