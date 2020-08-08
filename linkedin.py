# basic modules required selenium is an automation package
#web driver of any web browser
#
from selenium import webdriver
from selenium.webdriver.common.by import By

#location of chrome driver
driver=webdriver.Chrome(r"C:\\Users\\Brunda\\Downloads\\chro.zip\\chromedriver.exe")
driver.get('https://www.linkedin.com/')
driver.find_element(By.XPATH,'//*[contains(concat( " ", @class, " " ), concat( " ", "nav__button-secondary", " " ))]').click()

email=['your email@anymail.com']
password=['password']
inputemail='//*[(@id = "username")]'
inputpass='//*[(@id = "password")]'
submit='//*[contains(concat( " ", @class, " " ), concat( " ", "from__button--floating", " " ))]'
def check():

        driver.find_element_by_xpath(inputemail).send_keys(email[0])
        driver.find_element_by_xpath(inputpass).send_keys(password[0])
        driver.find_element_by_xpath(submit).click()
def notifications():
    driver.get('https://www.linkedin.com/notifications/')
    driver.maximize_window()
    s=driver.save_screenshot("C://Users/Brunda/Desktop/home.png")
    get_info()

def get_info():
    driver.close()









check()
notifications()
