from PyQt5.QtCore import *
from PyQt5.QtGui import QColor
import pandas as pd

class pandasModel(QAbstractTableModel):
    """Todo Pandas의 DataFrame을 위한 모델 생성"""
    def __init__(self, df=pd.DataFrame()):
        super().__init__()
        df = df.iloc[:,0:3]
        df.reset_index(drop=True, inplace=True)
        df = df.reset_index(names='rank')
        df['rank'] = df['rank'].apply(lambda x: f"{int(x)+1}위")
        self.df = df.set_index('rank')

    def rowCount(self, parent=None):
        """Todo DataFrame의 row 수 리턴"""
        return self.df.shape[0]

    def columnCount(self, index=None):
        """Todo DataFrame의 column수 리턴"""
        return self.df.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        """ Todo DataFrame의 index.row(), index.column()번째 데이터 리턴 """
        if not index.isValid():
            return QVariant()
        
        if role == Qt.DisplayRole or role == Qt.EditRole:
            return str(self.df.iloc[index.row(), index.column()])
        
        if role == Qt.ForegroundRole:
            if index.column()<=2:
                return QColor('red')
            elif index.column()>=4:
                return QColor('blue')

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        """
        Todo Header를 위해 DataFrame의 index/column의 section번째 데이터 리턴
        """
        if role != Qt.DisplayRole:
            return QVariant()

        if orientation == Qt.Horizontal:
            # print(f'section:{section}')
            return self.df.columns[section]
        elif orientation == Qt.Vertical:
            # print(f'section:{section}')
            return str(self.df.index[section])