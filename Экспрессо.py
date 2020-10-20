import sys, sqlite3
from PyQt5.QtWidgets import QWidget, QApplication, QComboBox, QTableWidget, QLineEdit, QPushButton, QTableWidgetItem
from ui_table import Ui_Form


class Poisk(Ui_Form, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.con = sqlite3.connect('coffee.db')
        self.pushButton.clicked.connect(self.run)

    def run(self):

        f = """SELECT Sorts_cofee.ID,name,
            Degree_of_roasting.title AS degree,
            volum
            FROM Sorts_cofee 
            INNER JOIN Degree_of_roasting 
            ON Degree_of_roasting.id = Sorts_cofee.degree"""
        #print(f)
        try:
            cur = self.con.cursor()
            data = list(cur.execute(f).fetchall())
            print('*', data)
            print(len(data), data)
            self.tableWidget.setColumnCount(4)
            self.tableWidget.setHorizontalHeaderLabels(['id', 'name', 'degree', 'volum'])

            self.tableWidget.setRowCount(0)
            for i, row in enumerate(data):
                self.tableWidget.setRowCount(self.tableWidget.rowCount()+1)
                for j, el in enumerate(row):

                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(el)))
                    # selfprint(j, elem).tableWidget.resizeColumnsToContents()
        except BaseException as el:
            print(el)


if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)
        el = Poisk()
        el.show()
        sys.exit(app.exec_())
    except BaseException as el2:
        print('*',el2)
