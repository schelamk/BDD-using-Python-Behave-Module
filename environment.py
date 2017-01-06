from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def before_scenario(context, scenario):
    context.browser = webdriver.Chrome()
    context.browser.maximize_window()
    context.browser.implicitly_wait(2)

def after_scenario(context, scenario):
    context.browser.quit()