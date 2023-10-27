from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
import MobilePayment

import BetweenCards
import AnyCard

class Birbank:
    def __init__(self):
        with open(file = 'card_place.txt', mode = 'r') as card:
            self.card_place = card.read()

        desired_caps = {
            'platformName': "Android",
            'deviceName': "27de7021"
        }
        capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)

        self.driver = webdriver.Remote(command_executor = 'http://localhost:4723/wd/hub', options = capabilities_options)
        self.sequel = True

    def Choice(self):
        choice = input("1-To The Any Card Of Bank\n2-Between your Cards And Accounts\n"
                       "3-Mobile Operators\n4-Stop The Program\nChoose One Of The Up Options Above:")
        while choice not in '1234':
            choice = input('Choose One Of The Up Options Above:')

        if choice == '1' : AnyCard.Any_BankCard(self.driver, self.card_place)
        elif choice == '2' : BetweenCards.Betweeen_Cards(self.driver)
        elif choice == '3' : MobilePayment.Mobile_Operators(self.driver, self.card_place)
        if choice == '4' : self.sequel = False


birbank = Birbank()

while birbank.sequel:
    birbank.Choice()
