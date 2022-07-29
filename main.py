from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


def Glogin(mail_address, password):
    # Login Page
    driver.get(
        'https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=https://www.google.com/&ec=GAZAAQ')

    # input Gmail

    usermail = driver.find_element("id", "identifierId")
    
    usermail.click()
    
    # driver.find_elements_by_id("identifierNext").click()

    usermail.send_keys(mail_address)
    
    driver.implicitly_wait(10)
   
    next =  driver.find_element("id", "identifierNext")
    
    next.click()
    time.sleep(2)
    
    # input Password

    password = driver.find_element(by=By.XPATH, value= '//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)
    driver.implicitly_wait(10)
    
    nxt = driver.find_element("id", "passwordNext")
    nxt.click()
    driver.implicitly_wait(10)
   
    # go to google home page
    driver.get("https://google.com")
    driver.implicitly_wait(100)

def turnOffMicCam():
    # turn off Microphone
    time.sleep(2)
    driver.find_element(by=By.XPATH, value= '//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[4]/div[1]/div/div/div').click()
    driver.implicitly_wait(10)

    # turn off camera
    time.sleep(1)
    driver.find_element(by=By.XPATH, value= '//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[4]/div[2]/div/div').click()
    driver.implicitly_wait(10)


def joinNow():
    # Join meet
    print(1)
    
    driver.implicitly_wait(10)
    driver.find_element(By.CSS_SELECTOR, 'div.uArJ5e.UQuaGc.Y5sE8d.uyXBBb.xKiqt').click()
    print(1)


def AskToJoin():
    # Ask to Join meet
    
    driver.implicitly_wait(10)
    driver.find_element(By.CSS_SELECTOR, 'div.uArJ5e.UQuaGc.Y5sE8d.uyXBBb.xKiqt').click()
    # Ask to join and join now buttons have same xpaths

def joinmeet():
    pass
# assign email id and password
mail_address = 'test@rapidinnovation.dev'
password = 'test@1234'

# create chrome instance
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
# driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver = webdriver.Chrome(chrome_options=opt, executable_path=ChromeDriverManager().install())

# login to Google account
Glogin(mail_address, password)

# go to google meet
driver.get('https://meet.google.com/qoj-xcih-zie')
time.sleep(5)

ask = driver.find_element("id", "c4")
    
ask.click()
    
# driver.find_elements_by_id("identifierNext").click()
print("o"*10, "ask to join")
ask.send_keys("komal")
driver.implicitly_wait(100)
driver.find_element(by=By.XPATH, value = "//*[contains(text(), 'Ask to join')]").click()
driver.implicitly_wait(100)
print("p"*10, "captions")
# driver.find_element(by=By.XPATH, value = "//*[@id=\"ow3\"]/div[1]/div/div[10]/div[3]/div[10]/div[2]/div/div[3]/span/button").click()
time.sleep(5)
print(driver.find_element(by=By.XPATH, value="//*[@id=\"ow3\"]/div[1]/div/div[10]/div[3]/div[7]/div[1]/div[1]/div").get_attribute("innerHTML"))
print("q"*10, " css")
tt = driver.find_element(By.CSS_SELECTOR, "div.iTTPOb.VbkSUe > span")
print("r"*10, " css1")
for i in len(tt):
    print(driver.find_element(By.CSS_SELECTOR, "div.iTTPOb.VbkSUe > span").get_attribute("innerHTML"))

# turnOffMicCam()
# AskToJoin()
# joinNow()
