from time import sleep
from selenium import webdriver
import chromedriver_binary
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import config


def set_user_info():
    username = config.USERNAME
    password = config.PASSWORD
    return username, password

def login_utas(driver, username, password):
    driver.get('https://utas.adm.u-tokyo.ac.jp/campusweb/campusportal.do')
    driver.find_elements_by_tag_name('button')[-1].click()
    sleep(3)
    driver.find_element_by_id('userNameInput').send_keys(username)
    driver.find_element_by_id('passwordInput').send_keys(password)
    driver.find_element_by_id('submitButton').click()


def open_course_page(driver, course_name):
    driver.find_element_by_id('tab-sy').click()
    sleep(10)
    driver.find_element_by_id('tabmenu-span').find_elements_by_class_name('menu-func')[-1].click()
    sleep(15)
    iframe = driver.find_element_by_tag_name('iframe')
    driver.switch_to_frame(iframe)
    sleep(5)
    driver.find_element_by_partial_link_text(course_name).click()
    new_handle = driver.window_handles[-1]
    driver.switch_to_window(new_handle)


def pick_up_zoom(driver):
    driver.find_element_by_partial_link_text('Detailed Information').click()
    zoom_url = driver.find_element_by_partial_link_text('zoom.us').get_attribute('textContent')
    return zoom_url


def main():
    course_name = '計量経済学' # argvから取得するよう変更

    username, password = set_user_info()
    driver = webdriver.Chrome()
    login_utas(driver, username, password)
    sleep(10)
    open_course_page(driver, course_name)
    sleep(1)
    zoom_url = pick_up_zoom(driver)
    print(zoom_url)


if __name__ == '__main__':
    main()
