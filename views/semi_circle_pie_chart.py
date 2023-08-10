import matplotlib.pyplot as plt
from math import fsum
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QApplication, QMainWindow
from PyQt6.QtCore import QObject, pyqtSignal, pyqtSlot
from matplotlib.backends.backend_qtagg import FigureCanvas
import sys


class SemiCirclePieChartWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)

    @pyqtSlot(list)
    def update_data(self, data):
        self.ax.clear()
        labels = ['Income', 'Expense']
        values = [fsum(item["amount"] for item in data if item["is_income"] == True),
                  fsum(item["amount"] for item in data if item["is_income"] == False)]
        print(values)
        self.ax.pie(values,
                    labels=labels,
                    autopct='%1.1f%%',
                    startangle=(-90),
                    counterclock=False,
                    )
        self.ax.set_aspect('equal')
        self.canvas.draw()

