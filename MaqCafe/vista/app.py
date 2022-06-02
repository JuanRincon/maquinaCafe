from curses import window
from PySide2.QtWidgets import QApplication
from controlador.main_window import ListCoffeWindow


if __name__ == "__main__":
    app = QApplication()
    window = ListCoffeWindow()
    window.show()

    app.exec_()

