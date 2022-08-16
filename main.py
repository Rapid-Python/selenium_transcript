from bs4 import BeautifulSoup

list_chat = list()
with open("output/DEMO_4534.txt","rb") as file_data:
    for line in file_data.readlines():
        # temp_dict = dict()
        html_content = line.decode().strip()
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
           
                # print(temp_dict)
                
# print(list_chat)
       
# exit()   

final_chat = list()
def final_message(count, temp_dict):
    # pass
     if temp_dict:
        temp_dict['message'] = temp_dict['message'].strip()
        if not temp_dict['message']:
            pass
        else:
            print("temp_dict['message']: ", temp_dict['message'])
            if temp_dict['message'][0].isalpha():
                pass
            else:
                temp_dict['message'] = temp_dict['message'][1:]
           
            if count > 1:
                print(final_chat[-1])
                get_author_len = final_chat[-1].find(" : ")
                get_author_from_final_chat = final_chat[-1][0:get_author_len]
                if temp_dict['author'] == get_author_from_final_chat:
                    # pass
                    get_message_from_final_chat = final_chat[-1][get_author_len+2:]
                    
                    del final_chat[-1]
                    temp_dict['message'] = get_message_from_final_chat.strip() +" "+temp_dict['message'].strip()
                    write_str = f"{temp_dict['author']} : {temp_dict['message']}\n\n"
                else:  
                    write_str = f"{temp_dict['author']} : {temp_dict['message']}\n\n"
            else:  
                write_str = f"{temp_dict['author']} : {temp_dict['message']}\n\n"
                
            if temp_dict['message']:
                final_chat.append(write_str)            


def previous_duplication_avoid():
    pass                
# final_chat = list()
temp_dict = dict()
count = -1
for author_chat in list_chat:
    count += 1
   
    final_message(count, temp_dict)
            
    temp_dict = dict()
   
    if count >0 and author_chat['author'] == list_chat[count-1].get('author'):
        temp_dict['author'] = author_chat['author']
        temp_dict['message'] = ''
        msg = list_chat[count-1].get('message')
      
        new_msg = msg.strip()
        if not new_msg:
            continue
       
        if new_msg[-1].isalpha():
            pass
        else:
            new_msg = new_msg[:-1]
        
        lastTwoWords = new_msg.split()[-2:]
        lastOneWords = new_msg.split()[-1:]
       
        joined_two_word = " ".join(lastTwoWords)
        joined_one_word = "".join(lastOneWords)
      
        if list_chat[count-1].get('message').upper() == author_chat['message'].upper():
            # print("iffffffffff")
            temp_dict['message'] = ''
            continue
        elif joined_two_word.upper() in author_chat['message'].upper():
           
            author_chat['message'] = author_chat['message'].upper()
            joined_two_word = joined_two_word.upper()
            temp_dict['message'] = author_chat['message'].split(joined_two_word,1)[1]
            temp_dict['message'] = temp_dict['message'].lower()
            
            continue
        elif joined_one_word.upper() in author_chat['message'].upper():
           
            author_chat['message'] = author_chat['message'].upper()
            joined_one_word = joined_one_word.upper()
            temp_dict['message'] = author_chat['message'].split(joined_one_word,1)[1]
            temp_dict['message'] = temp_dict['message'].lower()            
            continue
        else:
             temp_dict['message'] = author_chat['message']
             continue
    
        
    if author_chat['author'] == list_chat[count-1].get('author'):
        temp_dict['author'] = author_chat['author']
        if list_chat[count-1].get('message').upper() == author_chat['message'].upper():
            # print("iffffffffff")
            temp_dict['message'] = ''
            continue
        elif list_chat[count-1].get('message').upper() in author_chat['message'].upper():
            temp_dict['message'] = author_chat['message'].replace(list_chat[count-1].get('message'), "")
            continue
        else:
             temp_dict['message'] = author_chat['message']
             continue
         
         
    if count >= 2 and author_chat['author'] == list_chat[count-2].get('author'):
       
        temp_dict['author'] = author_chat['author']
        temp_dict['message'] = ''
        old_msg = list_chat[count-2].get('message')
       
        # print("msg: ", msg)
        # print("temp_dict['author']: ", temp_dict['author'])
        new_msg = old_msg.strip()
        if not new_msg:
            continue
        print("new_msg: ", new_msg)
        if new_msg[-1].isalpha():
            pass
        else:
            new_msg = new_msg[:-1]
        
        lastTwoWords = new_msg.split()[-2:]
        lastOneWords = new_msg.split()[-1:]
       
        joined_two_word = " ".join(lastTwoWords)
        joined_one_word = "".join(lastOneWords)
       
        if list_chat[count-2].get('message').upper() == author_chat['message'].upper():
          
            temp_dict['message'] = ''
            continue
        elif joined_two_word.upper() in author_chat['message'].upper():
            print("joined_two_word: ", joined_two_word)
            print("author_chat['message']: ", author_chat['message'])
            author_chat['message'] = author_chat['message'].upper()
            joined_two_word = joined_two_word.upper()
            temp_dict['message'] = author_chat['message'].split(joined_two_word,1)[1]
            temp_dict['message'] = temp_dict['message'].lower()
            continue
        elif joined_one_word.upper() in author_chat['message'].upper():
            # temp_dict['message'] = author_chat['message'].split(joined_one_word,1)[1]
            author_chat['message'] = author_chat['message'].upper()
            joined_one_word = joined_one_word.upper()
            temp_dict['message'] = author_chat['message'].split(joined_one_word,1)[1]
            temp_dict['message'] = temp_dict['message'].lower()
            continue
        else:
             temp_dict['message'] = author_chat['message']
             continue     
    
    if author_chat['author'] != list_chat[count-1].get('author'):
        temp_dict['author'] = author_chat['author']
        temp_dict['message'] = author_chat['message']
        continue
    else:
        
        if list_chat[count-1].get('message').upper() in author_chat['message'].upper():
            temp_dict['message'] = author_chat['message'].replace(list_chat[count-1].get('message'), "")
            continue
        else:
             temp_dict['message'] = author_chat['message']
             continue
# print(final_chat[0].find(" : "))
# print(final_chat[0][0:10])
# exit()
new_file = "T_TEST_4534.txt"
with open(new_file, "w+") as out_file:
    out_file.writelines(final_chat)
    


# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# from random import randint
# from bs4 import BeautifulSoup
# import os
# from dotenv import load_dotenv
# # create chrome instance
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager

# load_dotenv()

# # get all variable from .env

# MAIL_ID = os.getenv('MAIL_ID')
# PASSWORD = os.getenv('PASSWORD')
# MEET_LINK = os.getenv('MEET_LINK')

# opt = Options()
# opt.add_argument('--disable-blink-features=AutomationControlled')

# opt.add_argument('--start-maximized')
# opt.add_experimental_option("prefs", {
#     "profile.default_content_setting_values.media_stream_mic": 1,
#     "profile.default_content_setting_values.media_stream_camera": 1,
#     "profile.default_content_setting_values.geolocation": 0,
#     "profile.default_content_setting_values.notifications": 1
# })
# print(webdriver.Chrome)
# # driver = webdriver.Chrome(options=opt)
# driver = webdriver.Chrome(chrome_options=opt, executable_path=ChromeDriverManager().install())

# def Glogin(mail_address, password):
#     # Login Page
   
#     driver.get(
#         'https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=https://www.google.com/&ec=GAZAmgQ'
#     )

#     # input Gmail

#     driver.find_element(By.ID, "identifierId").send_keys(mail_address)
#     driver.find_element(By.ID, "identifierNext").click()
#     driver.implicitly_wait(10)

#     # input Password
#     driver.find_element(
#         "xpath", '//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)
#     driver.implicitly_wait(10)
#     driver.find_element(By.ID,"passwordNext").click()

#     # go to google home page
#     driver.get('https://google.com/')
#     time.sleep(1)
    

# def turnOffMicCam():
#     # turn off Microphone
#     time.sleep(1)
#     driver.find_element(by=By.XPATH,
#         value='//*[@id="yDmH0d"]/c-wiz/div/div/div[10]/div[3]/div/div[1]/div[4]/div/div/div[1]/div[1]/div/div[4]/div[1]').click()
#     driver.implicitly_wait(10)

#     # turn off camera
#     time.sleep(1)
#     driver.find_element(by=By.XPATH,
#         value='//*[@id="yDmH0d"]/c-wiz/div/div/div[10]/div[3]/div/div[1]/div[4]/div/div/div[1]/div[1]/div/div[4]/div[2]').click()
#     driver.implicitly_wait(10)
    
# def joinNow():
#     # Join meet
#     print(1)
#     time.sleep(1)
#     driver.implicitly_wait(10)
#     driver.find_element(by=By.XPATH,
#         value='//*[@id="yDmH0d"]/c-wiz/div/div/div[10]/div[3]/div/div[1]/div[4]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/button').click()
#     driver.implicitly_wait(10)
#     print(1)

# # assign email id and password

# mail_address = MAIL_ID
# password = PASSWORD


# # login to Google account
# Glogin(mail_address, password)

# # go to google meet
# driver.get(MEET_LINK)
# turnOffMicCam()
# joinNow()

# driver.implicitly_wait(20)

# # turn on Caption
# try:
#     wait = WebDriverWait(driver, 30)
#     wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.VfPpkd-Bz112c-LgbsSe.fzRBVc.tmJved.xHd4Cb.rmHNDe"))).click()
#     print("google meets screen is diplayed.....")
# except:
#     print("google meets screen not displayed.....")
#     driver.quit()

    
# time.sleep(5)

# """
# To get all HTML code of captions stored in file in every 2 sec sleep.
# File name taken by generating random number from 0000, 9999
# Breaking while loop after meeting got ended.
# """

# random_name = randint(0000,9999)
# file_name = f'DEMO_{random_name}.txt'
# auth_text = ''
# while True:
#    try:
#         time.sleep(2)
#         with open(file_name, "a") as file_object:
#             if auth_text != driver.find_element(By.CSS_SELECTOR, "div.K6EKFb").get_attribute("innerHTML"):
#                 file_object.write(str(auth_text))
#                 file_object.write("\n")
#             auth_text = driver.find_element(By.CSS_SELECTOR, "div.K6EKFb").get_attribute("innerHTML")
        
#    except:
#        break

# list_chat = list()
# with open(file_name,"rb") as file_data:
#     for line in file_data.readlines():
#         # temp_dict = dict()
#         html_content = line.decode().strip()
#         bs4_content = BeautifulSoup(html_content,'html.parser')
#         chatbox_html = bs4_content.find_all("div",class_="TBMuR bj4p3b")
#         for chat in chatbox_html:
#             temp_dict = dict()
#             span_msg = chat.find("div", class_="zs7s8d jxFHg").decode_contents().strip()
#             if span_msg:
#                 temp_dict["author"] = span_msg
#                 author_message = chat.find("div", class_="iTTPOb VbkSUe")
#                 if author_message:
#                     temp_dict["message"] = author_message.text
#                 else:
#                     temp_dict["message"] = ""
#                 list_chat.append(temp_dict)
           
#                 print(temp_dict)
                
# # print(list_chat)
       
# # exit()               
                
# final_chat = list()
# temp_dict = dict()
# count = -1
# for author_chat in list_chat:
#     count += 1
   
#     if temp_dict:
#         if temp_dict['message']:
#             temp_dict['message'] = temp_dict['message'].strip()
#             if temp_dict['message'][0].isalpha():
#                 pass
#             else:
#                 temp_dict['message'] = temp_dict['message'][1:]
                
#             write_str = f"{temp_dict['author']} : {temp_dict['message']}\n\n"
#             final_chat.append(write_str)
            
#     temp_dict = dict()
   
#     if count >0 and author_chat['author'] == list_chat[count-1].get('author'):
#         temp_dict['author'] = author_chat['author']
#         temp_dict['message'] = ''
#         msg = list_chat[count-1].get('message')
      
#         new_msg = msg.strip()
#         if not new_msg:
#             continue
       
#         if new_msg[-1].isalpha():
#             pass
#         else:
#             new_msg = new_msg[:-1]
        
#         lastTwoWords = new_msg.split()[-2:]
#         lastOneWords = new_msg.split()[-1:]
       
#         joined_two_word = " ".join(lastTwoWords)
#         joined_one_word = "".join(lastOneWords)
      
#         if list_chat[count-1].get('message').upper() == author_chat['message'].upper():
#             # print("iffffffffff")
#             temp_dict['message'] = ''
#             continue
#         elif joined_two_word.upper() in author_chat['message'].upper():
           
#             author_chat['message'] = author_chat['message'].upper()
#             joined_two_word = joined_two_word.upper()
#             temp_dict['message'] = author_chat['message'].split(joined_two_word,1)[1]
#             temp_dict['message'] = temp_dict['message'].lower()
            
#             continue
#         elif joined_one_word.upper() in author_chat['message'].upper():
           
#             author_chat['message'] = author_chat['message'].upper()
#             joined_one_word = joined_one_word.upper()
#             temp_dict['message'] = author_chat['message'].split(joined_one_word,1)[1]
#             temp_dict['message'] = temp_dict['message'].lower()            
#             continue
#         else:
#              temp_dict['message'] = author_chat['message']
#              continue
    
        
#     if author_chat['author'] == list_chat[count-1].get('author'):
#         temp_dict['author'] = author_chat['author']
#         if list_chat[count-1].get('message').upper() == author_chat['message'].upper():
#             # print("iffffffffff")
#             temp_dict['message'] = ''
#             continue
#         elif list_chat[count-1].get('message').upper() in author_chat['message'].upper():
#             temp_dict['message'] = author_chat['message'].replace(list_chat[count-1].get('message'), "")
#             continue
#         else:
#              temp_dict['message'] = author_chat['message']
#              continue
         
         
#     if count >= 2 and author_chat['author'] == list_chat[count-2].get('author'):
       
#         temp_dict['author'] = author_chat['author']
#         temp_dict['message'] = ''
#         msg = list_chat[count-2].get('message')
       
#         print("msg: ", msg)
#         print("temp_dict['author']: ", temp_dict['author'])
#         new_msg = msg.strip()
#         if not new_msg:
#             continue
#         print("new_msg: ", new_msg)
#         if new_msg[-1].isalpha():
#             pass
#         else:
#             new_msg = new_msg[:-1]
        
#         lastTwoWords = new_msg.split()[-2:]
#         lastOneWords = new_msg.split()[-1:]
       
#         joined_two_word = " ".join(lastTwoWords)
#         joined_one_word = "".join(lastOneWords)
       
#         if list_chat[count-2].get('message').upper() == author_chat['message'].upper():
          
#             temp_dict['message'] = ''
#             continue
#         elif joined_two_word.upper() in author_chat['message'].upper():
#             print("joined_two_word: ", joined_two_word)
#             print("author_chat['message']: ", author_chat['message'])
#             author_chat['message'] = author_chat['message'].upper()
#             joined_two_word = joined_two_word.upper()
#             temp_dict['message'] = author_chat['message'].split(joined_two_word,1)[1]
#             temp_dict['message'] = temp_dict['message'].lower()
#             continue
#         elif joined_one_word.upper() in author_chat['message'].upper():
#             # temp_dict['message'] = author_chat['message'].split(joined_one_word,1)[1]
#             author_chat['message'] = author_chat['message'].upper()
#             joined_one_word = joined_one_word.upper()
#             temp_dict['message'] = author_chat['message'].split(joined_one_word,1)[1]
#             temp_dict['message'] = temp_dict['message'].lower()
#             continue
#         else:
#              temp_dict['message'] = author_chat['message']
#              continue     
    
#     if author_chat['author'] != list_chat[count-1].get('author'):
#         temp_dict['author'] = author_chat['author']
#         temp_dict['message'] = author_chat['message']
#         continue
#     else:
        
#         if list_chat[count-1].get('message').upper() in author_chat['message'].upper():
#             temp_dict['message'] = author_chat['message'].replace(list_chat[count-1].get('message'), "")
#             continue
#         else:
#              temp_dict['message'] = author_chat['message']
#              continue

# new_file_name = f"CHAT_{file_name}"
# with open(new_file_name,"w+") as out_file:
#     out_file.writelines(final_chat)
    
    
