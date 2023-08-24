import matplotlib.pyplot as plt

from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import pyqtSlot
from matplotlib.backends.backend_qtagg import FigureCanvas


class PieChartWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)

    @pyqtSlot(list)
    def update_data(self, income, expense):

        self.ax.clear()
        labels = ['Income', 'Expense']
        values = [income, expense]
        self.ax.pie(values,
                    labels=labels,
                    autopct='%1.1f%%',
                    startangle=(-90),
                    counterclock=False,
                    )

        # set the text color to white
        for text in self.ax.texts:
            text.set_color('white')

        self.ax.set_aspect('equal')
        self.figure.set_alpha(0.0)
        self.figure.set_facecolor('none')
        self.canvas.draw()
