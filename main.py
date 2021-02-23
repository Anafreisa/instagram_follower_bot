from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
import time

CHROME_DRIVER_PATH = PATH OF THE CHROME DRIVER
USERNAME = YOUR INSTAGRAM USERNAME
PASSWORD = YOUR INSTAGRAM PASSWORD
SIMILAR_ACCOUNT = ACCOUNT YOU WANT THE FOLLOWERS


class InstaFollower:

    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)

    def login(self):
        self.driver.get("https://www.instagram.com/")

        # If you need to choose the account:

        # time.sleep(2)
        # change_account = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div['
        #                                                    '2]/div/p/button[1]')
        # change_account.click()

        time.sleep(2)
        login = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        login.send_keys(USERNAME)

        password = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.send_keys(PASSWORD)
        time.sleep(2)
        password.send_keys(Keys.ENTER)

        time.sleep(4)
        save_informations = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div'
                                                                  '/section/div/button')
        save_informations.click()

        time.sleep(4)
        active_notifications = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
        active_notifications.click()

    def find_followers(self):
        self.driver.get(f'https://www.instagram.com/{SIMILAR_ACCOUNT}/')

        time.sleep(2)
        followers = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li['
                                                      '2]/a/span')
        followers.click()

        time.sleep(2)
        modal = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        all_btns = self.driver.find_elements_by_css_selector("li button")
        for button in all_btns:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()

bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()
