#!/usr/bin/python
#
#       _           _       ____        _             _         _                     
#__   _(_)_ __ __ _(_)_ __ |  _ \ _   _| |___  ___   / \  _   _| |_ ___   _ __  _   _ 
#\ \ / / | '__/ _` | | '_ \| |_) | | | | / __|/ _ \ / _ \| | | | __/ _ \ | '_ \| | | |
# \ V /| | | | (_| | | | | |  __/| |_| | \__ \  __// ___ \ |_| | || (_) || |_) | |_| |
#  \_/ |_|_|  \__, |_|_| |_|_|    \__,_|_|___/\___/_/   \_\__,_|\__\___(_) .__/ \__, |
#             |___/                                                      |_|    |___/ 

import sys, getopt
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import datetime
from selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Install pip: http://stackoverflow.com/questions/4750806/how-do-i-install-pip-on-windows
# Install selenium via http://selenium-python.readthedocs.io/installation.html (pip install selenium)
# Please install Chrome driver via https://chromedriver.storage.googleapis.com/index.html?path=2.27/
# Webdriver Documentation:
# http://selenium-python.readthedocs.io/locating-elements.html

def usage():
    print "virginPulseAuto.py -u <username> -p <password>"

def main():
    # Get username and password args from command line.
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'u:p:') # get the args
    except getopt.GetoptError as err:
        print str(err)  # will print something like "option -a not recognized"
        usage()
        exit()
    username = None
    password = None
    for option, arg in opts:
        if   option == "-u":
            username = arg
        elif option == "-p":
            password = arg
        else:
            assert False, "unrecognized option!"
    if username == None or password == None:
        usage()
        exit()


    # Start up the browser!
    driver = webdriver.Chrome()
    
    # for windows
    #driver = webdriver.Chrome("C:\Users\eripflo\AppData\Local\Temp\Rar$EXa0.403\chromedriver.exe")
    ##
    
    # Log in with username and password
    print 'Logging in to Virgin Pulse.'
    driver.get("https://member.virginpulse.com/login.aspx")
    time.sleep(10)  # Give the page time to load.
    driver.find_element_by_id('username').send_keys(username)
    driver.find_element_by_id('password').send_keys(password)
    driver.find_element_by_name('login').click()
    time.sleep(5)  # Give the page time to load.
    
    # Navigate to the tracking page
    driver.get("https://app.member.virginpulse.com/#/healthyhabits")
    time.sleep(3)  # Give the page time to load.
    
    # Enter sleep hours
    driver.find_element_by_id('sleepHours').send_keys('8')
    driver.find_element_by_id('track-sleep').click()
    time.sleep(1)

    # Enter steps
    driver.find_element_by_id('numberOfSteps').send_keys('5000')
    driver.find_element_by_id('track-steps').click()
    time.sleep(1)

    # Enter workout
    # In my case, 60 minutes of Circuit Training on Mon, Wed, Friday.
    dayOfWeek = datetime.datetime.today().weekday()
    if(    dayOfWeek == 0   # Monday
        or dayOfWeek == 2   # Wednesday
        or dayOfWeek == 4): # Friday
        driver.find_element_by_id('steps-converter-activity-input').send_keys('Circuit Training' + Keys.ENTER)
        driver.find_element_by_id('steps-converter-time-input').send_keys('60')
        driver.find_element_by_id('steps-converter-submit').click()
        time.sleep(1)

    # Stair Tracker
    # "Did you take the stairs today?"  Why, yes as a matter of fact.
    driver.find_element_by_id('tracker-13-track-yes').click()
    time.sleep(1)

    # Breakfast tracker
    # "Did you eat a healthy breakfast today?"  Whole Greek yougurt or bust.
    driver.find_element_by_id('tracker-44-track-yes').click()
    time.sleep(1)

    # Exit.
    # "Go on, git!"
    driver.close()
    exit()

    
# Python boilerplate
if __name__ == "__main__":
    main()
