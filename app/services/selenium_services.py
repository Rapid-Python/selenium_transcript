from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from random import randint

# create chrome instance
from selenium.webdriver.common.by import By
from extension import MAIL_ID, PASSWORD, MEET_LINK
from app.helper.selenium_helper import  *
from app.services.bs_four import get_message_author_from_bsfour, evaluate_message, final_messages_in_text

driver = driver_installtion()
def Glogin(mail_address, password):
    # Login Page
    
    driver.get(
        'https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=https://www.google.com/&ec=GAZAmgQ'
    )

    # input Gmail

    driver.find_element(By.ID, "identifierId").send_keys(mail_address)
    driver.find_element(By.ID, "identifierNext").click()
    driver.implicitly_wait(10)

    # input Password
    driver.find_element(
        "xpath", '//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)
    driver.implicitly_wait(10)
    driver.find_element(By.ID,"passwordNext").click()

    # go to google home page
    driver.get('https://google.com/')
    time.sleep(1)
    # go to google meet
    driver.get(MEET_LINK)
    
 # turn off Microphone and camera
def turnOffMicCam():
    
    # driver = driver_installtion()
    time.sleep(1)
    driver.find_element(by=By.XPATH,
        value='//*[@id="yDmH0d"]/c-wiz/div/div/div[10]/div[3]/div/div[1]/div[4]/div/div/div[1]/div[1]/div/div[4]/div[1]').click()
    driver.implicitly_wait(10)

    time.sleep(1)
    driver.find_element(by=By.XPATH,
        value='//*[@id="yDmH0d"]/c-wiz/div/div/div[10]/div[3]/div/div[1]/div[4]/div/div/div[1]/div[1]/div/div[4]/div[2]').click()
    driver.implicitly_wait(10)
    
 # Join meet    
def joinNow():
   
    # driver = driver_installtion()
    time.sleep(1)
    driver.implicitly_wait(10)
    driver.find_element(by=By.XPATH,
        value='//*[@id="yDmH0d"]/c-wiz/div/div/div[10]/div[3]/div/div[1]/div[4]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/button').click()
    driver.implicitly_wait(20)


# turn on Caption
def turn_on_caption():
    # driver = driver_installtion()
    try:
        wait = WebDriverWait(driver, 30)
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.VfPpkd-Bz112c-LgbsSe.fzRBVc.tmJved.xHd4Cb.rmHNDe"))).click()
        print("google meets screen is diplayed.....")
    except:
        print("google meets screen not displayed.....")
        driver.quit()
        
def start_driver():
    # driver = driver_installtion()
    
    # assign email id and password
    mail_address = MAIL_ID
    password = PASSWORD


    # login to Google account
    Glogin(mail_address, password)

    
    turnOffMicCam()
    joinNow()

    # driver.implicitly_wait(20)
    turn_on_caption()
        
    time.sleep(2)
    
"""
To get all HTML code of captions stored in file in every 2 sec sleep.
File name taken by generating random number from 0000, 9999
Breaking while loop after meeting got ended.
"""
def capture_captions():
    # driver = driver_installtion
    start_driver()
    time.sleep(5)
    random_name = randint(0000,9999)
    file_name = f'{random_name}.txt'
    auth_text = ''
    is_exception = 0
    while True:
        if is_exception == 1:
            break
        try:
                time.sleep(2)
                with open(file_name, "a") as file_object:
                    if auth_text != driver.find_element(By.CSS_SELECTOR, "div.K6EKFb").get_attribute("innerHTML"):
                        file_object.write(str(auth_text))
                        file_object.write("\n")
                    auth_text = driver.find_element(By.CSS_SELECTOR, "div.K6EKFb").get_attribute("innerHTML")
                
        except:
            is_exception = 1    
            # break
    
    list_of_messages = get_message_author_from_bsfour(file_name) 
    evaluate_message(list_of_messages)
    final_messages_in_text(file_name)
    return "successfully messages imported."
    