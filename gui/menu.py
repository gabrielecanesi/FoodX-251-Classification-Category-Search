from PyQt6 import QtWidgets, uic
from gui.search import SearchWindow
from gui.classification_gui import ClassificationWindow


class MainMenu(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.classification_window = None
        self.search_window = None
        uic.loadUi('gui/main.ui', self)
        self.button_similarity = self.findChild(QtWidgets.QPushButton, 'buttonSearch')
        self.button_classification = self.findChild(QtWidgets.QPushButton, 'buttonClassification')
        self.button_similarity.clicked.connect(self.similarity_clicked)
        self.button_classification.clicked.connect(self.classification_clicked)
        self.label_loading = self.findChild(QtWidgets.QLabel, 'labelLoading')
        self.show()

    def similarity_clicked(self):
        self.label_loading.setText("Caricamento dei modelli...")
        self.repaint()
        self.search_window = SearchWindow()
        self.search_window.show()
        self.label_loading.setText("")

    def classification_clicked(self):
        self.classification_window = ClassificationWindow()
        self.classification_window.show()
