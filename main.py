import sys
from PyQt5.QtWidgets import QApplication
from FileSelector import FileSelector

def main():
    app = QApplication(sys.argv)
    window = FileSelector()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()