from PyQt5.QtCore import *
from PyQt5.QtGui import QColor
import pandas as pd


class pandasModel(QAbstractTableModel):
    """
    Todo Pandas의 DataFrame을 위한 모델 생성
    """

    def __init__(self, df=pd.DataFrame()):
        super().__init__()
        self.df = df

    def rowCount(self, parent=None):
        """
        Todo DataFrame의 row 수 리턴
        """
        return self.df.shape[0]

    def columnCount(self, index=None):
        """
        Todo DataFrame의 column수 리턴
        """
        return self.df.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        """
        Todo DataFrame의 index.row(), index.column()번째 데이터 리턴
        """
        if not index.isValid():
            return QVariant()
        
        if role == Qt.DisplayRole or role == Qt.EditRole:
            return str(self.df.iloc[index.row(), index.column()])
        
        if role == Qt.ForegroundRole:
            if index.column()<=2:
                return QColor('red')
            elif index.column()>=4:
                return QColor('blue')


    def flags(self, index):
        return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable


    def setData(self, index, value, role):
        """
        Todo Editable model을 위해 작성, DataFrame의 index.row(), index.column()위치에 value 대입
        """
        if not index.isValid():
            return False
        if role == Qt.EditRole:
            self.df.iloc[index.row(), index.column()] = value
            self.dataChanged.emit(index, index)
            return True
        return False


    def headerData(self, section, orientation, role=Qt.DisplayRole):
        """
        Todo Header를 위해 DataFrame의 index/column의 section번째 데이터 리턴
        """
        if role != Qt.DisplayRole:
            return QVariant()

        if orientation == Qt.Horizontal:
            print(f'section:{section}')
            return self.df.columns[section]
        elif orientation == Qt.Vertical:
            print(f'section:{section}')
            return str(self.df.index[section])
