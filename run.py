from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from random import randint
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
# create chrome instance
from selenium.webdriver.common.by import By

load_dotenv()

# get all variable from .env

MAIL_ID = os.getenv('MAIL_ID')
PASSWORD = os.getenv('PASSWORD')
MEET_LINK = os.getenv('MEET_LINK')

opt = Options()
opt.add_argument('--disable-blink-features=AutomationControlled')

opt.add_argument('--start-maximized')
opt.add_experimental_option("prefs", {
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 0,
    "profile.default_content_setting_values.notifications": 1
})
print(webdriver.Chrome)
driver = webdriver.Chrome(options=opt)
# driver = webdriver.Chrome(chrome_options=opt, executable_path=ChromeDriverManager().install())

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
    

def turnOffMicCam():
    # turn off Microphone
    time.sleep(1)
    driver.find_element(by=By.XPATH,
        value='//*[@id="yDmH0d"]/c-wiz/div/div/div[10]/div[3]/div/div[1]/div[4]/div/div/div[1]/div[1]/div/div[4]/div[1]').click()
    driver.implicitly_wait(10)

    # turn off camera
    time.sleep(1)
    driver.find_element(by=By.XPATH,
        value='//*[@id="yDmH0d"]/c-wiz/div/div/div[10]/div[3]/div/div[1]/div[4]/div/div/div[1]/div[1]/div/div[4]/div[2]').click()
    driver.implicitly_wait(10)
    
def joinNow():
    # Join meet
    print(1)
    time.sleep(1)
    driver.implicitly_wait(10)
    driver.find_element(by=By.XPATH,
        value='//*[@id="yDmH0d"]/c-wiz/div/div/div[10]/div[3]/div/div[1]/div[4]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/button').click()
    driver.implicitly_wait(10)
    print(1)

# assign email id and password

mail_address = MAIL_ID
password = PASSWORD


# login to Google account
Glogin(mail_address, password)

# go to google meet
driver.get(MEET_LINK)
turnOffMicCam()
joinNow()

driver.implicitly_wait(20)

# turn on Caption
try:
    wait = WebDriverWait(driver, 30)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.VfPpkd-Bz112c-LgbsSe.fzRBVc.tmJved.xHd4Cb.rmHNDe"))).click()
    print("google meets screen is diplayed.....")
except:
    print("google meets screen not displayed.....")
    driver.quit()

    
time.sleep(5)

"""
To get all HTML code of captions stored in file in every 2 sec sleep.
File name taken by generating random number from 0000, 9999
Breaking while loop after meeting got ended.
"""

random_name = randint(0000,9999)
file_name = f'{random_name}.txt'
auth_text = ''
while True:
   try:
        time.sleep(2)
        with open(file_name, "a") as file_object:
            if auth_text != driver.find_element(By.CSS_SELECTOR, "div.K6EKFb").get_attribute("innerHTML"):
                file_object.write(str(auth_text))
                file_object.write("\n")
            auth_text = driver.find_element(By.CSS_SELECTOR, "div.K6EKFb").get_attribute("innerHTML")
        
   except:
       break
 
"""
Use beautiful soup to get author name and messages from file.
stored author with message in list.

"""    
print(" after meeting ended")
list_chat = list()
with open(file_name, "rb") as file_data:
    for line in file_data.readlines():
        html_content = line.decode().strip()
        #
        bs4_content = BeautifulSoup(html_content,'html.parser')
        chatbox_html = bs4_content.find_all("div",class_="TBMuR bj4p3b")
        for chat in chatbox_html:
            temp_dict = dict()
            span_msg = chat.find("div", class_="zs7s8d jxFHg").decode_contents().strip()
            if span_msg:
                temp_dict["author"] = span_msg
                author_message = chat.find("div", class_="iTTPOb VbkSUe")
                if author_message:
                    temp_dict["message"] = author_message.text
                else:
                    temp_dict["message"] = ""
                list_chat.append(temp_dict)
           
           
"""
Logic implemented to avoid duplication of messages,
and stored in final list varible.

"""                
final_chat = list()
temp_dict = dict()
count = -1
for author_chat in list_chat:
    count += 1
    
    # To avoid dupilcation of author message which captured multiple times.
    if count >= 2 and author_chat['author']==list_chat[count-2].get('author'):
        temp_dict['author'] = author_chat['author']
        
        if list_chat[count-2].get('message').upper() in author_chat['message'].upper():
            temp_dict["message"][-1] = author_chat["message"]
            
            continue
        else:
            # temp_dict["message"].append(author_chat["message"])
            continue
        
    # To stored messsage in list and list stored in dict when author is different. 
    if temp_dict.get('author') != author_chat['author']:
        if temp_dict:
            temp_dict["message"] = "".join(temp_dict["message"])
            write_str = f"{temp_dict['author']} : {temp_dict['message']}\n"
            # print(write_str)
            final_chat.append(write_str)
        temp_dict = dict()
        temp_dict['author'] = author_chat['author']
        temp_dict['message'] = [author_chat['message']]
        continue
    
    # To avoid message is simillar to previous message of same author.    
    if temp_dict["message"][-1].upper() == author_chat["message"].upper():
        continue
    
    # To avoid some same message contains in new messages of same author. 
    elif len(temp_dict["message"][-1]) < len(author_chat["message"]):
        old_upper_message = temp_dict["message"][-1].upper()
        new_upper_message = author_chat["message"].upper()
        if old_upper_message in new_upper_message:
            temp_dict["message"][-1] = author_chat["message"]
        else:
            temp_dict["message"].append(author_chat["message"])
    
    # If above condition are not matching then avoid duplication of messages to previous.
    else:
        old_upper_message = temp_dict["message"][-1].upper()
        new_upper_message = author_chat["message"].upper()
        if new_upper_message in old_upper_message:
            continue
        else:
            temp_dict["message"].append(author_chat["message"])

# Write final messages in file with author name.
chat_file_name = f"CHAT_{file_name}"
with open(chat_file_name, "w+") as out_file:
    out_file.writelines(final_chat)
   