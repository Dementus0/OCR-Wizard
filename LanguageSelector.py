import sys
from PyQt5.QtWidgets import QApplication, QWidget,QVBoxLayout, QCheckBox, QPushButton, QLabel
from Wizard import Wizard

class LanguageSelector(QWidget):
    def __init__(self, FileSelector=None):
        super().__init__()    
        self.FileSelector = FileSelector
        self.setWindowTitle('OCR Wizard')
        self.setGeometry(100, 100, 1000, 600)
        self.languages = ["English", "Traditional Chinese", "Simplified Chinese", "German", "Japanese"]
        self.languages_name = ["English", "繁體中文", "简体中文", "Deutsch", "日本語"]
        self.languages_code = ["eng", "chi_tra", "chi_sim", "deu", "jpn"]

        # Create checkboxes for different languages
        self.language_checkboxes = []
        for language_name in self.languages_name:
            checkbox = QCheckBox(language_name, self)
            self.language_checkboxes.append(checkbox)
        
        # Create a label for instructions
        self.word_label = QLabel('Please select the languages in the document', self)

        # Create a button to select a file and Start OCR
        self.ocr_button = QPushButton('Start OCR', self)

        # Create a layout to add checkboxes and the buttons
        layout = QVBoxLayout()

        # Add the checkboxes to the layout
        layout.addWidget(self.word_label)
        for checkbox in self.language_checkboxes:
            layout.addWidget(checkbox)   
        layout.addWidget(self.ocr_button)

        # Set the layout for the main window
        self.setLayout(layout)

        # Connect the buttons to their respective functions
        self.ocr_button.clicked.connect(self.start_ocr)

    def language_selected(self):
        self.selected_languages = []
        for idx, checkbox in enumerate(self.language_checkboxes):
            if checkbox.isChecked():
                self.selected_languages.append(self.languages_code[idx])
        return        

    def start_ocr(self):
        # check the selected languages
        self.language_selected()

        # check if at least one language is selected
        if len(self.selected_languages) == 0:
            self.word_label.setText("[ERROR] Please select at least one language.")
            return
        
        # close this window
        self.close()

        # Open the language selector window and pass a reference to self
        self.progress_window = Wizard(self)
        self.progress_window.show()
        return

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LanguageSelector()
    window.show()
    sys.exit(app.exec_())