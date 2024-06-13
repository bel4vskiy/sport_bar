import time

import requests
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from models import *


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))




# class Site:
#   #empty constructor
#   def __init__(self):
#     pass

def checkAnotherActivity():
    url = 'http://127.0.0.1:5000/api/availability?activity=basketball'
    data = requests.get(url).json()
    return data['message'] == 'This activity is not exists'

def checkRightActivity():
    url = 'http://127.0.0.1:5000/api/availability?activity=billiard'
    data = requests.get(url).json()
    return data[0]['available'] == True or data[0]['available'] == False

def checkBooking():
    url = 'http://127.0.0.1:5000'
    driver.get(url)

    select_element = driver.find_element(By.NAME, 'activity')
    select = Select(select_element)
    select.select_by_value('bowling')

    input_num_people = driver.find_element(By.NAME, 'people').send_keys('3')
    input_customer_name = driver.find_element(By.NAME, 'customer_name').send_keys('Stanislaw')

    button_booking = driver.find_element(By.NAME, 'button_sub').click()
    time.sleep(5)
    cursor.execute("SELECT * FROM Booking WHERE activity_name= ? AND customer_name= ? AND booked_date = ?", ('bowling', 'Stanislaw', '12:00'))
    driver.close()
    return cursor.fetchall() == [(2, 'bowling', '12:00', 31, 'Stanislaw')]



class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(checkAnotherActivity(), True)

    def test_something1(self):
        self.assertEqual(checkRightActivity(), True)

    def testing_booking(self):
        self.assertEqual(checkBooking(), True)

if __name__ == '__main__':
    unittest.main()
