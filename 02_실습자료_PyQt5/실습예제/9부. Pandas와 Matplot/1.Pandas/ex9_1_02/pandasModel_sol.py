from PyQt5.QtCore import *
import pandas as pd
from PyQt5.QtGui import QColor


class pandasModel(QAbstractTableModel):
    def __init__(self, df=pd.DataFrame()):
        super().__init__()
        self.df = df

    def rowCount(self, parent=None):
        return self.df.shape[0]

    def columnCount(self, index=None):
        return self.df.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return QVariant()
        if role == Qt.DisplayRole or role == Qt.EditRole:
            return str(self.df.iloc[index.row(), index.column()])

        if role == Qt.ForegroundRole:
            value = self.df.iloc[index.row(), 5]
            if value >= 4:
                return QColor('blue')
            elif value <= 2:
                return QColor('red')
        return QVariant()
    
    def flags(self, index):
        return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable

    def setData(self, index, value, role):
        if not index.isValid():
            return False
        if role == Qt.EditRole:
            self.df.iloc[index.row(), index.column()] = value
            self.dataChanged.emit(index, index)
            return True
        return False

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role != Qt.DisplayRole:
            return QVariant()

        if orientation == Qt.Horizontal:

            return self.df.columns[section]
        elif orientation == Qt.Vertical:
            return str(self.df.index[section])
