import matplotlib.pyplot as plt
from PyQt6.QtWidgets import QWidget, QVBoxLayout
from matplotlib.backends.backend_qtagg import FigureCanvas


class SemiCirclePieChartWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)

    def update_data(self, data):
        self.ax.clear()
        labels = ['Income', 'Expense']
        values = [sum(item[2] for item in data if item[5] == 'T'), 
                  sum(item[2] for item in data if item[5] == 'F')]
        self.ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90, counterclock=False)
        self.ax.set_theta_direction(-1)  # Make the pie chart clockwise
        self.ax.set_theta_offset(-90)  # Start the pie chart from the top
        self.ax.set_aspect('equal')
        self.canvas.draw()