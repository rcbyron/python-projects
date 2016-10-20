from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

import time

base_url = "https://utdirect.utexas.edu/registration/chooseSemester.WBX"
username = "rcb2746"
password = input("Password: ")

xpaths = {
    'semester_btn': "//input[contains(@value, 'Spring 2016')]",
    'reg_closed':   "//form/div/p[contains(text(), 'not allowed')]"
}

browser = webdriver.Firefox()

global reg_url


def login():
    browser.get(base_url)
    # browser.maximize_window()

    browser.find_element_by_id('IDToken1').clear()
    browser.find_element_by_id('IDToken1').send_keys(username)

    browser.find_element_by_id('IDToken2').clear()
    browser.find_element_by_id('IDToken2').send_keys(password)
    browser.find_element_by_id('IDToken2').submit()


def open_reg_page():
    global reg_url
    reg_url = browser.current_url

    reg_is_open = False
    while not reg_is_open:
        try:
            browser.find_element_by_xpath(xpaths['semester_btn']).click()
            # reg_div = browser.find_element_by_id('regContent')
            # reg_div.find_element_by_xpath(xpaths['reg_closed'])
            error_div = browser.find_element_by_id('service_content')
            error_div.find_element_by_class_name('error')

            print("Registration still closed. Trying again in 1 second...")
            time.sleep(1)
            browser.get(reg_url)
        except NoSuchElementException:
            reg_is_open = True

    print('WOOHOO! WE ARE IN BABY!\n')


def temp_open():
    global reg_url
    reg_url = 'file:///C:/Users/Connor/Downloads/Registrationerror.html'
    browser.get(reg_url)


def add_class(course):
    global msg_box
    msg_box = browser.find_element_by_id('n_message')
    add_input = browser.find_element_by_id('s_unique_add')

    add_input.clear()
    add_input.send_keys(course)
    add_input.submit()


def try_list(courses, name):
    print("Trying courses for: " + name)
    for course in courses:
        try:
            add_class(course)
        except:
            print("CRITICAL ERROR FINDING REGISTRATION PAGE!")
            browser.get(reg_url)
            add_class(course)

        try:
            global msg_box
            msg_box.find_element_by_class_name('error')
            print("Error adding class: " + str(course))
        except:
            pass
            # print("Successfully added: " + str(course))
            # return
    print("All attempts unsuccessful :(\n")

login()
open_reg_page()
# temp_open()

m325k_courses = ['53380', '53365', '53360', '53355']
m348_courses = ['53610', '53605']
ee313_courses = ['16015', '16020', '16010']
ee333t_courses = ['16255', '16245', '16240', '16250', '16230', '16235']

try_list(m325k_courses, "M325K - DISCRETE MATH")
try_list(m348_courses, "M348 - NUMERICAL ANALYSIS")
try_list(ee313_courses, "EE313 - LINEAR SIGNALS")
try_list(ee333t_courses, "EE333T - COMMUNICATIONS")
