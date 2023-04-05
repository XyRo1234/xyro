import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

import sys, os
from PyQt5.QtWidgets import *

import os 
import pathlib 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import random
import tensorflow as tf
from keras.preprocessing.image import ImageDataGenerator
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense, Conv2D, Flatten, Dropout, MaxPooling2D


GUI_FILE_NAME = 'gui_gragh'
os.system('python -m PyQt5.uic.pyuic -x ' + GUI_FILE_NAME + '.ui -o ' + GUI_FILE_NAME + '.py')
from gui_gragh import Ui_MainWindow
from pandasModel import *

class Form(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.df = pd.DataFrame()
        self.age_df = pd.DataFrame()
        self.index_df = pd.DataFrame()
        self.PG_df = pd.DataFrame()
        self.PT_df = pd.DataFrame()
        self.CG_df = pd.DataFrame()
        self.btnOpen.clicked.connect(self.openFile)
        self.btnLoad.clicked.connect(self.LoadImage)
        self.CB_age_group.activated.connect(self.func_age_group)
        self.CB_index_name.activated.connect(self.func_index_name)
        self.CB_product_group_name.activated.connect(self.func_product_group_name)
        self.CB_product_type_name.activated.connect(self.func_product_type_name)
        self.CB_colour_group_name.activated.connect(self.func_colour_group_name)
        
        print('Model 불러오는 중')
        self.model = tf.keras.models.load_model(r"D:\01_SW_Reskilling\00_Project\my_model")
        print('Model 불러오기 완료')

        self.top_100_details = pd.read_csv("./top_100_details.csv")
        print(' top_100_details 로드 완료')
        self.df_prices = pd.read_csv("./df_prices.csv")
        print(' df_prices 로드 완료')
        self.cust_details = pd.read_csv("./cust_details.csv")
        print(' cust_details 로드 완료')
        self.sold_qty_describe_df = pd.read_csv("./sold_qty_describe_df.csv")
        print(' sold_qty_describe_df 로드 완료')
        self.top_100_price_details = pd.read_csv("./top_100_price_details.csv")
        print(' top_100_price_details 로드 완료')
        self.worst_100_price_details = pd.read_csv("./worst_100_price_details.csv")
        print(' worst_100_price_details 로드 완료')
        self.worst_details = pd.read_csv("./worst_details.csv")
        print(' worst_details 로드 완료')
        self.load = pd.read_csv("./load.csv")
        print(' load 로드 완료')
        print('Ready')

        self.btn_sold_qty_describe.clicked.connect(self.sold_qty_describe)
        self.btn_Q1.clicked.connect(self.Q1)
        self.btn_Q1_2.clicked.connect(self.Q1_2)
        self.btn_Q2.clicked.connect(self.Q2)
        self.btn_Q2_2.clicked.connect(self.Q2_2)
        self.btn_Q3.clicked.connect(self.Q3)
        self.btn_Q3_2.clicked.connect(self.Q3_2)
        self.btn_Q4.clicked.connect(self.Q4)
        self.btn_Q4_2.clicked.connect(self.Q4_2)
        self.btn_Q4_3.clicked.connect(self.Q4_3)
        self.btn_def_cust_details.clicked.connect(self.def_cust_details)
        self.btn_Q5.clicked.connect(self.Q5)
        self.btn_Q6.clicked.connect(self.Q6)
        self.btn_Q7.clicked.connect(self.Q7)



    def openFile(self):
        file_name = 'load.csv'
        self.df = pd.read_csv(file_name)

        age_group = np.sort(self.df.age_group.unique())
        
        self.CB_age_group.setEnabled(True)
        self.CB_index_name.setEnabled(False)
        self.CB_product_group_name.setEnabled(False)
        self.CB_product_type_name.setEnabled(False)
        self.CB_colour_group_name.setEnabled(False)

        self.CB_age_group.clear()
        self.CB_age_group.addItem('항목을 선택해주세요')
        self.CB_age_group.addItems([str(x) for x in age_group])
        print('file opened')

    def func_age_group(self, index):
        if index==0: return
        age = self.CB_age_group.currentText()
        print('activate', index, age)
        # 콤보박스활성화
        self.CB_index_name.setEnabled(True)
        self.CB_product_group_name.setEnabled(False)
        self.CB_product_type_name.setEnabled(False)
        self.CB_colour_group_name.setEnabled(False)
        # 콤보박스 리스트 활성화
        self.age_df = self.df[self.df['age_group']==age].sort_values(by='count',ascending=False)
        index_name = np.sort(self.age_df.index_name.unique())
        self.CB_index_name.clear()
        self.CB_index_name.addItem('항목을 선택해주세요')
        self.CB_index_name.addItems([str(x) for x in index_name])

    def func_index_name(self, index):
        if index==0: return
        idx = self.CB_index_name.currentText()
        print('activate', index, idx)
        # 콤보박스활성화
        self.CB_product_group_name.setEnabled(True)
        self.CB_product_type_name.setEnabled(False)
        self.CB_colour_group_name.setEnabled(False)
        # 콤보박스 리스트 활성화
        self.index_df = self.age_df[self.age_df['index_name']==idx].sort_values(by='count',ascending=False)
        product_group_name = np.sort(self.index_df.product_group_name.unique())
        self.CB_product_group_name.clear()
        self.CB_product_group_name.addItem('항목을 선택해주세요')
        self.CB_product_group_name.addItems([str(x) for x in product_group_name])

    def func_product_group_name(self, index):
        if index==0: return
        pg = self.CB_product_group_name.currentText()
        print('activate', index, pg)
        # 콤보박스활성화
        self.CB_product_type_name.setEnabled(True)
        self.CB_colour_group_name.setEnabled(False)
        # 콤보박스 리스트 활성화
        self.PG_df = self.index_df[self.index_df['product_group_name']==pg].sort_values(by='count',ascending=False)
        product_type_name = np.sort(self.PG_df.product_type_name.unique())
        self.CB_product_type_name.clear()
        self.CB_product_type_name.addItem('항목을 선택해주세요')
        self.CB_product_type_name.addItems([str(x) for x in product_type_name])

    def func_product_type_name(self, index):
        if index==0: return
        PT = self.CB_product_type_name.currentText()
        print('activate', index, PT)
        # 콤보박스활성화
        self.CB_colour_group_name.setEnabled(True)
        # 콤보박스 리스트 활성화
        self.PT_df = self.PG_df[self.PG_df['product_type_name']==PT].sort_values(by='count',ascending=False)
        colour_group_name = np.sort(self.PT_df.colour_group_name.unique())
        self.CB_colour_group_name.clear()
        self.CB_colour_group_name.addItem('항목을 선택해주세요')
        self.CB_colour_group_name.addItems([str(x) for x in colour_group_name])

    def func_colour_group_name(self, index):
        if index==0: return
        CG = self.CB_colour_group_name.currentText()
        self.CG_df = self.PT_df[self.PT_df['colour_group_name']==CG].sort_values(by='count',ascending=False)
        article_id = np.sort(self.CG_df.article_id.unique())
        row, col = self.CG_df.shape
        print('행:',row,' 열:', col)
        print(self.CG_df)
        # print(article_id)
        if row>=3:
            prod_No1, prod_name1, price1 = self.CG_df.iat[0,0], self.CG_df.iat[0,1], self.CG_df.iat[0,2].round(2)
            prod_No2, prod_name2, price2 = self.CG_df.iat[1,0], self.CG_df.iat[1,1], self.CG_df.iat[1,2].round(2)
            prod_No3, prod_name3, price3 = self.CG_df.iat[2,0], self.CG_df.iat[2,1], self.CG_df.iat[2,2].round(2)
            print('1위:',prod_No1, prod_name1, price1,' 2위:',prod_No2, prod_name2, price2,' 3위:',prod_No3, prod_name3, price3)
        elif row==2:
            prod_No1, prod_name1, price1 = self.CG_df.iat[0,0], self.CG_df.iat[0,1], self.CG_df.iat[0,2].round(2)
            prod_No2, prod_name2, price2 = self.CG_df.iat[1,0], self.CG_df.iat[1,1], self.CG_df.iat[1,2].round(2)
            print('1위:',prod_No1, prod_name1, price1,' 2위:',prod_No2, prod_name2, price2)
        elif row==1:
            prod_No1, prod_name1, price1 = self.CG_df.iat[0,0], self.CG_df.iat[0,1], self.CG_df.iat[0,2].round(2)
            print('1위:',prod_No1, prod_name1, price1)
        else:
            print('No have item')
        self.drawDf(self.CG_df)

    def drawDf(self, df):
        model = pandasModel(df)
        self.tableView.setModel(model)

        self.tableView.resizeColumnsToContents()




    def sold_qty_describe(self):    # 판매 수량에 대한 요약 통계
        self.lbl_1.setText('')
        self.widget.fig.clear()
        self.widget.canvas.draw()
        s = ''
        for key, value in dict(self.sold_qty_describe_df["sold_qty"].describe()).items():
            if key=='count': key='제품종류'
            elif key=='mean': key='제품별 평균 판매수'
            elif key=='std': key='판매량 표준편차'
            elif key=='min': key='가장적은 판매량'
            elif key=='25%': key='제1사분위수(25%)'
            elif key=='50%': key='중위값(50%)'
            elif key=='75%': key='제3사분위수(75%)'
            elif key=='max': key='Top 1 제품 판매량'
            s += f"{key.ljust(12,' ')}: {value.round(1):,}\n"
        self.lbl_1.setText(s)

    # Q1 - Which are the TOP 100 articles in terms of sold quantity?
    def Q1(self):
        self.lbl_1.setText('')
        self.widget.fig.clear()
        ax = self.widget.fig.add_subplot(111)
    
        top_100_details = self.top_100_details

        top_30_sold_qty_qiantile = top_100_details.iloc[:30].groupby("prod_name")["sold_qty"].sum() \
                    .transform(lambda x: (x / x.sum() * 100)).rename('sold_qty(%)').reset_index().sort_values(by="sold_qty(%)", ascending=False)

        g = sns.barplot(top_30_sold_qty_qiantile, y="prod_name", x="sold_qty(%)", palette='ocean', ax=ax)
        for container in g.containers:
            print('container',container)
            g.bar_label(container, padding = 5, fmt='%.1f', fontsize=12)
        ax.set_title("TOP 30 most sold products", fontsize=20, fontweight="extra bold")
        ax.set_ylabel('')
        self.widget.fig.tight_layout()
        self.widget.canvas.draw()

    def Q1_2(self):
        self.lbl_1.setText('')

        top_100_details = self.top_100_details

        self.widget.fig.clear()
        ax = self.widget.fig.subplots(2,2)
        self.widget.fig.suptitle("TOP 100 most sold products characteristics", fontweight="bold",fontsize=25)    # Top 제목

        no=100

        data1 = top_100_details.iloc[:no].groupby("product_type_name")["sold_qty"].sum().transform(lambda x: (x / x.sum() * 100)).rename('sold_qty(%)').reset_index().sort_values(by="sold_qty(%)", ascending=False)
        data2 = top_100_details.iloc[:no].groupby("index_name")["sold_qty"].sum().transform(lambda x: (x / x.sum() * 100)).rename('sold_qty(%)').reset_index().sort_values(by="sold_qty(%)", ascending=False)
        data3 = top_100_details.iloc[:no].groupby("colour_group_name")["sold_qty"].sum().transform(lambda x: (x / x.sum() * 100)).rename('sold_qty(%)').reset_index().sort_values(by="sold_qty(%)", ascending=False)
        data4 = top_100_details.iloc[:no].groupby("product_group_name")["sold_qty"].sum().transform(lambda x: (x / x.sum() * 100)).rename('sold_qty(%)').reset_index().sort_values(by="sold_qty(%)", ascending=False)


        g = sns.barplot(data1, y="product_type_name", x="sold_qty(%)", ax=ax[0,0], palette="mako")
        for container in g.containers:
            g.bar_label(container, padding = 5, fmt='%.1f', fontsize=10, color="black")
        ax[0,0].set_ylabel("")
        ax[0,0].set_xlabel("Sold Quantity (%)", size=10, fontweight="bold")
        ax[0,0].set_title("Product Type",fontweight="bold",fontsize=15)
        ax[0,0].grid(axis="x",color = 'grey', linestyle = '--', linewidth = 1.5)
        

        g = sns.barplot(data2, y="index_name", x="sold_qty(%)", ax=ax[0,1], palette="viridis")
        for container in g.containers:
            g.bar_label(container, padding = 5, fmt='%.1f', fontsize=10, color="black")
        ax[0,1].set_ylabel("")
        ax[0,1].set_xlabel("Sold Quantity (%)", size=10, fontweight="bold")
        ax[0,1].set_title("Index",fontweight="bold",fontsize=15)
        ax[0,1].grid(axis="x",color = 'grey', linestyle = '--', linewidth = 1.5)


        g = sns.barplot(data3, y="colour_group_name", x="sold_qty(%)", ax=ax[1,0], palette="mako")
        for container in g.containers:
            g.bar_label(container, padding = 5, fmt='%.1f', fontsize=10, color="black")
        ax[1,0].set_ylabel("")
        ax[1,0].set_xlabel("Sold Quantity (%)", size=10, fontweight="bold")
        ax[1,0].set_title("Colour Group",fontweight="bold",fontsize=15)
        ax[1,0].grid(axis="x",color = 'grey', linestyle = '--', linewidth = 1.5)

        
        g = sns.barplot(data4, y="product_group_name", x="sold_qty(%)", ax=ax[1,1], palette="Reds_r")
        for container in g.containers:
            g.bar_label(container, padding = 5, fmt='%.1f', fontsize=10, color="black")
        ax[1,1].set_ylabel("")
        ax[1,1].set_xlabel("Sold Quantity (%)", size=10, fontweight="bold")
        ax[1,1].set_title("Product Group",fontweight="bold",fontsize=15)
        ax[1,1].grid(axis="x",color = 'grey', linestyle = '--', linewidth = 1.5)

        
        self.widget.fig.tight_layout()
        self.widget.canvas.draw()

    ## Q2 - Are there articles that have been sold only once?
    def Q2(self):
        self.lbl_1.setText('')
        self.widget.fig.clear()
        self.widget.canvas.draw()

        worst_details = self.worst_details

        count_of_only_once_sold = worst_details.value_counts('sold_qty').values[0]    # Count of products sold only once 한번만 팔린 제품수
        s = f"Count of products sold only once: {count_of_only_once_sold:,}"
        self.lbl_1.setText(s)


    def Q2_2(self):
        worst_details = self.worst_details

        count_of_only_once_sold = worst_details.value_counts('sold_qty').values[0]    # Count of products sold only once 한번만 팔린 제품수
        s = f"Count of products sold only once: {count_of_only_once_sold:,}"
        self.lbl_1.setText(s)

        self.widget.fig.clear()
        ax = self.widget.fig.subplots(2,2)
        self.widget.fig.suptitle("TOP 100 most earning products characteristics", fontweight="bold",fontsize=25)    # Top 제목

        no=100

        data1 = worst_details.iloc[:no].groupby("product_type_name")["sold_qty"].sum().transform(lambda x: (x / x.sum() * 100)).rename('sold_qty(%)').reset_index().sort_values(by="sold_qty(%)", ascending=False)
        data2 = worst_details.iloc[:no].groupby("index_name")["sold_qty"].sum().transform(lambda x: (x / x.sum() * 100)).rename('sold_qty(%)').reset_index().sort_values(by="sold_qty(%)", ascending=False)
        data3 = worst_details.iloc[:no].groupby("colour_group_name")["sold_qty"].sum().transform(lambda x: (x / x.sum() * 100)).rename('sold_qty(%)').reset_index().sort_values(by="sold_qty(%)", ascending=False)
        data4 = worst_details.iloc[:no].groupby("product_group_name")["sold_qty"].sum().transform(lambda x: (x / x.sum() * 100)).rename('sold_qty(%)').reset_index().sort_values(by="sold_qty(%)", ascending=False)

        g = sns.barplot(data1, y="product_type_name", x="sold_qty(%)", ax=ax[0,0],palette="viridis_r")
        for container in g.containers:
            g.bar_label(container, padding = 5, fmt='%.1f', fontsize=12, color="black")
        ax[0,0].set_ylabel("")
        ax[0,0].set_xlabel("Sold Quantity (%)", size=20, fontweight="bold")
        ax[0,0].set_title("Product Type", size=25, fontweight="bold")
        ax[0,0].grid(axis="x",color = 'grey', linestyle = '--', linewidth = 1.5)


        g = sns.barplot(data2, y="index_name", x="sold_qty(%)", ax=ax[0,1],palette="Reds_r")
        for container in g.containers:
            g.bar_label(container, padding = 5, fmt='%.1f', fontsize=15, color="black")
        ax[0,1].set_ylabel("")
        ax[0,1].set_xlabel("Sold Quantity (%)", size=20, fontweight="bold")
        ax[0,1].set_title("Index", size=25, fontweight="bold")
        ax[0,1].grid(axis="x",color = 'grey', linestyle = '--', linewidth = 1.5)

        
        g = sns.barplot(data3, y="colour_group_name", x="sold_qty(%)", ax=ax[1,0],palette="mako")
        for container in g.containers:
            g.bar_label(container, padding = 5, fmt='%.1f', fontsize=12, color="black")
        ax[1,0].set_ylabel("")
        ax[1,0].set_xlabel("Sold Quantity (%)", size=20, fontweight="bold")
        ax[1,0].set_title("Colour Group", size=25, fontweight="bold")
        ax[1,0].grid(axis="x",color = 'grey', linestyle = '--', linewidth = 1.5)

        
        g = sns.barplot(data4, y="product_group_name", x="sold_qty(%)", ax=ax[1,1],palette="Blues_r")
        for container in g.containers:
            g.bar_label(container, padding = 5, fmt='%.1f', fontsize=15, color="black")
        ax[1,1].set_ylabel("")
        ax[1,1].set_xlabel("Sold Quantity (%)", size=20, fontweight="bold")
        ax[1,1].set_title("Product Group", size=25, fontweight="bold")
        ax[1,1].grid(axis="x",color = 'grey', linestyle = '--', linewidth = 1.5)

        self.widget.fig.tight_layout()
        self.widget.canvas.draw()

    ## Q3 - Which are the TOP 100 articles that generated most earnings for the company?
    def Q3(self):
        df_prices = self.df_prices
        top_100_price_details = self.top_100_price_details

        s = ''
        for i in [10,50,100,200,300,400,1000]:  # TOP 100의 매출이 전체매출의 몇퍼센트를 차지하는지?
            s += f"The TOP {i} : {(df_prices['earning'].iloc[:i].sum() / df_prices['earning'].iloc[:].sum() * 100):.2f}% of total earnings\n"
        self.lbl_1.setText(s)


        self.widget.fig.clear()
        ax = self.widget.fig.add_subplot(111)
        self.widget.fig.suptitle("generated most earnings TOP50", fontweight="bold",fontsize=25)    # Top 제목


        data = top_100_price_details.iloc[:50].groupby('prod_name')['earning'].sum().transform(lambda x:x/x.sum()*100) \
        .rename('Earning (%)').reset_index().sort_values(by='Earning (%)',ascending=False)

        g = sns.barplot(data, x='Earning (%)', y='prod_name', palette='ocean', ax=ax)
        ax.set_xlabel('Earning (%)')
        ax.set_ylabel('')

        for container in ax.containers:
            ax.bar_label(container, padding = 5, fmt='%.1f', fontsize=10)

        self.widget.fig.tight_layout()
        self.widget.canvas.draw()

    def Q3_2(self):
        self.lbl_1.setText('')

        self.widget.fig.clear()
        ax = self.widget.fig.subplots(2,2)
        self.widget.fig.suptitle("generated most earnings TOP50 characteristics", fontweight="bold",fontsize=25)    # Top 제목

        df_prices = self.df_prices
        top_100_price_details = self.top_100_price_details

        no=100

        data1 = top_100_price_details.iloc[:no].groupby("product_type_name")["earning"].sum() \
        .transform(lambda x: (x / x.sum() * 100)).rename('earning(%)').reset_index().sort_values(by="earning(%)",ascending=False)
        data2 = top_100_price_details.iloc[:no].groupby("index_name")["earning"].sum() \
        .transform(lambda x: (x / x.sum() * 100)).rename('earning(%)').reset_index().sort_values(by="earning(%)", ascending=False)
        data3 = top_100_price_details.iloc[:no].groupby("colour_group_name")["earning"].sum() \
        .transform(lambda x: (x / x.sum() * 100)).rename('earning(%)').reset_index().sort_values(by="earning(%)", ascending=False)
        data4 = top_100_price_details.iloc[:no].groupby("product_group_name")["earning"].sum() \
        .transform(lambda x: (x / x.sum() * 100)).rename('earning(%)').reset_index().sort_values(by="earning(%)", ascending=False)


        g = sns.barplot(data1, y="product_type_name", x="earning(%)", ax=ax[0,0], palette="Blues_r")
        for container in g.containers:
            g.bar_label(container, padding = 5, fmt='%.1f', fontsize=14, color="black")
        ax[0,0].set_ylabel("")
        ax[0,0].set_xlabel("Earnings (%)", size=20,fontweight="bold")
        ax[0,0].set_title("Product Type", size=25,fontweight="bold")
        ax[0,0].grid(axis="x",color = 'grey', linestyle = '--', linewidth = 1.5)


        g = sns.barplot(data2, y="index_name", x="earning(%)", ax=ax[0,1], palette="viridis")
        for container in g.containers:
            g.bar_label(container, fmt='%.1f', padding = 5, fontsize=18, color="black")
        ax[0,1].set_ylabel("")
        ax[0,1].set_xlabel("Earnings (%)", size=20,fontweight="bold")
        ax[0,1].set_title("Index", size=25,fontweight="bold")
        ax[0,1].grid(axis="x",color = 'grey', linestyle = '--', linewidth = 1.5)


        g = sns.barplot(data3, y="colour_group_name", x="earning(%)", ax=ax[1,0],palette="mako")
        for container in g.containers:
            g.bar_label(container, padding = 5, fmt='%.1f', fontsize=18, color="black")
        ax[1,0].set_ylabel("")
        ax[1,0].set_xlabel("Earnings (%)", size=20,fontweight="bold")
        ax[1,0].set_title("Colour Group", size=25,fontweight="bold")
        ax[1,0].grid(axis="x",color = 'grey', linestyle = '--', linewidth = 1.5)


        g = sns.barplot(data4, y="product_group_name", x="earning(%)", ax=ax[1,1],palette="Reds_r")
        for container in g.containers:
            g.bar_label(container, fmt='%.1f', padding=5, fontsize=18, color="black")
        ax[1,1].set_ylabel("")
        ax[1,1].set_xlabel("Earnings (%)", size=20,fontweight="bold")
        ax[1,1].set_title("Product Group", size=25,fontweight="bold")
        ax[1,1].grid(axis="x",color = 'grey', linestyle = '--', linewidth = 1.5)

        self.widget.fig.tight_layout()
        self.widget.canvas.draw()

    ## Q4 - Which are articles that generated lower earnings for the company?
    def Q4(self):
        self.lbl_1.setText('')
        self.widget.fig.clear()
        self.widget.canvas.draw()

        df_prices = self.df_prices

        s = ''
        for i in [100,1000,10000,41000]:        # Worst 100의 매출이 전체매출의 몇퍼센트를 차지하는지?
            s += f"The Worst {i} : {100-(df_prices['earning'].iloc[:-i].sum()/df_prices['earning'].iloc[:].sum() * 100):.3f}% of total earnings\n"
        self.lbl_1.setText(s)

    def Q4_2(self):
        self.lbl_1.setText('')

        worst_100_price_details = self.worst_100_price_details

        self.widget.fig.clear()
        ax = self.widget.fig.subplots(2,1)
        self.widget.fig.suptitle("Worst 100 products characteristics", fontsize=25 ,fontweight="bold", y=1)

        no=100

        data1 = worst_100_price_details.iloc[:no].groupby("product_type_name")["earning"].sum() \
        .transform(lambda x: (x / x.sum() * 100)).rename('earning(%)').reset_index().sort_values(by="earning(%)", ascending=False)

        g = sns.barplot(data1, x="product_type_name", y="earning(%)", ax=ax[0],palette="mako")
        for container in g.containers:
            g.bar_label(container, fmt='%.1f', fontsize=10)
        ax[0].grid(axis="y",color = 'grey', linestyle = '--', linewidth = 1.5)
        ax[0].set_xlabel("")
        ax[0].set_ylabel("Earnings (%)", size=20,fontweight="bold")
        ax[0].set_xticklabels(g.get_xticklabels(), rotation=80)
        ax[0].set_title("Product Type", size=35,fontweight="bold")


        data2 = worst_100_price_details.iloc[:no].groupby("colour_group_name")["earning"].sum() \
        .transform(lambda x: (x / x.sum() * 100)).rename('earning(%)').reset_index().sort_values(by="earning(%)", ascending=False)

        g = sns.barplot(data2, x="colour_group_name", y="earning(%)", ax=ax[1],palette="mako")
        for container in g.containers:
            g.bar_label(container, fmt='%.1f', fontsize=10)
        ax[1].set_ylabel("Earnings (%)", size=20,fontweight="bold")
        ax[1].set_xlabel("")
        ax[1].set_xticklabels(g.get_xticklabels(), rotation=80)
        ax[1].set_title("Colour Group", size=35,fontweight="bold")
        ax[1].grid(axis="y",color = 'grey', linestyle = '--', linewidth = 1.5)

        self.widget.fig.tight_layout()
        self.widget.canvas.draw()

    def Q4_3(self):
        self.lbl_1.setText('')

        worst_100_price_details = self.worst_100_price_details

        self.widget.fig.clear()
        ax = self.widget.fig.subplots(2,1)
        self.widget.fig.suptitle("Worst 100 products characteristics (2)", fontsize=25 ,fontweight="bold", y=1)

        no=100

        data3 = worst_100_price_details.iloc[:no].groupby("index_name")["earning"].sum() \
        .transform(lambda x: (x / x.sum() * 100)).rename('earning(%)').reset_index().sort_values(by="earning(%)", ascending=False)

        g = sns.barplot(data3, y="index_name", x="earning(%)", ax=ax[0],palette="mako")
        for container in g.containers:
            g.bar_label(container, fmt='%.1f', fontsize=15)
        ax[0].set_ylabel("")
        ax[0].set_xlabel("Earnings (%)", size=20,fontweight="bold")
        ax[0].set_title("Index",size=35,fontweight="bold")
        ax[0].grid(axis="x",color = 'grey', linestyle = '--', linewidth = 1.2)


        data4 = worst_100_price_details.iloc[:no].groupby("product_group_name")["earning"].sum() \
        .transform(lambda x: (x / x.sum() * 100)).rename('earning(%)').reset_index().sort_values(by="earning(%)", ascending=False)

        g = sns.barplot(data4, y="product_group_name", x="earning(%)", ax=ax[1],palette="mako")
        for container in g.containers:
            g.bar_label(container, fmt='%.1f', fontsize=15)
        ax[1].set_ylabel("")
        ax[1].set_xlabel("Earnings (%)", size=20,fontweight="bold")
        ax[1].set_title("Product Group", size=35,fontweight="bold")
        ax[1].grid(axis="x",color = 'grey', linestyle = '--', linewidth = 1.5)
                    
        self.widget.fig.tight_layout()
        self.widget.canvas.draw()

    ## 고객별 총 구매금액
    def def_cust_details(self):
        self.lbl_1.setText('')
        self.widget.fig.clear()
        self.widget.canvas.draw()

        print(f"In total there are {len(self.cust_details)} different customers")
        self.lbl_1.setText(f"In total there are {len(self.cust_details):,} different customers")
    
    ## Q5 - Which age group purchase more articles?
    def Q5(self):
        self.lbl_1.setText('')
        self.widget.fig.clear()
        ax = self.widget.fig.add_subplot(111)
        self.widget.fig.suptitle("Purchased quantity rate by age group\n", fontsize=25 ,fontweight="bold")
        
        data = self.cust_details.groupby("age_groups")["article_id"].sum() \
        .transform(lambda x: (x / x.sum() * 100)).rename('Purchased Quantity(%)').reset_index()

        g = sns.barplot(data, x="age_groups", y="Purchased Quantity(%)", ax=ax) # edgecolor="black"
        ax.set_xlabel("Age Group",fontweight="bold", size=22)
        ax.set_ylabel("Purchased Quantity (%)",fontweight="bold", size=19)

        for container in g.containers:
            g.bar_label(container, padding = 5, fmt='%.1f', fontsize=18, color="black")
        ax.grid(axis="y",color = 'grey', linestyle = '--', linewidth = 1.5)  
        self.widget.fig.tight_layout()
        self.widget.canvas.draw()

    ## Q6 - Which age group generates more earnings for the company?
    def Q6(self):
        self.lbl_1.setText('')
        self.widget.fig.clear()
        ax = self.widget.fig.add_subplot(111)
        ax.set_title("Company Earnings rate by age group\n", fontweight="bold", size=28)

        data = self.cust_details.groupby("age_groups")["price"].sum().transform(lambda x: (x / x.sum() * 100)).rename('earning(%)').reset_index()

        g = sns.barplot(data, x="age_groups", y="earning(%)", ax=ax)
        ax.set_xlabel("Age Group",fontweight="bold", size=22)
        ax.set_ylabel("Earnings (%)",fontweight="bold", size=25)
        for container in g.containers:
            g.bar_label(container, padding = 5, fmt='%.1f', fontsize=18, color="black")
        ax.grid(axis="y",color = 'grey', linestyle = '--', linewidth = 1.5)
        self.widget.fig.tight_layout()
        self.widget.canvas.draw()
    
    ## Q7 - Does the club member status influence the purchased quantity?
    def Q7(self):
        self.lbl_1.setText('')
        cust_details = self.cust_details

        self.widget.fig.clear()
        ax = self.widget.fig.add_subplot(111)
        ax.set_title("Average Purchased Quantity by Club Member Status\n", fontweight="bold", size=22)

        data = cust_details.groupby("club_member_status")["article_id"].mean().astype(int).reset_index()

        g = sns.barplot(data, x="club_member_status", y="article_id", palette="viridis", edgecolor="black", ax=ax)

        ax.axhline(y = cust_details["article_id"].mean(), color = 'r', linestyle = '--')
        ax.text(0.76, 23.7, 'Mean Purchased Quantity: {:.0f}'.format(cust_details["article_id"].mean()), size=16, color="red",fontweight="bold")

        ax.set_xlabel("Club Member Status",fontweight="bold", size=20)
        ax.set_ylabel("Average Purchased Quantity",fontweight="bold", size=16)

        for container in g.containers:
            g.bar_label(container, padding = 5, fmt='%.0f', fontsize=23, color="black")

        ax.grid(axis="y",color = 'grey', linestyle = '--', linewidth = 1.5)
        self.widget.fig.tight_layout()
        self.widget.canvas.draw()


    def LoadImage(self):
        self.lbl_1.setText('')
        self.widget.fig.clear()
        ax = self.widget.fig.add_subplot(111)
        filepath, filter_type = QFileDialog.getOpenFileName(filter="jpg(*.jpg;*.jpeg);;모든 파일(*.*)", initialFilter="모든 파일(*.*)", directory=r".\0_images\List")
        if not filepath: return
        # 이미지 파일 경로 지정
        # file = r"D:\01_SW_Reskilling\00_Project\0_images\jeans\37.jpg"
        file = filepath

        def img_for_pred(img_path):
            img = tf.keras.utils.load_img(img_path, target_size=(240, 240))
            img = tf.keras.utils.img_to_array(img, dtype=np.uint8)
            img = np.array(img)/255.0
            return img

        g = img_for_pred(file)
        ax.imshow(g)
        ax.axis("off")
        self.widget.fig.tight_layout()
        self.widget.canvas.draw()

        
        p = self.model.predict(g[np.newaxis, ...])
        labels = {0:'Belt', 1:'Coat', 2:'Gloves', 3:'Jacket', 4:'Leggings', 5:'Shirt', 6:'Socks', 7:'Trousers', 8:'Vest top', 9:'shoes'}
        predicted_class = labels[np.argmax(p[0], axis=-1)]
        print("Classified:", predicted_class, "\n\n")
        self.lbl_1.setText(f"Recommend items similar to the picture! '{predicted_class}'")

        file_name = 'load.csv'
        categorical = pd.read_csv(file_name)

        if predicted_class=="Leggings": predicted_class = "Leggings/Tights"
        elif predicted_class=="shoes": predicted_class = "Flat shoes"

        test_df = categorical[categorical['product_type_name']==predicted_class].sort_values(by='count',ascending=False).iloc[:,0:3]
        test_df.reset_index(drop=True, inplace=True)
        test_df = test_df.reset_index(names='rank')
        test_df['rank'] = test_df['rank'].apply(lambda x: f"{int(x)+1}위")
        test_df = test_df.set_index('rank')
        self.drawDf(test_df)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec_())




