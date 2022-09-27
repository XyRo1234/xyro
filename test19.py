from tkinter import * # __all__
from tkinter import filedialog
import tkinter as tk
from tkinter import PhotoImage, Button, Label, StringVar, ttk, colorchooser
import tkinter.ttk as ttk
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys
import re
import requests
from bs4 import BeautifulSoup as bs


root = Tk()
root.title("GSCS")



def start_1():
    id = ent1.get()
    print(id)
    pwd = ent2.get()
    otp = ent3.get()
    print(otp)
    url = 'https://gscs.lge.com/gscs/portal/main/portalMain.do;jsessionid=A586E72546416C5C9136AF3B9A09EBA0.gscs_14'

    url = 'https://sso.lge.com/'
    browser = webdriver.Ie('./IEDriverServer.exe')
    browser.get(url)
    browser.set_window_position(500,0)
    # browser.set_window_size(1020,600)

    browser.find_element_by_id("USER").send_keys(id)
    browser.find_element_by_id("LDAPPASSWORD").send_keys(pwd)
    browser.find_element_by_id("OTPPASSWORD").send_keys(otp)
    browser.find_element_by_id("loginSsobtn").click()   
    p = re.compile('http://newep.lge.com/portal/main/portalMain.do')
    WebDriverWait(browser, sys.maxsize).until(EC.presence_of_element_located((By.XPATH, '//*[@id="topLogo"]/h1/a/img')))

    url = 'https://gscs.lge.com/gscs/ssoLoginNew.do'
    browser.get(url)
    browser.find_element_by_xpath('//*[@id="topMenu"]/ul/li[3]/a/span').click()   # 매뉴얼 클릭
    time.sleep(1)
    res = requests.get(url)
    soup = bs(res.text, "html.parser")
    with open('gscs.html','w',encoding='utf-8') as file:
        file.write(soup)
    browser.find_element_by_xpath('//*[@id="1432869133120"]/a').click()
    browser.find_element_by_xpath('//*[@id="1432869133120"]/a').click()
    browser.find_element_by_xpath('//*[@id="1432869133120"]/a').click()
    browser.find_element_by_xpath('//*[@id="1432869133120"]/a').click()
    browser.find_element_by_xpath('//*[@id="1432869133120"]/a').click()

    print('wait')
    print('wait')







# ID 라벨
lab1 = Label(root)
lab1.config(text = "ID")
lab1.pack()

# ID 입력창
ent1 = Entry(root)
ent1.pack()

# Password 라벨
lab2 = Label(root)
lab2.config(text = "Password")
lab2.pack()

# Password 입력창
ent2 = Entry(root)
ent2.config(show = "*")
ent2.pack()

# OTP 라벨
lab3 = Label(root)
lab3.config(text = "OTP")
lab3.pack()

# ID 입력창
ent3 = Entry(root)
ent3.pack()


btn_close = Button(root, padx=5, pady=5, text="닫기", width=12, command=root.quit)
btn_close.pack(side="right", padx=5, pady=5)

btn_start = Button(root, padx=5, pady=5, text="시작", width=12, command=start_1)
btn_start.pack(side="right", padx=5, pady=5)


root.resizable(True, False) # x(너비), y(높이) 값 변경 불가 (창 크기 변경 불가)
root.mainloop()
