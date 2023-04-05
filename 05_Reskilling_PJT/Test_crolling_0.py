import time, os, re
import requests
import urllib.request
import urllib.error
# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from PIL import Image
from PIL import UnidentifiedImageError

options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")
# service = ChromeService(executable_path=ChromeDriverManager().install())
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver = webdriver.Chrome(options=options)

driver.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&authuser=0&ogbl")
# driver.get("https://www.google.co.kr/search?q=%EC%BD%94%ED%8A%B8&sxsrf=AJOqlzXkXh-8STPXSHY6hT1CpvOVc7FFOg:1679032660680&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjS7biKpOL9AhVqSWwGHRJhDVsQ_AUoAXoECAEQAw")
# driver.get("https://www.lg.com/common/index.jsp")
# driver.get("https://www.selenium.dev/selenium/web/web-form.html")
title = driver.title

driver.implicitly_wait(0.5)
# driver.set_window_position(900,0)
# driver.set_window_size(1020,1080)
driver.set_window_position(0,0)
driver.set_window_size(1020,1080)

time.sleep(1)

search_words = ['Belt', 'Coat', 'Gloves', 'Jacket', 'Leggings/Tights', 'Shirt', 'shoes', 'Socks', 'Trousers', 'Vest top']  # ['Belt', 'Coat', 'Gloves', 'Jacket', 'Leggings/Tights', 'Shirt', 'shoes', 'Socks', 'Trousers', 'Vest top']
for search_word in search_words:

        
    elem = driver.find_element(By.NAME, "q")  # 검색탕의 검색엔진을 찾는 코드
    elem.clear()
    elem.send_keys(search_word)  # 해당 검색엔진에 글자를 입력
    elem.send_keys(Keys.RETURN)
    time.sleep(1)
    # 스크린샷 저장하기
    driver.save_screenshot('screenshot.png')




    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")  #브라우져 높이를 확인 가능(자바스크립트)
    t=0
    while t<10:      # 스크롤 횟수제한
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # 브라우져 끝까지 스크롤을 내리겠다.
        # Wait to load page
        time.sleep(1)  # 페이지 로딩 될 동안 웨잇
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:  # 스크롤이 끝까지 내려가서 더이상 내릴 것이 없을 때
            try:
                driver.find_element(By.CSS_SELECTOR, ".mye4qd").click()  # 검색어 더 찾아보기 클릭
            except:
                break
        last_height = new_height
        t +=1


    images = driver.find_elements(By.CSS_SELECTOR, ".rg_i.Q4LuWd")

    if search_word == "Leggings/Tights": search_word = "Leggings"
    folder_name = search_word
    #해당 이미지 이름과 동일한 폴더 생성
    if not os.path.isdir(folder_name):  # 없으면 새로 생성하는 조건문
        os.mkdir(folder_name)

    count = 1

    time.sleep(1)
    for i, image in enumerate(images,1):
        # html = driver.page_source
        # # HTML 파일로 저장하기
        # with open('html.html', 'w', encoding='utf-8') as f:
        #     f.write(html)

        # if i<=5: 
        #     count += 1
        #     continue

        if count > 100:  # 이미지 저장 수량 # #######################################################
            break

        try:
            image.click()
        except ElementClickInterceptedException:
            time.sleep(1)
            driver.execute_script( "arguments[0].click();" , image)
        time.sleep(1) 
        try:
            imgUrl = driver.find_element(By.XPATH, "/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div[2]/div/div[2]/div[2]/div[2]/c-wiz/div/div[2]/div[1]/a/img").get_attribute("src")
        except NoSuchElementException:
            imgUrl = driver.find_element(By.XPATH, "/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div[2]/div/div[2]/div[2]/div[2]/c-wiz/div/div[1]/div[2]/div[2]/div/a/img").get_attribute("src")

        print('imgUrl:',count,imgUrl)               
        
        if re.match(r'^data', imgUrl):
            print("imgUrl starts with 'data'")
            response = urllib.request.urlopen(imgUrl)
            with open(f"{folder_name}/{search_word}{str(count)}.jpg", 'wb') as f:
                f.write(response.file.read())
            with Image.open(f"{folder_name}/{search_word}{str(count)}.jpg") as img:
                # Resize the image to the desired size
                new_img = img.resize((240, 240))
                # Save the resized image to a new file
                new_img.save(f"{folder_name}/{search_word}{str(count)}.jpg")
            count = count + 1
            continue

        r = requests.get(imgUrl, headers={'User-Agent':'Mozilla/5.0'}, verify=False)

        with open(f"{folder_name}/{search_word}{str(count)}.jpg", "wb") as outfile:
            outfile.write(r.content)
        try:
            with Image.open(f"{folder_name}/{search_word}{str(count)}.jpg") as img:
                # Resize the image to the desired size
                new_img = img.resize((240, 240))
                # Save the resized image to a new file
                try:
                    new_img.save(f"{folder_name}/{search_word}{str(count)}.jpg")
                except OSError:
                    print('OSError : RGBA 이미지, jpg저장불가. RGB로 변경저장')
                    new_img = new_img.convert("RGB")
                    new_img.save(f"{folder_name}/{search_word}{str(count)}.jpg")
        except UnidentifiedImageError:
            print('UnidentifiedImageError: 깨진이미지 발생',count)
            os.remove(f"{folder_name}/{search_word}{str(count)}.jpg")
            count -= 1
            
        count = count + 1

    driver.back()
driver.close()

